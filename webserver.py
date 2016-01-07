#!/usr/bin/python3
#*-*Coding: UTF-8 *-*

from http.server import BaseHTTPRequestHandler, HTTPServer
import re
import json
from crud import CRUD

class SQHandler(BaseHTTPRequestHandler):
    
    def get(self,requestline, param):
        """
        retrieve parameter from urls
        """
        value=None
        try:
            pattern = re.compile(r'.*'+param+'=(?P<argument>\w*)&?.*')
            value = pattern.search(requestline).group('argument')
        except AttributeError:
            pass
        return value

    def do_GET(self):
        crud = CRUD()

        print(self.requestline)
        #urls params
        requestline = self.requestline
        resp = ''

        if (requestline.find("update_terminal")>=0):
            used = self.get(requestline, "used")
            game = self.get(requestline, "game")
            id = self.get(requestline, "id")
            crud.updateTerminal(id,used, game)

        if (requestline.find("post_score")>=0):
            game = self.get(requestline, "game")
            user = self.get(requestline, 'user')
            score = self.get(requestline, 'score')
            resp = (game,user,score)

        if (requestline.find("get_score")>=0):
            game = self.get(requestline, "game")
            resp = crud.getScore(game)

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(json.dumps(resp).encode("utf-8"))

if __name__ == "__main__":
    PORT = 8000
    server = HTTPServer(('', PORT), SQHandler)
    print("starting server on port", PORT)
    server.serve_forever()

