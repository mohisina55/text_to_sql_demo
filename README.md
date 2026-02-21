# text_to_sql_demo

An AI-powered Text-to-SQL application that converts natural language questions into SQL queries and retrieves data from a SQLite database.

This project demonstrates how Large Language Models (Google Gemini) can be integrated with structured databases to build intelligent query systems.

---

## 🚀 Tech Stack

- 🐍 Python
- 📊 SQLite
- 🤖 Google Gemini API
- 🎨 Streamlit
- 🔐 python-dotenv

---

## 📌 Project Overview

This application allows users to:

1. Enter a natural language question.
2. Convert it into a SQL query using Gemini.
3. Execute the SQL query on a local SQLite database.
4. Display the results interactively in a web interface.

Example:

**User Question:**
What is the average marks of students in class 10th section A?

**Generated SQL:**
```sql
SELECT AVG(marks) FROM students WHERE class='10th' AND section='A';
```
**Project Strcuture**
```Text-to-SQL/
│
├── venv/
├── .env
├── app.py
├── sql.py
├── my_database.db
├── requirements.txt
└── README.md
```
## 🗄️ Database Details

**Database Name:** `my_database.db`  
**Table Name:** `students`

---

### 📌 Table Structure

| Column  | Type     |
|----------|----------|
| Name     | varchar  |
| class    | varchar  |
| section  | varchar  |
| marks    | int      |

---

### 📊 Sample Data Inserted

| Name            | Class | Section | Marks |
|-----------------|--------|----------|--------|
| John Doe        | 10th   | A        | 85     |
| Jane Smith      | 10th   | B        | 90     |
| Alice Johnson   | 10th   | A        | 78     |
| Bob Brown       | 10th   | B        | 92     |
| Charlie Davis   | 10th   | A        | 88     |
| Emily Wilson    | 10th   | B        | 95     |
| David Lee       | 10th   | A        | 80     |


---

## 📸 Application Preview

![Screenshots](images/app_ui.png)
