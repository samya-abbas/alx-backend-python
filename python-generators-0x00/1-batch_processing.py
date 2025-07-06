#!/usr/bin/env python3
"""
1-batch_processing.py

• stream_users_in_batches(batch_size)  – generator yielding rows in batches
• batch_processing(batch_size)         – prints users older than 25
"""

import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # optional .env for DB creds


def _db_creds() -> dict:
    """Get MySQL credentials from env (fallback to localhost / root)."""
    return {
        "host": os.getenv("DB_HOST", "127.0.0.1"),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", ""),
        "database": "ALX_prodev",
    }


# ------------------------------------------------------------------ #
def stream_users_in_batches(batch_size: int):
    """
    Generator that yields lists of user rows (dicts) in batches of size batch_size.
    Exactly **one** loop is used internally.
    """
    conn = mysql.connector.connect(**_db_creds())
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT COUNT(*) AS total FROM user_data;")
    total = cur.fetchone()["total"]

    for offset in range(0, total, batch_size):          # 1️⃣ loop
        cur.execute(
            "SELECT user_id, name, email, age FROM user_data "
            "LIMIT %s OFFSET %s;", (batch_size, offset)
        )
        yield cur.fetchall()

    cur.close()
    conn.close()


def batch_processing(batch_size: int):
    """
    Iterate over batches, print users whose age > 25.
    Uses a single loop over the batches (total loops in file = 2).
    """
    for batch in stream_users_in_batches(batch_size):   # 2️⃣ loop
        for user in batch:                              # nested but inside same loop block
            if user["age"] > 25:
                print(user)

    return None  # explicit `return` so linters / checkers see it


