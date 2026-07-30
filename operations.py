from database import connect_database


# ---------------------- ADD STUDENT ----------------------

def add_student():
    conn = connect_database()

    if conn is None:
        return

    cursor = conn.cursor()

    print("\n========== ADD STUDENT ==========")

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    query = """
    INSERT INTO students(name, age, department, email, phone)
    VALUES(%s,%s,%s,%s,%s)
    """

    values = (name, age, department, email, phone)

    try:
        cursor.execute(query, values)
        conn.commit()
        print("\nStudent Added Successfully!")

    except Exception as e:
        print("Error:", e)

    cursor.close()
    conn.close()


# ---------------------- VIEW STUDENTS ----------------------

def view_students():

    conn = connect_database()

    if conn is None:
        return

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\n================ ALL STUDENTS ================\n")

    if len(students) == 0:
        print("No Student Records Found")

    else:

        print("{:<5} {:<20} {:<5} {:<20} {:<30} {:<15}".format(
            "ID", "NAME", "AGE", "DEPARTMENT", "EMAIL", "PHONE"
        ))

        print("-" * 110)

        for student in students:

            print("{:<5} {:<20} {:<5} {:<20} {:<30} {:<15}".format(
                student[0],
                student[1],
                student[2],
                student[3],
                student[4],
                student[5]
            ))

    cursor.close()
    conn.close()


# ---------------------- SEARCH STUDENT ----------------------

def search_student():

    conn = connect_database()

    if conn is None:
        return

    cursor = conn.cursor()

    student_id = input("\nEnter Student ID : ")

    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))

    student = cursor.fetchone()

    if student:

        print("\nStudent Found\n")

        print("ID :", student[0])
        print("Name :", student[1])
        print("Age :", student[2])
        print("Department :", student[3])
        print("Email :", student[4])
        print("Phone :", student[5])

    else:

        print("\nStudent Not Found")

    cursor.close()
    conn.close()


# ---------------------- UPDATE STUDENT ----------------------

def update_student():

    conn = connect_database()

    if conn is None:
        return

    cursor = conn.cursor()

    student_id = input("\nEnter Student ID to Update : ")

    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))

    student = cursor.fetchone()

    if student is None:

        print("Student Not Found")

        cursor.close()
        conn.close()
        return

    print("\nEnter New Details\n")

    name = input("Name : ")
    age = int(input("Age : "))
    department = input("Department : ")
    email = input("Email : ")
    phone = input("Phone : ")

    query = """
    UPDATE students
    SET name=%s,
        age=%s,
        department=%s,
        email=%s,
        phone=%s
    WHERE id=%s
    """

    values = (name, age, department, email, phone, student_id)

    cursor.execute(query, values)

    conn.commit()

    print("\nStudent Updated Successfully")

    cursor.close()
    conn.close()


# ---------------------- DELETE STUDENT ----------------------

def delete_student():

    conn = connect_database()

    if conn is None:
        return

    cursor = conn.cursor()

    student_id = input("\nEnter Student ID to Delete : ")

    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))

    student = cursor.fetchone()

    if student is None:

        print("Student Not Found")

        cursor.close()
        conn.close()
        return

    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))

    conn.commit()

    print("\nStudent Deleted Successfully")

    cursor.close()
    conn.close()