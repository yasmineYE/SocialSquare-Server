#!/usr/bin/python3
#*-*Coding: UTF-8 *-*

import sqlite3

class CRUD:

    def __init__(self):
        #connection to the db
        self.connection = sqlite3.connect('database.db')
        # cursor
        self.cursor = self.connection.cursor()
        # foreign key constraints
        # specific to sqlite
        self.cursor.execute("pragma foreign_keys = on")

    def getAvailableTerms(self):
        cursor = self.cursor
        request = "SELECT id FROM terminal WHERE used='0'"
        cursor.execute(request)
        terminals = cursor.fetchall()
        return list(map(lambda t: t[0], terminals))

    def updateTerminal(self, id, used, game='NULL'):
        cursor = self.cursor
        connection = self.connection
        if game == 'NULL':
            game = None
        request = "UPDATE terminal SET used=?, game=? WHERE id=?"
        cursor.execute(request, (used, game, id))
        connection.commit()
        return 1

    def getScore(self, game):
        cursor = self.cursor
        request = "SELECT score, user FROM score "
        request += "WHERE game ='" + game + "' "
        request += "ORDER BY score DESC "
        cursor.execute(request)
        scores = cursor.fetchall()
        out  = []
        for score in scores:
            s = {}
            s['score'] = score[0]
            s['username'] = score[1]
            out.append(s)
        return out

    def insertScore(self, score, game, user):
        connection = self.connection
        cursor = self.cursor
        if not user in self.getAllUsers():
            request = "INSERT INTO user VALUES (?)"
            cursor.execute(request, (user,))
        request = "INSERT INTO score"
        request += " VALUES (?, ?, ?)"
        cursor.execute(request, (score, game, user))
        connection.commit()
        return 1

    def getAllUsers(self):
        cursor = self.cursor
        request = "SELECT * FROM user"
        cursor.execute(request)
        users = cursor.fetchall()
        return list(map(lambda u: u[0], users))

    def getAllGames(self):
        cursor = self.cursor
        request = "SELECT * FROM game"
        cursor.execute(request)
        games = cursor.fetchall()
        return list(map(lambda g: g[0], games))

    def isTerminalAvailable(self, id):
        """
        check if a terminal is available
        """
        cursor = self.cursor
        cursor.execute("SELECT used FROM terminal WHERE id=?", (id,))
        available = cursor.fetchone() == (1,)
        return available

