import sqlite3

MAIN_QUERY = ('''
  SELECT
    count(*) as count
    , date(created_at,'-7 days', 'weekday 1') as week
    , workflow_state as workflow_state
  FROM applicants
  GROUP BY strftime('%W', created_at), workflow_state
  ORDER BY week ASC
''')

def main():
  db = sqlite3.connect('applicants.sqlite3')
  print('Database opened')

  cursor = db.execute(MAIN_QUERY)

  with open('output.txt','w+') as f:
    names = list(map(lambda d: str(d[0]), cursor.description))
    name_str = ', '.join(names) + '\n'
    f.write(name_str)
    for row in cursor:
      row_str = ', '.join([str(i) for i in row]) + '\n'
      f.write(row_str)

  print('Database closed')
  db.close()

if __name__ == '__main__':
	main()
