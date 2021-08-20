import socket
import select
import errno
import sys

headerLength = 10
if len(sys.argv) != 3:
	print ("How to make it work: script, IP address, PORT number")
	exit()

# The first argument from the prompt is saved in IP_ADDRESS as a IP address.
IP = str(sys.argv[1])

# The second argument from the prompt is saved in PORT as a port number.
port = int(sys.argv[2])

print('Connect, write your Username')
while True:
    myUsername = input("User: ")
    if len(myUsername) > 0:
        break
    else:
        print('Write your Username')

conection = socket.SOCK_STREAM
addripv4 = socket.AF_INET
socketCliente = socket.socket(addripv4, conection)
socketCliente.connect((IP, port))
socketCliente.setblocking(False)
username = myUsername.encode('utf-8')
userHeader = f"{len(username):<{headerLength}}".encode('utf-8')
socketCliente.send(userHeader + username)
while True:

    message = input('{} > '.format(myUsername))

    if len(message) != 0:
        message = message.encode('utf-8')
        msgHeader = f"{len(message):<{headerLength}}".encode('utf-8')
        socketCliente.send(msgHeader + message)

    try:
        while True: 
            userHeader = socketCliente.recv(headerLength)

            if not len(userHeader):
                print('No data received, the server will close')
                sys.exit()

            userLength = int(userHeader.decode('utf-8').strip())
            username = socketCliente.recv(userLength).decode('utf-8')
            msgHeader = socketCliente.recv(headerLength)
            msgLength = int(msgHeader.decode('utf-8').strip())
            message = socketCliente.recv(msgLength).decode('utf-8')
            print('{} > {}'.format(username, message))

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Error: {}'.format(str(e)))
            sys.exit()

        continue

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit()

    except KeyboardInterrupt as e:
        print('Error: {}'.format(str(e)))
        sys.exit()
