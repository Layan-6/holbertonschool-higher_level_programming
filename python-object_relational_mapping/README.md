# Python - Object-Relational Mapping (ORM)

## Overview
This project demonstrates two approaches to database interaction in Python:
1. **Raw SQL with MySQLdb** - Direct database queries
2. **ORM with SQLAlchemy** - Object-oriented database mapping

##¯ Learning Objectives
- Connect Python applications to MySQL databases
- Execute SQL queries using MySQLdb
- Implement ORM with SQLAlchemy
- Perform CRUD operations (Create, Read, Update, Delete)
- Prevent SQL injection attacks
- Manage database sessions and connections

## Project Structure

### Part 1: MySQLdb (Files 0-5)
Direct SQL execution with parameterized queries for security.

### Part 2: SQLAlchemy (Files 6-14)
Object-Relational Mapping with model classes and sessions.

## File Index

| File | Description |
|------|-------------|
| `0-select_states.py` | Lists all states sorted by ID |
| `1-filter_states.py` | Lists states starting with 'N' |
| `2-my_filter_states.py` | Filters states by user input |
| `3-my_safe_filter_states.py` | Safe parameterized queries |
| `4-cities_by_state.py` | Lists cities with state names |
| `5-filter_cities.py` | Lists cities in a specific state |
| `model_state.py` | State model definition |
| `7-model_state_fetch_all.py` | Lists all states via ORM |
| `8-model_state_fetch_first.py` | Fetches first state |
| `9-model_state_filter_a.py` | Filters states with 'a' |
| `10-model_state_my_get.py` | Gets state by name |
| `11-model_state_insert.py` | Inserts new state |
| `12-model_state_update_id_2.py` | Updates state with ID=2 |
| `13-model_state_delete_a.py` | Deletes states with 'a' |
| `model_city.py` | City model definition |
| `14-model_city_fetch_by_state.py` | Lists cities by state |

## Installation & Setup

### 1. Install MySQL
```bash
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation
