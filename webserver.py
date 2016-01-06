#!/usr/bin/python3
#*-*Coding: UTF-8 *-*

from http.server import BaseHTTPRequestHandler, HTTPServer
import re
import json
from crud import CRUD

class SQHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        crud = CRUD()

        print(self.requestline)
        #urls params
        requestline = self.requestline

        if (requestline.find("update_terminal")>=0):
            pattern = re.compile(r".*used=(?P<used>.*)&game=(?P<game>.*)&id=(?P<id>.*)\s+.*")
            results = pattern.search(requestline)
            used = results.group('used') == 'true'
            game = results.group('game')
            id = results.group('id')
            resp = crud.updateTerminal(id, used, game)

        if (requestline.find("post_score")>=0):
            pattern = re.compile(r".*game=(?P<game>.*)&user=(?P<user>.*)&score=(?P<score>.*)\s+.*")
            results = pattern.search(requestline)
            game = results.group('game')
            user = results.group('user')
            score = results.group('score')
            resp = crud.insertScore(score, game, user)

        if (requestline.find("get_score")>=0):
            pattern = re.compile(r".*game=(?P<game>.*)\s+.*")
            results = pattern.search(requestline)
            game = results.group('game')
            resp = crud.getScore(game)

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(json.dumps(resp).encode("utf-8"))

    def stop(self):
        self.server.shutdown()

if __name__ == "__main__":
    PORT = 8000
    server = HTTPServer(('', PORT), SQHandler)
    print("starting server on port", PORT)
    server.serve_forever()

