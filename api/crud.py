def search_prononciation(db, pron):
    cur = db.execute(
        "SELECT mot, pron FROM prononciations WHERE pron LIKE ?",
        (f"%{pron}%",)
    )
    return cur.fetchall()
