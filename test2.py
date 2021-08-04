import re
import sqlite3
conn = sqlite3.connect("trpgsetting.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Test (id INTEGER PRIMARY KEY, context TEXT)")
line="List add i hava a cat"
line = re.sub('List','',line)
line = re.sub('add','',line)
print(line)
cursor.execute("INSERT INTO Background_story VALUES (null,?)",(line,))


cursor.execute("SELECT context FROM Background_story")
data=cursor.fetchall()
cursor.close()
print(data)

