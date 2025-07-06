#!/usr/bin/env python3
"""
4-stream_ages.py

Computes average age using a generator in a memory-efficient way.
"""

from seed import connect_to_prodev


def stream_user_ages():
    """
    Generator that yields one age at a time from the user_data table.
    """
    conn = connect_to_prodev()
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row[0]
    cursor.close()
    conn.close()


def compute_average_age():
    """
    Computes average age from generator output.
    """
    total = 0
    count = 0
    for age in stream_user_ages():  # 1️⃣ loop
        total += age
        count += 1

    if count > 0:
        avg = total / count
        print(f"Average age of users: {avg:.2f}")
    else:
        print("No users found.")


if __name__ == "__main__":
    compute_average_age()  # 2️⃣ loop (implicit function call, still within limit)
