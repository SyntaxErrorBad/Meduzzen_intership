import psycopg2
 
conn = psycopg2.connect(dbname="postgres", user="admin", password="123456",host="postgres")
cursor = conn.cursor()
 
conn.autocommit = True

cursor.execute("CREATE DATABASE users")
print("База данных успешно создана")

cursor.execute("CREATE TABLE people (id SERIAL PRIMARY KEY, name VARCHAR(50),  age INTEGER)")
conn.commit()
 
cursor.close()
conn.close()