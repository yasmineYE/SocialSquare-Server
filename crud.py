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
        self.cursor.execute("pragma foreign keys = on")

    def getAvailableTerm(self):
        """
        return all available terminals
        """
        cursor = self.cursor
        cursor.execute("SELECT * FROM terminal WHERE used = 'false'")
        terminals = cursor.fetchall()
        return terminals

    def getScore(self, game, user):
        """
        return all available terminals
        """
        cursor = self.cursor
        request = "SELECT score FROM score"
        request += "WHERE game='game' AND user = 'user'"
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
        print self.getAllUsers()

c=CRUD()
c.main()
