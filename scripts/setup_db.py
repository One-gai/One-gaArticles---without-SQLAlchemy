

import sqlite3


conn = sqlite3.connect('articles.db')
cursor = conn.cursor()


with open('lib/db/schema.sql', 'r') as f:
    schema_sql = f.read()


cursor.executescript(schema_sql)
conn.commit()
conn.close()

print("Database setup complete.")
