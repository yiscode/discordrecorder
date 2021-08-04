import sqlite3
from doforstring import convertinteger
conn = sqlite3.connect("trpgsetting.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Background_story (id INTEGER PRIMARY KEY, context TEXT)")
line="i hava a cat"
cursor.execute("INSERT INTO Background_story VALUES (null,?)",(line,))
cursor.execute("INSERT INTO Background_story VALUES (null,\"test3\")")

cursor.execute("SELECT context FROM Background_story")
data=cursor.fetchall()
print(convertinteger(data))
cursor.close()
conn.close()