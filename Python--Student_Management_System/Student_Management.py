import os

FILE_NAME = "students.txt"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{roll},{name},{age},{grade}\n")

    print("Student added successfully.\n")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as f:
        data = f.readlines()

    if not data:
        print("No students found.\n")
        return

    print("\nStudent Records:")
    for line in data:
        roll, name, age, grade = line.strip().split(",")
        print(f"Roll: {roll} | Name: {name} | Age: {age} | Grade: {grade}")
    print()


def search_student():
    roll_search = input("Enter Roll Number to search: ")

    with open(FILE_NAME, "r") as f:
        for line in f:
            roll, name, age, grade = line.strip().split(",")
            if roll == roll_search:
                print(f"Found: {roll} | {name} | {age} | {grade}\n")
                return

    print("Student not found.\n")


def delete_student():
    roll_delete = input("Enter Roll Number to delete: ")

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    with open(FILE_NAME, "w") as f:
        found = False
        for line in lines:
            roll, name, age, grade = line.strip().split(",")
            if roll != roll_delete:
                f.write(line)
            else:
                found = True

    if found:
        print("Student deleted successfully.\n")
    else:
        print("Student not found.\n")


while True:
    print("----- Student Management System -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.\n")