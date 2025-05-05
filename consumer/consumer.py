import pika
import psycopg2
import json
import time

# Función para conectar a RabbitMQ
def connect_to_rabbitmq(retries=5, delay=5):
    for i in range(retries):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials('user', 'pass')))
            print("Conexión exitosa a RabbitMQ")
            return connection
        except pika.exceptions.AMQPConnectionError:
            print(f"Intento {i+1}: RabbitMQ no disponible, reintentando en {delay} segundos...")
            time.sleep(delay)
    raise Exception("No se pudo conectar a RabbitMQ después de varios intentos")

# Función para conectar a PostgreSQL
def connect_to_postgres():
    try:
        conn = psycopg2.connect(
            dbname='weatherdb', user='postgres', password='postgres', host='db'
        )
        return conn
    except Exception as e:
        print(f"Error al conectar a PostgreSQL: {e}")
        return None

# Callback para procesar los mensajes
def callback(ch, method, properties, body):
    data = json.loads(body)
    try:
        # Validar temperatura dentro del rango
        if not (-50 <= data["temperature"] <= 50):
            raise ValueError("Temperatura fuera de rango")

        # Conectar a PostgreSQL
        conn = connect_to_postgres()
        if conn is None:
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            return

        # Insertar los datos en la base de datos
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO weather_logs (station_id, temperature, humidity, timestamp) VALUES (%s, %s, %s, %s)",
            (data["station_id"], data["temperature"], data["humidity"], data["timestamp"])
        )
        conn.commit()
        cur.close()
        conn.close()

        print(f"Guardado en BD: {data}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print("Error procesando:", e)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

# Conexión a RabbitMQ
connection = connect_to_rabbitmq()
channel = connection.channel()

# Declarar la cola y el intercambio
channel.exchange_declare(exchange='weather_logs', exchange_type='direct', durable=True)
channel.queue_declare(queue='weather_data', durable=True)
channel.queue_bind(exchange='weather_logs', queue='weather_data', routing_key='log.weather')

# Configurar la calidad del servicio y empezar a consumir mensajes
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='weather_data', on_message_callback=callback)
channel.start_consuming()
