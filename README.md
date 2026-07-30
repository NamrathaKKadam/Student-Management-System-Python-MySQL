# Student Management System

A console-based Student Management System developed using **Python** and **MySQL**. The application allows users to efficiently manage student records through CRUD (Create, Read, Update, Delete) operations.

---

## Features

- Add Student
- View All Students
- Search Student by ID
- Update Student Details
- Delete Student
- Menu-Driven Console Application
- MySQL Database Integration
- Error Handling

---

## Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- VS Code

---

## Project Structure

```
StudentManagementSystem/
│
├── database.py
├── operations.py
├── main.py
├── student_db.sql
├── README.md
├── requirements.txt
├── .gitignore
└── screenshots/
```

---

## Database

Database Name

```
student_db
```

Table

```
students
```

| Column | Type |
|----------|------------|
| id | INT (Primary Key) |
| name | VARCHAR(100) |
| age | INT |
| department | VARCHAR(100) |
| email | VARCHAR(100) |
| phone | VARCHAR(15) |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/NamrathaKKadam/Student-Management-System-Python-MySQL.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

1. Install MySQL Server
2. Open MySQL Workbench
3. Execute `student_db.sql`
4. Update your MySQL password in `database.py`

### Run

```bash
python main.py
```

---

## Screenshots

- Home Screen
- Add Student
- View Students
- Search Student
- Update Student
- Delete Student

---

## Future Enhancements

- Login Authentication
- GUI using Tkinter
- Export Data to Excel
- Search by Name
- Email Validation
- Phone Validation

---

## Author

Namratha K Kadam