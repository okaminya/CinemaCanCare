import random
import sqlite3

conn


class Client:
    def __init__(self, hall, row, place):
        self.hall = hall
        self.row = row
        self.place = place
