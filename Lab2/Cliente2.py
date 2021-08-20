import http.client
import sys
import errno

if len(sys.argv) != 3:
	print ("How to make it work: script, IP address, PORT number")
	exit()

# The first argument from the prompt is saved in IP_ADDRESS as a IP address.
IP = str(sys.argv[1])

# The second argument from the prompt is saved in PORT as a port number.
PORT = int(sys.argv[2])

conn = http.client.HTTPConnection(IP,PORT)
while True:
    while True:
        myUsername = input("User: ")
        if len(myUsername) > 0:
            break
        else:
            print('Write your Username')
    conn.request("POST","/user",myUsername.encode())
    r2 = conn.getresponse()
    if (r2.status == 201):
        break
    else:
        print("Username taken")


while True:
    try:
        while True:
            message = input('{}>'.format(myUsername))
            if len(message) != 0:
                message = myUsername +">"+message
                conn.request("POST","/",message.encode())
                r2 = conn.getresponse()

            conn.request("POST","/getMsg",myUsername.encode())
            r1 = conn.getresponse()
            d1 = r1.read()
            d1 = d1.decode()
            print(d1[2:])

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Error: {}'.format(str(e)))
            conn.close()
            sys.exit()
        
        continue

    except Exception as e:
        print('Error: {}'.format(str(e)))
        conn.close()
        sys.exit()

    except KeyboardInterrupt as e:
        print('Error: {}'.format(str(e)))
        conn.close()
        sys.exit()

conn.close()