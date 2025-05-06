import pika

try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'pass'))
    )
    print("Conexión exitosa a RabbitMQ")
except Exception as e:
    print("Error:", e)
