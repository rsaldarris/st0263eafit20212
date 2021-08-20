import socket
import select
import sys

headerLength = 10


if len(sys.argv) != 3:
	print ("How to make it work: script, IP address, PORT number")
	exit()

# The first argument from the prompt is saved in IP_ADDRESS as a IP address.
IP = str(sys.argv[1])

# The second argument from the prompt is saved in PORT as a port number.
port = int(sys.argv[2])

addripv4 = socket.AF_INET
conection = socket.SOCK_STREAM 
socketServer = socket.socket(addripv4, conection)
socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketServer.bind((IP, port))
socketServer.listen()
socketList = [socketServer]
clients = {}

print(f'Connection from {IP}:{port}')
def msgReceived(clientSocket):

    try:
        msgHeader = clientSocket.recv(headerLength)

        if not len(msgHeader):
            return False

        msgLength = int(msgHeader.decode('utf-8').strip())
        return {'header': msgHeader, 'data': clientSocket.recv(msgLength)}

    except:
        return False


while True:

    socketRead, _, socketException = select.select(
        socketList, [], socketList)

    for socketNotification in socketRead:

        if socketNotification == socketServer:
            clientSocket, clientAddres = socketServer.accept()
            username = msgReceived(clientSocket)

            if username is False:
                continue

            socketList.append(clientSocket)
            clients[clientSocket] = username

            print('Connection accepted from {}:{}, Username: {}'.format(
                *clientAddres, username['data'].decode('utf-8')))

        else:

            message = msgReceived(socketNotification)
            if message is False:
                print('Closed connection from: {}'.format(
                    clients[socketNotification]['data'].decode('utf-8')))

                socketList.remove(socketNotification)
                del clients[socketNotification]

                continue

            username = clients[socketNotification]

            print('Received message from {}: {}'.format(
                username["data"].decode("utf-8"), message["data"].decode("utf-8")))

            for clientSocket in clients:

                if clientSocket != socketNotification:

                    clientSocket.send(
                        username['header'] + username['data'] + message['header'] + message['data'])

    for socketNotification in socketException:
        socketList.remove(socketNotification)
        del clients[socketNotification]
