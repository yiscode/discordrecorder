import sqlite3

conn = sqlite3.connect("trpgsetting.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE Background_story")
conn.commit()
cursor.execute("CREATE TABLE IF NOT EXISTs Background_story (id INTEGER PRIMARY KEY, context TEXT)")
conn.commit()
cursor.close()
conn.close()

