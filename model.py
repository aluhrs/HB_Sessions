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
    if row == None:
        return None
    else:
        return row[0]

def get_user_by_name(username):
    query = """SELECT id FROM users WHERE username = ?"""
    DB.execute(query, (username,))
    row = DB.fetchone()
    return row[0]

def get_wallposts_by_userid(userid):
    query = """SELECT owner_id, author_id, created_at, content FROM wall_posts AS w 
                JOIN users AS u ON owner_id = u.id 
                WHERE u.id = ?"""
    DB.execute(query, (userid,))
    row = DB.fetchall()
    return row
    

def get_author_name_by_author_id(author_id):
    query = """SELECT username FROM users JOIN wall_posts ON author_id = user.id
             WHERE author_id = ?"""
    DB.execute(query, (author_id,))
    row = DB.fetchone()
    print "This is the author_name %r" % row
    return row
