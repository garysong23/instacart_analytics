import sqlite3
conn = sqlite3.connect('applicants.sqlite3')

print('Database opened')

MAIN_QUERY = ('''
  SELECT
    first_name
  FROM applicants
  LIMIT 10
''')

cursor = conn.execute(MAIN_QUERY)
for row in cursor:
  print(row[0])

conn.close()
