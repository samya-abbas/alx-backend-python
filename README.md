# Python Generators Project

This repository contains a series of tasks demonstrating practical uses of Python generators for efficient database access and data processing. The project connects to a MySQL database `ALX_prodev` with a `user_data` table, and showcases streaming, batching, pagination, and aggregation techniques.

---

## Project Overview

Each task builds upon the previous and explores generator functions to:

- Efficiently fetch rows one by one without loading entire datasets into memory
- Process data in batches for scalable operations
- Lazily paginate through data
- Compute aggregate statistics using memory-efficient generators

---

## Tasks

### Task 0: Database Setup and Seeding (`seed.py`)

- Create MySQL database `ALX_prodev`
- Create `user_data` table with columns:
  - `user_id` (UUID, primary key)
  - `name` (VARCHAR, not null)
  - `email` (VARCHAR, not null)
  - `age` (DECIMAL, not null)
- Seed the table with sample data from `user_data.csv`

---

### Task 1: Stream Rows One by One (`0-stream_users.py`)

- Implement `stream_users()` generator function
- Fetch rows from the database one at a time
- Use `yield` to stream user dictionaries lazily

---

### Task 2: Batch Processing (`1-batch_processing.py`)

- Implement `stream_users_in_batches(batch_size)` generator that yields batches of users
- Implement `batch_processing(batch_size)` to filter and process users over age 25
- Demonstrates batching combined with generator-based processing

---

### Task 3: Lazy Pagination (`2-lazy_paginate.py`)

- Implement `paginate_users(page_size, offset)` to fetch fixed-size pages
- Implement `lazy_paginate(page_size)` generator to lazily load pages only when needed
- Simulates paginated API fetching with generators

---

### Task 4: Memory-Efficient Aggregate (`4-stream_ages.py`)

- Implement `stream_user_ages()` generator yielding user ages one by one
- Use generator to compute average age without loading entire dataset into memory
- Avoid SQL aggregation functions; compute average in Python

---

### Task 5: (Add description here if any, or remove if only 5 tasks)

---

## Requirements

- Python 3.x
- MySQL server with database access
- Python packages:
  - `mysql-connector-python` (or `mysqlclient` / `pymysql` as preferred)
- Proper database credentials configured in your environment or config file

---

## Usage

Run each script independently to execute its respective task. Example:

```bash
python3 0-main.py
python3 1-main.py
python3 2-main.py
python3 3-main.py
python3 4-stream_ages.py
