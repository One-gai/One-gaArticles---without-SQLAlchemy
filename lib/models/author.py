from lib.db.connection import get_connection
from lib.models.articles import Article

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        authors = []
        for row in cursor.execute("SELECT * FROM authors"):
            authors.append(cls(row[0], row[1]))
        conn.close()
        return authors

    def articles(self):
        return Article.find_by_author_id(self.id)
