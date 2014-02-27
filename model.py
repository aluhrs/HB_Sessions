import sqlite3

# ADMIN_USER="hackbright"
# ADMIN_PASSWORD=5980025637247534551
#TODO - right now CONN and DB are global variables. 
# It is better practice to have these function calls inside a function that is
# called from authenticate.
CONN = None
DB = None

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("thewall.db")
    DB = CONN.cursor()

def authenticate(username, password):
    query = """SELECT id FROM users WHERE username = ? 
                and password = ?"""
    DB.execute(query, (username, hash(password)))            
    row = DB.fetchone()
    print row
    if row == None:
        return None
    else:
        return row[0]

def get_user_by_name(username):
    pass