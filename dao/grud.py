import sqlite3


def init_db():
    global connection, cursor
    # Connect to SQLite database (or create it if it doesn't exist)
    connection = sqlite3.connect("dialogues.db")
    # Create a cursor object to interact with the database
    cursor = connection.cursor()
    # Create a table
    cursor.execute("""
       CREATE TABLE IF NOT EXISTS dialogue (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           question TEXT NOT NULL,
           answer TEXT NOT NULL
       )
       """)
    return


def close_db():
    connection.commit()
    cursor.close()
    connection.close()


def get_answer_by_question(question):
    sql = f"SELECT `answer` FROM dialogue where question like '%{question}%'  or answer like '%{question}%'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows
