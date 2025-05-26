import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from lib.db.connection import get_connection


from lib.db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO authors (name) VALUES ('Stelar')")
    cursor.execute("INSERT INTO authors (name) VALUES ('Gregory')")
    cursor.execute("INSERT INTO authors (name) VALUES ('Nahum')")

    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Tech Scripts', 'Technology')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Talk Healthy', 'Healthy')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Compositions', 'Literature')")

    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('AI in 2025', 1, 1)")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Herbalists Techniques', 2, 2)")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Composers Block', 1, 3)")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Tech Ethics', 3, 1)")
    

    conn.commit()
    conn.close()
    print("Seed planted successfully")

if __name__ == "__main__":
    seed_data()