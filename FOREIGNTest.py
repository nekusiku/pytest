import sqlite3

conn=sqlite3.connect('Foreign.db')
c=conn.cursor()
c.execute('BEGIN TRANSACTION')
#c.execute('PRAGMA foreign_keys=ON;')

c.execute('CREATE TABLE idmaster (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)');
c.execute("INSERT INTO idmaster VALUES (null, 'A')");
c.execute("INSERT INTO idmaster VALUES (null, 'B')");

c.execute('CREATE TABLE address (id INTEGER, address TEXT, FOREIGN KEY(id) REFERENCES idmaster(id))');
c.execute("INSERT INTO address VALUES (1, 'addressA')");
c.execute("INSERT INTO address VALUES (2, 'addressB')");
c.execute("INSERT INTO address VALUES (3, 'addressC')");
conn.commit()
