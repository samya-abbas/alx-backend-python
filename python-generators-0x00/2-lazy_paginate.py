#!/usr/bin/env python3
"""
2-lazy_paginate.py

Simulate lazy loading paginated data from the users table using a generator.
"""

from seed import connect_to_prodev


def paginate_users(page_size, offset):
    """
    Fetch one page of users from the database.
    """
    conn = connect_to_prodev()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def lazy_pagination(page_size):
    """
    Generator that yields pages (lists of user dicts) lazily,
    fetching only when needed. Uses one loop.
    """
    offset = 0
    while True:  # 1️⃣ one loop only
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
