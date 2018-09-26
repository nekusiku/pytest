import sqlite3
conn = sqlite3.connect('Google.Acounts.sqlite3')

c = conn.cursor()

c.execute('PRAGMA foreign_keys = ON;')#外部キー設定


c.execute('CREATE TABLE Account(id interger primary_key,address,password);')

c.execute('CREATE TABLE Project(id interger primary_key,AccountId interger foreign_key,GoogleProjectId,Name);')

c.execute('CREATE TABLE ApiKeys(id primary_key,ProjectId foreign_key,Apikey);')

c.execute('CREATE TABLE ClientIds(Id primary_key,ProjectId foreign_key,ClientId,ClientSecret);')

c.execute('CREATE TABLE RefreshTokens(Id primary_key,ClientId foreign_key,RefreshToken);')



c.execute('INSERT into Account(id,address,password) VALUES(null,"huga","hhogehoge");')

c.execute('INSERT into Project(id,AccountId,GoogleProjectId,Name) VALUES(null,0,0,"hugahuga");')

c.execute('INSERT into ApiKeys(id,ProjectId,ApiKey) VALUES(null,0,"AIzaSyDJntsUxTlr6nOUTDqOuynw8OyJGw9Tai0");')

c.execute('INSERT into ClientIds(Id,ProjectId,ClientID,ClientSecret) VALUES(null,"1","1033655159638-fek1o17voj7hfut8hggaffceh1bab4po.apps.googleusercontent.com","TtvNOi4daznlLTjQJho66LwO");')

c.execute('INSERT into RefreshTokens(Id,ClientId,RefreshToken) VALUES(null,"1033655159638-fek1o17voj7hfut8hggaffceh1bab4po.apps.googleusercontent.com","1/FUAfwIr9_ZvjTCiqHX6-BApngOVuaVWylClw80U8Tlc");')

conn.commit()

conn.close()