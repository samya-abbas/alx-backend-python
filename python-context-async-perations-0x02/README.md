# 📁 python-context-async-perations-0x02

This project focuses on using context managers and asynchronous operations in Python to manage SQLite database interactions safely and efficiently.

## 🧰 Technologies Used
- Python 3.x
- SQLite3
- aiosqlite (for async DB access)
- AsyncIO (concurrency)
- Context managers (`with`, `__enter__`, `__exit__`)

---

## 📄 Task 0: `0-databaseconnection.py` — Class-Based DB Context Manager

### 🎯 Objective:
Create a custom context manager class `DatabaseConnection` that:
- Opens a SQLite connection in `__enter__`
- Closes it automatically in `__exit__`

### ✅ Features:
- Safe handling of DB connections using the `with` statement.
- Prevents forgetting to close connections.

### 💡 Example Usage:
```python
with DatabaseConnection("users.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
````

---

## 📄 Task 1: `1-execute.py` — Reusable Query Context Manager

### 🎯 Objective:

Create a class-based context manager `ExecuteQuery` that:

* Accepts a SQL query and parameters
* Executes it on `__enter__`
* Returns results from the query

### ✅ Features:

* Abstracts connection + execution in one reusable manager
* Query params passed safely via tuple

### 💡 Example Usage:

```python
with ExecuteQuery("users.db", "SELECT * FROM users WHERE age > ?", (25,)) as results:
    print(results)
```

---

## 📄 Task 3: `3-concurrent.py` — Async Queries with `aiosqlite` & `asyncio.gather`

### 🎯 Objective:

Run multiple database queries **concurrently** using:

* `asyncio.gather()`
* `aiosqlite` for async DB operations

### ✅ Features:

* Non-blocking concurrent DB queries
* Uses async context managers

### 💡 Example Usage:

```python
async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

# Run
asyncio.run(fetch_concurrently())
```

---

## ✅ Summary

This directory demonstrates practical and modern Python practices:

* Clean resource management with context managers
* Concurrent DB operations using asyncio
* Real-world examples using SQLite and `aiosqlite`
