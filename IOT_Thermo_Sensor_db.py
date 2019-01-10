import sqlite3

conn=sqlite3.connect('Accounts.db')
c=conn.cursor()
c.execute('BEGIN TRANSACTION')
c.execute('PRAGMA foreign_keys=ON;')

c.execute('CREATE TABLE Accounts (Id PRIMARY KEY,MailAddress,Password);')
c.execute("INSERT INTO Accounts VALUES(1,'nekusiku01@gmail.com','yuucya210');")

c.execute('CREATE TABLE Projects (Id PRIMARY KEY,AccountId FOREIGN KEY(Id) REFERENCES Accounts(Id),GoogleProjectId,Name)')
c.execute("INSERT INTO Projects VALUES (1,1,1,'IOTThermoSensor')")

c.execute('CREATE TABLE ApiKeys (Id PRIMARY KEY,ProjectId FOREIGN KEY,ApiKey)')
c.execute("INSERT INTO ApiKeys VALUES (1,1,'AIzaSyDJntsUxTlr6nOUTDqOuynw8OyJGw9Tai0')")

c.execute('CREATE TABLE ClientIds (Id PRIMARY KEY,ProjectId FOREIGN KEY,ClientId,ClientSecret)')
c.execute("INSERT INTO ClientIds VALUES (1,1,'1033655159638-fek1o17voj7hfut8hggaffceh1bab4po.apps.googleusercontent.com','TtvNOi4daznlLTjQJho66LwO')")

c.execute('CREATE TABLE RefreshTokens (Id PRIMARY KEY,ClientId FOREIGN KEY,RefreshToken)')
c.execute("INSERT INTO RefreshTokens VALUES (1,'1033655159638-fek1o17voj7hfut8hggaffceh1bab4po.apps.googleusercontent.com','1/FUAfwIr9_ZvjTCiqHX6-BApngOVuaVWylClw80U8Tlc')")

conn.commit()
conn.close()
