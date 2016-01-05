#!/usr/bin/python3
#*-*Coding: UTF-8 *-*
import sqlite3

class CRUD:
    def __init__(self):

        #connection to the db
        self.connection = sqlite3.connect('database.db')

        # cursor
        self.cursor = sqlite3.cursor()

    def getAvalaibleTerm(self):
        """
        return all available terminals
        """
        cursor = self.cursor
        cursor.execute("SELECT * FROM terminal WHERE used = false")
        terminals = cursor.fetchall()
        return terminals
