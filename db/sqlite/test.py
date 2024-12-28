import sqlite3
import json

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

#cur.execute("CREATE TABLE movie(title, year, score)")

#cur.execute("""
#    INSERT INTO movie VALUES
#        ('Monty Python and the Holy Grail', 1975, 8.2),
#        ('And Now for Something Completely Different', 1971, 7.5)
#""")

result = cur.execute("SELECT * FROM movie")
rows = cur.fetchall()
columns = [col[0] for col in cur.description]
data = [dict(zip(columns, row)) for row in rows]
to_json = json.dumps(data, indent=2)

print (to_json)

cur.close()
con.close()