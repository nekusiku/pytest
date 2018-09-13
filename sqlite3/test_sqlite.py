#pythonでsqliteの操作をする。
import sqlite3

conn = sqlite3.connect("Test_List.sqlite")

cur=conn.cursor()

#conn.execute("create table Test_Table(num, location)")
test = 114514
#conn.execute("insert into Test_Table values("+str(test)+", 'hamamatu')")

cur.execute("select * from TempTest")

for row in cur:
    print(str(row[0]) + "," + row[1])

conn.commit()
