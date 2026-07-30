import mysql.connector


def connect_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password",
            database="student_db"
        )

        return connection

    except mysql.connector.Error as err:
        print("Database Connection Error")
        print(err)
        return None