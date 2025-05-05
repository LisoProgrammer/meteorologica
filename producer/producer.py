import pika
import json
import time
import random

# Función para generar datos meteorológicos simulados
def generate_weather_data():
    return {
        "station_id": "ST-001",
        "temperature": round(random.uniform(-10, 40), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

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

# Conexión a RabbitMQ
connection = connect_to_rabbitmq()
channel = connection.channel()

# Declarar el intercambio en RabbitMQ
channel.exchange_declare(exchange='weather_logs', exchange_type='direct', durable=True)

# Publicar mensajes en el ciclo principal
while True:
    data = generate_weather_data()
    message = json.dumps(data)

    # Enviar el mensaje a RabbitMQ
    channel.basic_publish(
        exchange='weather_logs',
        routing_key='log.weather',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # Hacer que el mensaje sea persistente
        )
    )

    print(f"Enviado: {message}")
    time.sleep(2)
