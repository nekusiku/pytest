import sqlite3
conn = sqlite3.connect('sample_sql.db')

c = conn.cursor()

c.execute('PRAGMA foreign_keys = ON;')

#c.execute('CREATE TABLE  Acount(id primary_key,address,password);')

c.execute('INSERT into Acount(id,address,password) VALUES("","hoge_huga","hogehoge");')

conn.commit()

conn.close()