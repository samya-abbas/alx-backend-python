#!/usr/bin/env python3
"""
seed.py ― utilities to create / seed the ALX_prodev database.

Functions
---------
connect_db() -> connection
    Connect to the MySQL server (no database selected).

create_database(conn)
    Create database ALX_prodev if it does not exist.

connect_to_prodev() -> connection
    Connect **specifically** to the ALX_prodev database.

create_table(conn)
    Create table user_data (id, name, email, age) with correct types.

insert_data(conn, csv_path)
    Insert rows from csv_path if they are not already present.
"""

import csv
import uuid
import mysql.connector
from mysql.connector import errorcode
from pathlib import Path

# ----------------------- connection helpers ----------------------- #
def _mysql_credentials() -> dict:
    """
    Central place to tweak how you connect to MySQL.
    By default, it relies on localhost + env vars or defaults.
    """
    import os
    return {
        "host":     os.getenv("MYSQL_HOST", "127.0.0.1"),
        "port":     int(os.getenv("MYSQL_PORT", 3306)),
        "user":     os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", ""),
    }


def connect_db():
    """Return a server‑level connection (no DB selected)."""
    try:
        return mysql.connector.connect(**_mysql_credentials())
    except mysql.connector.Error as err:
        print(f"❌  MySQL connection error: {err}")
        return None


def connect_to_prodev():
    """Return a connection to the ALX_prodev database."""
    try:
        creds = _mysql_credentials() | {"database": "ALX_prodev"}
        return mysql.connector.connect(**creds)
    except mysql.connector.Error as err:
        print(f"❌  Cannot connect to ALX_prodev: {err}")
        return None


# ---------------------------- DDL --------------------------------- #
CREATE_DB_SQL = "CREATE DATABASE IF NOT EXISTS ALX_prodev CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS user_data (
    user_id CHAR(36)          NOT NULL PRIMARY KEY,
    name    VARCHAR(255)      NOT NULL,
    email   VARCHAR(255)      NOT NULL,
    age     DECIMAL(5,0)      NOT NULL,
    KEY user_id_idx (user_id)
) ENGINE=InnoDB;
"""


def create_database(connection):
    """Create ALX_prodev schema if it does not exist."""
    cursor = connection.cursor()
    cursor.execute(CREATE_DB_SQL)
    connection.commit()
    cursor.close()


def create_table(connection):
    """Create user_data table with the required columns."""
    cursor = connection.cursor()
    cursor.execute(CREATE_TABLE_SQL)
    connection.commit()
    cursor.close()
    print("Table user_data ready ✅")


# ---------------------------- DML --------------------------------- #
def _row_exists(cursor, user_id: str) -> bool:
    """Return True if a row with user_id already exists."""
    cursor.execute("SELECT 1 FROM user_data WHERE user_id=%s LIMIT 1;", (user_id,))
    return cursor.fetchone() is not None


def insert_data(connection, csv_path: str | Path):
    """
    Insert CSV rows (user_id, name, email, age) into user_data.
    Skips rows whose user_id already exists.
    """
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(csv_path)

    inserted, skipped = 0, 0
    cursor = connection.cursor()

    with csv_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            uid = row.get("user_id") or str(uuid.uuid4())
            if _row_exists(cursor, uid):
                skipped += 1
                continue
            cursor.execute(
                "INSERT INTO user_data (user_id, name, email, age) VALUES (%s,%s,%s,%s);",
                (uid, row["name"], row["email"], row["age"]),
            )
            inserted += 1

    connection.commit()
    cursor.close()
    print(f"Inserted {inserted} rows, skipped {skipped} duplicates.")


# --------------- run as standalone utility ----------------------- #
if __name__ == "__main__":
    # Allow:  python seed.py  -> full setup + insert sample data
    root_conn = connect_db()
    if not root_conn:
        exit(1)

    create_database(root_conn)
    root_conn.close()
    print("✅ Database ensured.")

    db_conn = connect_to_prodev()
    if not db_conn:
        exit(1)

    create_table(db_conn)
    try:
        insert_data(db_conn, "user_data.csv")
    except FileNotFoundError:
        print("⚠️  user_data.csv not found – skipping seed insert.")
    db_conn.close()
