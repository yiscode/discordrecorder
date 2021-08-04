def convertinteger(tuple):
  tlist=list(tuple)
  
  changelist=[str(i).replace("'","").replace("'","").replace("(","").replace(")","").lstrip().replace(",","") for i in tlist]
  
  listostring = "\n".join(changelist)
  return listostring