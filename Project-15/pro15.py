import sqlite3

# Connect to database (creates if not exists)
conn = sqlite3.connect("student_marks.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject1 REAL NOT NULL,
    subject2 REAL NOT NULL,
    subject3 REAL NOT NULL,
    average REAL NOT NULL
)
''')
conn.commit()

def validate_mark(mark):
    try:
        m = float(mark)
        if 0 <= m <= 100:
            return m
        else:
            print("❌ Mark should be between 0 and 100.")
            return None
    except ValueError:
        print("❌ Please enter a valid number.")
        return None

def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return
    
    while True:
        s1 = validate_mark(input("Enter mark for Subject 1: "))
        if s1 is not None:
            break

    while True:
        s2 = validate_mark(input("Enter mark for Subject 2: "))
        if s2 is not None:
            break

    while True:
        s3 = validate_mark(input("Enter mark for Subject 3: "))
        if s3 is not None:
            break

    avg = (s1 + s2 + s3) / 3
    cursor.execute("INSERT INTO students (name, subject1, subject2, subject3, average) VALUES (?, ?, ?, ?, ?)",
                   (name, s1, s2, s3, avg))
    conn.commit()
    print(f"✅ Student '{name}' added successfully with average {avg:.2f}.")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if not rows:
        print("⚠️ No student records found.")
        return

    print("\n--- Student Records ---")
    for row in rows:
        print(f"ID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Subject 1: {row[2]}")
        print(f"Subject 2: {row[3]}")
        print(f"Subject 3: {row[4]}")
        print(f"Average: {row[5]:.2f}")
        print("---------------------------")
    print()

def main():
    while True:
        print("\n🎓 Student Mark Tracker")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

# Close connection when program ends
conn.close()
