import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables (optional)

def stream_users_in_batches(batch_size):
    """
    Generator that fetches users in batches from the database.
    """
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database="ALX_prodev"
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) FROM user_data")
    total_rows = cursor.fetchone()['COUNT(*)']

    for offset in range(0, total_rows, batch_size):
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        batch = cursor.fetchall()
        yield batch

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    Processes batches and filters users over the age of 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
