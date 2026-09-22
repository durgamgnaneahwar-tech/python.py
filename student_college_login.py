"""Simple College Student Login project (console application).

Run with:
    python student_college_login.py
"""

import hashlib
import sqlite3
from getpass import getpass


DATABASE = "college_portal.db"


def hash_password(password):
    """Return a one-way hash so plain-text passwords are not stored."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def create_database():
    with sqlite3.connect(DATABASE) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                course TEXT NOT NULL,
                password_hash TEXT NOT NULL
            )
            """
        )


def register_student():
    print("\n--- Student Registration ---")
    student_id = input("Student ID: ").strip()
    name = input("Full name: ").strip()
    course = input("Course: ").strip()
    password = getpass("Create password: ")
    confirm_password = getpass("Confirm password: ")

    if not all([student_id, name, course, password]):
        print("All fields are required.")
        return
    if password != confirm_password:
        print("Passwords do not match.")
        return
    if len(password) < 4:
        print("Password must contain at least 4 characters.")
        return

    try:
        with sqlite3.connect(DATABASE) as connection:
            connection.execute(
                "INSERT INTO students VALUES (?, ?, ?, ?)",
                (student_id, name, course, hash_password(password)),
            )
        print("Registration successful. You can now log in.")
    except sqlite3.IntegrityError:
        print("That Student ID is already registered.")


def login_student():
    print("\n--- Student Login ---")
    student_id = input("Student ID: ").strip()
    password = getpass("Password: ")

    with sqlite3.connect(DATABASE) as connection:
        student = connection.execute(
            "SELECT student_id, name, course FROM students "
            "WHERE student_id = ? AND password_hash = ?",
            (student_id, hash_password(password)),
        ).fetchone()

    if student:
        print("\nLogin successful!")
        print("=" * 32)
        print("College Student Dashboard")
        print("=" * 32)
        print(f"Student ID : {student[0]}")
        print(f"Name       : {student[1]}")
        print(f"Course     : {student[2]}")
    else:
        print("Invalid Student ID or password.")


def main():
    create_database()

    while True:
        print("\n===== COLLEGE STUDENT PORTAL =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            login_student()
        elif choice == "3":
            print("Thank you for using the College Student Portal.")
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
