import sqlite3
conn = sqlite3.connect('sample_sql.db')

c = conn.cursor()

#c.execute('''CREATE TABLE  sample_table(id primary key,address,passwaord)''')

c.execute("INSERT into sample_table VALUES('','hoge_huga','hogehoge')")