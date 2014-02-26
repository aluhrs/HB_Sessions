import sqlite3

# ADMIN_USER="hackbright"
# ADMIN_PASSWORD=5980025637247534551
#TODO - right now CONN and DB are global variables. 
# It is better practice to have these function calls inside a function that is
# called from authenticate.
CONN = sqlite3.connect("thewall.db")
DB = CONN.cursor()

def authenticate(username, password):
    query = """SELECT username, password FROM users WHERE username = ? 
                and password = ?"""
    DB.execute(query, (username, hash(password)))            
    row = DB.fetchone()
    if username == row[0] and hash(password) == row[1]:
        return username
    else:
        return None
