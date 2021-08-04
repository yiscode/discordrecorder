__create database using sqlite3__

```
import sqlite3
conn = sqlite3.connect("trpgsetting.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTs Background_story (id INTEGER PRIMARY KEY, context TEXT)")
cursor.execute("INSERT INTO Background_story VALUES (null,\"test\")")
cursor.execute("SELECT context FROM Background_story")
print(cursor.fetchall())

```
null let table auto create primary key.
cursor.fetchall() is list

__delete table__
```
cursor.execute("DROP TABLE Background_story")

```
__permanently change__
```
conn.commit()
```
__end this connection__
```
cursor.close()
conn.close()
```