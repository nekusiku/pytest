import sqlite3
conn = sqlite3.connect('Google.Acounts.sqlite3')

c = conn.cursor()

c.execute('PRAGMA foreign_keys = ON;')

c.execute('CREATE TABLE  Acount(id primary_key,address,password);')

c.execute('CREATE TABLE Project(id primary_key,AccountId foreign_key,GoogleProjectId,Name);')

c.execute('CREATE TABLE ApiKeys(id primary_key,ProjectId foreign_key,Apikey);')

c.execute('CREATE TABLE ClientIds(Id primary_key,ProjectId foreign_key,ClientId,ClientSecret);')

c.execute('CREATE TABLE RefreshTokens(Id primary_key,ClientId foreign_key,RefreshToken);')

c.execute('INSERT into Acount(id,address,password) VALUES("","","");')