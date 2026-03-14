# Community Living Database

A community management system for gated societies built with Python, Streamlit, and MySQL.

## What is This?

This is a ticket management application for residential communities. Residents can raise tickets/complaints, and help desk staff can view, update, and resolve them. The system manages tickets, resident information, and community data.

## Technologies Used

- **Python** - Core programming language
- **Streamlit** - Web UI for the application
- **MySQL** - Database for storing resident and ticket information

## Project Structure

- `streamlit-and-mysql-ui/` - Main application code
  - `app.py` - Streamlit frontend
  - `database.py` - MySQL database connection and queries
  - `crud/` - Create, read, update, delete operations
- `ddl/` - Database DDL scripts
- `schema/` - Database schema documentation
- `report.pdf` - Project report

## Features

* Raise Tickets - Residents can submit complaints
* View All Tickets - See community tickets
* Update Tickets - Help desk can resolve issues
* Delete Tickets - Remove resolved tickets
* Custom Queries - Execute SQL queries directly

## How to run?

Install dependencies and specify host, user, database and password to mysql.connector
(in streamlit-and-mysql-ui/database.py), create database and run using streamlit run app.py
This will start the Streamlit server, and you can access the application in your web browser at http://localhost:8501.
