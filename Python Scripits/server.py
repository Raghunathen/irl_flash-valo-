
from http.server import BaseHTTPRequestHandler, HTTPServer

my_request = None
text = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    tmp = open('text.txt', 'r')
    txt = tmp.read()
    #txt = "yoru"
    global my_request, text
    my_request = self.requestline
    my_request = str(text)[5 : int(len(my_request) - 9)]
    print('received request')
    print(my_request)
    print(txt)
    messagetosend = bytes(txt,"utf")
    tmp.close()
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    return



server_address_httpd = ('192.168.0.41',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('server started')
httpd.serve_forever()