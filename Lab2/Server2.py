from http.server import HTTPServer, BaseHTTPRequestHandler
import select
import sys

if len(sys.argv) != 3:
	print ("How to make it work: script, IP address, PORT number")
	exit()

# The first argument from the prompt is saved in IP_ADDRESS as a IP address.
IP = str(sys.argv[1])

# The second argument from the prompt is saved in PORT as a port number.
PORT = int(sys.argv[2])

messages={}

class msgHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        userName = ""
        msg = messages.get(userName)
        messages[userName] = ""
        msg = "nada"
        self.wfile.write(msg.encode())

    def do_POST(self):
        if(self.path.endswith("/user")):
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            post_body = post_body.decode()
            if messages.get(post_body) == None:
                messages[post_body] = ""
                self.send_response(201)
                self.send_header('content-type','text/html')
                self.end_headers()
                print("User registered "+post_body)
            else:
                self.send_response(401)
                self.send_header('content-type','text/html')
                self.end_headers()

        elif(self.path.endswith("/getMsg")):
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len).decode()
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            mensajes = messages.get(post_body)
            messages[post_body] = ""
            self.wfile.write(mensajes.encode())

        else:
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            post_body = post_body.decode()
            userName = post_body.split(">")[0]
            for name in messages:
                if name != userName:
                    msg = messages.get(name)
                    msg = msg +"\n"+post_body
                    messages[name] = msg
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            # self.wfile.write('POST'.encode())

def main():
    server = HTTPServer((IP,PORT),msgHandler)
    print("Server running on port %s" %PORT)
    server.serve_forever()

if __name__ == "__main__":
    main()