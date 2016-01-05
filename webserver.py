#!/usr/bin/python3
#*-*Coding: UTF-8 *-*

from http.server import BaseHTTPRequestHandler, HTTPServer

class SQHandler(BaseHTTPRequestHandler):

    def foo(self):

        return {'id':676,
                'hello':'world'}

    def do_GET(self):
        print(self.requestline)

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        resp = self.foo()
        resp = str(resp)
        
        self.wfile.write(resp.encode("utf-8"))


if __name__ == "__main__":
    PORT = 8000
    server = HTTPServer(('',PORT), SQHandler)
    print("starting server on port "+str(PORT))
    server.serve_forever()
