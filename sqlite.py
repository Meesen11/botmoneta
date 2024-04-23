import sqlite3 as sq



async def db_start():
    global db, cur
    
    db = sq.connect('tgbot_db')
    cur = db.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, count TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS profile2(user_id TEXT PRIMARY KEY, count TEXT)")
    db.commit
    
    