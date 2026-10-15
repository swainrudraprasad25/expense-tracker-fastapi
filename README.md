# Expense Tracker

A simple expense tracker built with FastAPI, MySQL and Jinja2 templates.

## Features
- Add an expense (category, amount, date, description)
- View all expenses in a table
- Search by category
- Filter by date range
- See the highest expense and the total expense

## Tech Stack
Python, FastAPI, MySQL, Jinja2, HTML

## Project Structure
expense_tracker/
├── main.py
├── database.py
└── templates/
    ├── home.html
    ├── add_expense.html
    ├── expenses.html
    ├── search_catagory.html
    ├── filter.html
    └── total.html

## Setup

1. Install dependencies:
   pip install fastapi uvicorn mysql-connector-python python-multipart jinja2

2. Create the database and table:
   CREATE DATABASE IF NOT EXISTS expense_db;
   USE expense_db;
   CREATE TABLE record (
     id INT PRIMARY KEY,
     catagory VARCHAR(100),
     amount INT,
     travelDate DATE,
     description VARCHAR(255)
   );

3. Set your MySQL credentials in `database.py`
   (better: use a `.env` file).

4. Run the server:
   uvicorn main:app --reload

5. Open http://127.0.0.1:8000/ in your browser.

## Routes
| Method | Route | Description |
|--------|-------|-------------|
| GET/POST | /add-expense | Add a new expense |
| GET | /show-expense | Show all expenses |
| GET/POST | /search | Search by category |
| GET/POST | /search_filter | Filter by date range |
| GET | /highest_expense | Show the highest expense |
| GET | /total_expense | Show the total expense |
