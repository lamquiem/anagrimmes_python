import sqlite3

def init_db(db_path="anagrimes.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS prononciations (mot TEXT PRIMARY KEY, pron TEXT);""")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized")
