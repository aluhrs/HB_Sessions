#import sqlite3

ADMIN_USER="hackbright"
ADMIN_PASSWORD=5980025637247534551

def authenticate(username, password):
    # CONN = sqlite3.connect("thewall.db")
    # DB = CONN.cursor()
    # query = """SELECT username, password FROM users WHERE username = ? 
    #             and password = ?"""
    # row = DB.execute(query, (username, hash(password)))            
    if username == ADMIN_USER and hash(password) == ADMIN_PASSWORD:
        return ADMIN_USER
    else:
        return None
