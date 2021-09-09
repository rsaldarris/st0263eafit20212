import pika
import sys


if len(sys.argv) != 2:
	print ("How to make it work: script, IP address, message")
	exit()

IP = ' '.join(sys.argv[1]) # or "54.89.218.72"

# message = ' '.join(sys.argv[2:]) or "Hello World!"


connection = pika.BlockingConnection(pika.ConnectionParameters(IP, 5672, '/',
pika.PlainCredentials('user', 'password')))
channel = connection.channel()

print('Connect, write your Username')
while True:
    myUsername = input("User: ")
    if len(myUsername) > 0:
        break
    else:
        print('Write your Username')

print('Connect, write your Email')
while True:
    myEmail = input("Email: ")
    if len(myEmail) > 0:
        break
    else:
        print('Write your Email')

msg = " "+myEmail+" "+myUsername
while True:
    task = input("Task: ")
    if(task == "Exit")
        sys.exit()
    if len(task) > 0:
        task+=msg
        channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=task)
        break
    else:
        print('Write the task or write Exit to exit the programm')


# message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print("Runnning Producer Application...")
print(" [x] Sent %r" % message)
connection.close()


