# 🗄️ Python Generators ‑ Task 1/5  
## MySQL Seeder & Row‑Streaming Generator

This task bootstraps a MySQL schema **ALX_prodev** with a `user_data` table, seeds it from **`user_data.csv`**, and exposes helper functions for downstream generator tasks.

---

### 📑 Table of Contents
1. [Project Goals](#project-goals)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
4. [Environment Variables](#environment-variables)  
5. [Usage](#usage)  
6. [Project Structure](#project-structure)  
7. [Key Functions](#key-functions)  
8. [Sample Output](#sample-output)  
9. [Troubleshooting](#troubleshooting)  
10. [Author](#author)  

---

## Project Goals
| Goal | Description |
|------|-------------|
| **DB bootstrap** | Create `ALX_prodev` schema and `user_data` table with proper types. |
| **Seeding** | Load rows from `user_data.csv`, skipping duplicates. |
| **Reusable helpers** | Provide `connect_db`, `create_database`, `connect_to_prodev`, `create_table`, `insert_data`. |
| **Foundation for streaming** | Later tasks will stream these rows via Python generators. |

---

## Prerequisites
- **Python 3.9+**  
- MySQL server (local or remote)  
- `mysqlclient` or `mysql‑connector‑python`  
  ```bash
  pip install mysqlclient
  # or
  pip install mysql-connector-python
  ```

---

## Installation

```bash
# Clone the repo
git clone https://github.com/<your‑user>/alx-backend-python.git
cd alx-backend-python/python-generators-0x00

# (Optional) activate a virtualenv
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

# Install requirements if you have a requirements.txt
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` (or export in your shell) to avoid hard‑coding credentials:

```env
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
```

`seed.py` reads these via `os.getenv(...)` with sensible defaults (`root@localhost` and no password).

---

## Usage

Run the provided test‑driver:

```bash
python 0-main.py
```

Typical output:

```
connection successful
Table user_data ready ✅
Database ALX_prodev is present
[('5527a424-...', 'Jane Doe', 'jane@example.com', 29), ...]
```

You can also run the seeder standalone:

```bash
python seed.py          # Creates DB, table, inserts CSV rows
```

---

## Project Structure

```
python-generators-0x00/
├── seed.py           # DB helpers + CSV importer
├── 0-main.py         # Task checker / demo script
├── user_data.csv     # 10 000 sample rows (UUID,name,email,age)
└── README.md
```

---

## Key Functions (seed.py)

| Prototype | Purpose |
|-----------|---------|
| `connect_db()` | Connects to the MySQL server (no schema). |
| `create_database(conn)` | Creates **ALX_prodev** if absent. |
| `connect_to_prodev()` | Connects directly to ALX_prodev. |
| `create_table(conn)` | Creates `user_data` table with UUID PK, indexed. |
| `insert_data(conn, csv_path)` | Bulk‑inserts CSV rows, skipping existing IDs. |

---

## Sample Output

```bash
$ python 0-main.py
connection successful
Table user_data ready ✅
Database ALX_prodev is present
[('00234e50-34eb-4ce2-94ec-26e3fa749796', 'Dan Altenwerth Jr.', 'Molly59@gmail.com', 67),
 ('006bfede-724d-4cdd-a2a6-59700f40d0da', 'Glenda Wisozk', 'Miriam21@gmail.com', 119),
 ...]
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError: No module named 'mysql'` | `pip install mysqlclient` or `mysql-connector-python`. |
| `Access denied for user` | Check `MYSQL_USER`/`MYSQL_PASSWORD` in your environment. |
| CSV not found | Ensure `user_data.csv` is in the same directory or pass an absolute path. |
| Duplicate key errors | `insert_data` skips duplicates; ensure UUIDs are truly unique. |

---

## Author
**Samya Abbas**  
ALX SE Student  
[GitHub](https://github.com/samya-abbas)

---

> **Next Tasks** will build generators that stream this data one row at a time and demonstrate memory‑efficient processing 🔄