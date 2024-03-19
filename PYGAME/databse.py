
import sqlite3

#Create database connection (DB_NAME)
DB_NAME = 'mygame'
con = sqlite3.connect(DB_NAME)

# enable to execute CRUD commands/querys
cur = con.cursor()

#create users table
player_table = '''
    CREATE  TABLE IF NOT EXISTS players (
        id INTEGR PRIMARY KEY,
        fullname TEXT NOT NULL,
        nickname TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        status BOOLEAN DEFAULT true,
        create_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        update_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL

    )
'''
#Execute query 
cur.execute(player_table)

#send changes to database 
con.commit()