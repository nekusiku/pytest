from apiclient.discovery import build

api_key = 'AIzaSyDJntsUxTlr6nOUTDqOuynw8OyJGw9Tai0'
service = build('fusiontables', 'v2', developerKey=api_key)

tableid = '1MNHaJ5Y9GbvSjAzXgI7_ww2sszbYIc88O2MYdewH'
rows = service.query().sql(sql="INSERT INTO %s (Timestamp, CpuTemperature) values('%s',%s)" % (tableid,'2001-02-03 04:05:06',45678)).execute()