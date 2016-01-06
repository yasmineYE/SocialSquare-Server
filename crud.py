#!/usr/bin/python3
#*-*Coding: UTF-8 *-*
import sqlite3
import json

class CRUD:
    def __init__(self):

        #connection to the db
        self.connection = sqlite3.connect('database.db')
        # cursor
        self.cursor = self.connection.cursor()
        # foreign key constraints
        # specific to sqlite
        self.cursor.execute("pragma foreign_keys = on")


    def getAvailableTerm(self):

        cursor = self.cursor
        request = "SELECT * FROM terminal WHERE used = 'false'"
        cursor.execute(request)
        terminals = cursor.fetchall()
        return terminals

    def updateTerminal(self, id, used, game='NULL'):
        cursor = self.cursor
        connection = self.connection
         if game=='NULL':
            request = "UPDATE terminal "
            request += "SET used ='" + used + "' "
            request += "WHERE id =" + id 
        else:
            request = "UPDATE terminal "
            request += "SET used ='" + used + "', game = "+game
            request += " WHERE id =" + id 
        cursor.execute(request)
        connection.commit()


    def getScore(self, game):

        cursor = self.cursor
        request = "SELECT score, user FROM score "
        request += "WHERE game ='" + game + "' "
        request += "ORDER BY score DESC "
        request += "LIMIT 10;"
        cursor.execute(request)
        scores = cursor.fetchall()
        out  = []
        for score in scores:
            s = {}
            s['score'] = score[0]
            s['username'] = score[1]
            out += [s]

        out = json.dumps(out)
        return out

    def insertScore(self, score, game, user):
        connection = self.connection
        cursor = self.cursor
        request = "INSERT INTO score"
        request += "VALUES (score, game, user)"
        cursor.execute(request)
        connection.commit()


    def getAllUsers(self):

        cursor = self.cursor
        request = "SELECT * FROM user"
        cursor.execute(request)
        user = cursor.fetchall()
        return user

    def getAllGames(self):

        cursor = self.cursor
        request = "SELECT * FROM game"
        cursor.execute(request)
        games = cursor.fetchall()
        return games

    def isTerminalAvailable(self, id):
        """
        check if a terminal is available
        """
        cursor = self.cursor
        cursor.execute("SELECT used WHERE id="+id)
        resp = cursor.fetchone()[0]
        return json.dumps({"id":resp})

    def main(self):
        """
        print self.getAllUsers() #OK
        print self.getAllGames() #OK
        print self.getAvailableTerm() #OK
        print self.getScore("Memory")
        #print self.updateTerminal(2,True)
        """

c=CRUD()
print(c.getScore('TicTacToe'))
