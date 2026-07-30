from operations import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

def display_menu():
    print("\n" + "=" * 45)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 45)


while True:

    display_menu()

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank you for using Student Management System.")
        print("Project Closed Successfully.")
        break

    else:
        print("\nInvalid Choice! Please enter a number between 1 and 6.")