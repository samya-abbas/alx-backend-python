import sqlite3
import functools

# Decorator to manage DB connection automatically
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')  # Open DB connection
        try:
            # Pass the connection as the first argument
            return func(conn, *args, **kwargs)
        finally:
            conn.close()  # Always close the connection
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# fetch user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)
