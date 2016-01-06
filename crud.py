#!/usr/bin/python3
#*-*Coding: UTF-8 *-*
import sqlite3

class CRUD:
    def __init__(self):

        #connection to the db
        self.connection = sqlite3.connect('database.db')
        # cursor
        self.cursor = self.connection.cursor()

    def getAvalaibleTerm(self):
        """
        return all available terminals
        """
        cursor = self.cursor
        request = "SELECT * FROM terminal WHERE used = 'false'"
        cursor.execute(request)
        terminals = cursor.fetchall()
        return terminals

    def updateTerminal(self, id, used):
        cursor = self.cursor
        request = "UPDATE terminal "
        request += "SET used='used'"
        request += "WHERE id='id' "
        cursor.execute(request)
        terminals = cursor.fetchall()
        return terminals

    def getScore(self, game):
        """
        return all scores for a specific game by descending order
        """
        cursor = self.cursor
        request = "SELECT score FROM score"
        request += "WHERE game='game'"
        request += "ORDER BY score DESC"
        cursor.execute(request)
        terminals = cursor.fetchall()
        return terminals

    def insertScore(self, score, game, user):
        """
        Insert (score,game,user) into the table score
        """
        cursor = self.cursor
        request = "INSERT INTO score"
        request += "VALUES ('score', 'game', 'user')"
        cursor.execute(request)
        terminals = cursor.fetchall()
        return terminals

    def getAllUsers(self):
        """
        return all available terminals
        """
        cursor = self.cursor
        request = "SELECT * FROM users"
        cursor.execute(request)
        terminals = cursor.fetchall()
        return terminals

    def getAllGames(self):
        """
        return all available terminals
        """
        cursor = self.cursor
        request = "SELECT * FROM game"
        cursor.execute(request)
        terminals = cursor.fetchall()
        return terminals

    def main(self):
        print self.getAllUsers() #OK
        print self.getAllGames() #OK
        print self.getAvalaibleTerm() #OK
        #print self.getScore('TIC TAC TOE')
        #print self.updateTerminal(2,True)

c=CRUD()
c.main()
