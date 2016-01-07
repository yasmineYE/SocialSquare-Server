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
        # handle GET requests
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
            crud.insertScore(score, game, user)

        if (requestline.find("get_score")>=0):
            game = self.get(requestline, "game")
            resp = crud.getScore(game)

        if (requestline.find("get_terminal")>=0):
            #check if a terminal is available
            terminal_id = self.get(requestline,'id')
            resp = crud.isTerminalAvailable(terminal_id)

        if(requestline.find("get_games")>=0):
            resp = crud.getAllGames()

        if(requestline.find("get_users")>=0):
            #get all users
            resp = crud.getAllUsers()

        #header
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        #response data
        print(resp)
        self.wfile.write(json.dumps(resp).encode("utf-8"))

if __name__ == "__main__":
    PORT = 8000
    server = HTTPServer(('', PORT), SQHandler)
    print("starting server on port", PORT)
    server.serve_forever()
