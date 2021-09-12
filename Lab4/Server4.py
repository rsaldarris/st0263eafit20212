import pika
import sys

if len(sys.argv) != 2:
	print ("How to make it work: script, IP address")
	exit()

IP = ' '.join(sys.argv[1]) # or "54.89.218.72"

connection = pika.BlockingConnection(pika.ConnectionParameters(IP, 5672, '/',
pika.PlainCredentials("user", "password")))
channel = connection.channel()
def callback(ch, method, properties, body):
        print(f'{body} is received')
channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)

while True:
    try:
        channel.start_consuming()

    except KeyboardInterrupt:
        channel.stop_consuming()
        sys.exit()