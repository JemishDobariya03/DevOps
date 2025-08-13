students = {}

while True:
    print("\nChoose an option:")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        if name in students:
            print(f"{name} already exists.")
        else:
            students[name] = grade
            print(f"Added {name} with grade {grade}.")
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"{name} not found.")
    elif choice == "3":
        if not students:
            print("No students found.")
        else:
            print("Student Grades:")
            for name, grade in students.items():
                print(f"{name}: {grade}")
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")