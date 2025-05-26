from lib.db.connection import get_connection
@classmethod
def find_by_author_id(cls, author_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
    articles = cursor.fetchall()
    conn.close()
    return [cls(*row) for row in articles]

