from doforstring import convertinteger as con
import sqlite3
import re
def howdolist(message):
  if 'show' in message.content:
    
    return showoneormore(message)
  elif 'add' in message.content:
    addlist(message)
    return 'successfully add'
def showoneormore(message):
  if 'all' in message.content:
    conn = sqlite3.connect("trpgsetting.db")
    cursor = conn.cursor()
    cursor.execute("SELECT context FROM Background_story")
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    
    
    return con(data)
def addlist(message):
  conn = sqlite3.connect("trpgsetting.db")
  cursor = conn.cursor()
  line = re.sub('List','',message.content,1)
  line = re.sub('add','',line,1)
  cursor.execute("INSERT INTO Background_story VALUES (null,?)",(line,))
  conn.commit()
  cursor.close()
  conn.close()

  
  
  


