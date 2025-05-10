import sqlite3
from models.post import Post  

def create_post(user_id, category_id, title, publication_date, image_url, content, approved):
    """Adds a new post to the database when a user creates a post

    Args:
        Post (dictionary): Post object containing the post's details

    """
    with sqlite3.connect('./db.sqlite3') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Posts (user_id, category_id, title, publication_date, image_url, content, approved)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, category_id, title, publication_date, image_url, content, int(approved)))
        conn.commit()

def get_all_posts():
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Posts')
        rows = cursor.fetchall()
        return [Post(**dict(row)) for row in rows]
    
def update_post(post_id, user_id, category_id, title, publication_date, image_url, content, approved):
    with sqlite3.connect('./db.sqlite3') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Posts
            SET user_id = ?, category_id = ?, title = ?, publication_date = ?, image_url = ?, content = ?, approved = ?
            WHERE id = ?
        ''', (user_id, category_id, title, publication_date, image_url, content, int(approved), post_id))
        conn.commit()
        
def delete_post(post_id): 
    with sqlite3.connect('./db.sqlite3') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Posts WHERE id = ?', (post_id,))
        conn.commit()   

