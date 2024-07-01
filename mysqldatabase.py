import mysql.connector

def create_database_and_table(cursor):
    """
    Creates a database named 'school' and a table named 'students' with columns: 
    student_id, first_name, last_name, age, and grade.
    """
    cursor.execute("CREATE DATABASE IF NOT EXISTS school")
    cursor.execute("USE school")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            age INT,
            grade FLOAT
        )
    """)
    print("Database and table created.")

def insert_student(cursor, first_name, last_name, age, grade):
    """
    Inserts a new student record into the 'students' table.
    """
    cursor.execute("""
        INSERT INTO students (first_name, last_name, age, grade)
        VALUES (%s, %s, %s, %s)
    """, (first_name, last_name, age, grade))
    print(f"Student inserted: {first_name} {last_name}")

def update_student_grade(cursor, first_name, new_grade):
    """
    Updates the grade of the student with the given first name.
    """
    cursor.execute("""
        UPDATE students
        SET grade = %s
        WHERE first_name = %s
    """, (new_grade, first_name))
    print(f"Grade updated for {first_name} to {new_grade}")

def delete_student(cursor, last_name):
    """
    Deletes the student record with the given last name.
    """
    cursor.execute("""
        DELETE FROM students
        WHERE last_name = %s
    """, (last_name,))
    print(f"Student deleted with last name: {last_name}")

def fetch_all_students(cursor):
    """
    Fetches and displays all student records from the 'students' table.
    """
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("Fetching all students:")
    for student in students:
        print(f"Student ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}, Age: {student[3]}, Grade: {student[4]}")

def main():
    """
    Main function to perform all database operations.
    """
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        cursor = conn.cursor()

        # Create database and table
        create_database_and_table(cursor)

        # Insert a new student record
        insert_student(cursor, "Alice", "Smith", 18, 95.5)
        conn.commit()

        # Update the grade of the student with the first name "Alice"
        update_student_grade(cursor, "Alice", 97.0)
        conn.commit()

        # Delete the student with the last name "Smith"
        delete_student(cursor, "Smith")
        conn.commit()

        # Fetch and display all student records
        fetch_all_students(cursor)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the connection
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    main()
