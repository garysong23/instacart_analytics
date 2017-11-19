import sys
import sqlite3
import datetime

def build_query(begin_date, end_date):
  query = ('''
    SELECT
      count(*) as count
      , date(created_at,'-7 days', 'weekday 1') as week
      , workflow_state as workflow_state
    FROM applicants
    WHERE (
      created_at > '{}'
      AND created_at < '{}'
    )
    GROUP BY strftime('%W', created_at), workflow_state
    ORDER BY week ASC
  ''').format(begin_date, end_date)
  return query

def excute_query(query):
  db = sqlite3.connect('applicants.sqlite3')
  cursor = db.execute(query)

  with open('output.txt','w+') as f:
    names = list(map(lambda d: str(d[0]), cursor.description))
    name_str = ', '.join(names) + '\n'
    f.write(name_str)
    for row in cursor:
      row_str = ', '.join([str(i) for i in row]) + '\n'
      f.write(row_str)

  db.close()

def main():
  if (len(sys.argv) != 3):
    print('Invalid arguments')
    return

  begin_time_str = sys.argv[1]
  end_time_str = sys.argv[2]

  begin_date = datetime.datetime.strptime(begin_time_str, '%Y-%m-%d')
  end_date = datetime.datetime.strptime(end_time_str, '%Y-%m-%d')

  query = build_query(begin_date, end_date)
  excute_query(query)

if __name__ == '__main__':
	main()
