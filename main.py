from modules.performance import performance_menu
from modules.assignments import assignment_menu
from modules.progress import progress_menu
from modules.placement import placement_menu
from modules.reports import overall_report
from utils.json_handler import load_json
from utils.validators import get_non_empty


DATA_DIR = "data"


def student_profile():
    students = load_json(f"{DATA_DIR}/students.json", [])
    if not students:
        print("\nNo student profile found.")
        return

    student = students[0]
    print("\n" + "=" * 50)
    print("STUDENT PROFILE")
    print("=" * 50)
    print(f"Name       : {student['name']}")
    print(f"Student ID : {student['id']}")
    print(f"Year       : {student['year']}")
    print(f"Branch     : {student['branch']}")
    print(f"College    : {student['college']}")
    print(f"Email      : {student['email']}")
    print(f"Skills     : {', '.join(student.get('skills', []))}")
    print("=" * 50)


def main():
    while True:
        print("\n" + "=" * 56)
        print("                 STUDENT360")
        print("       Student Academic & Career Analytics")
        print("=" * 56)
        print("1. Student Performance Analyzer")
        print("2. Assignment Performance Analyzer")
        print("3. Student Progress Tracker")
        print("4. Placement Readiness Analyzer")
        print("5. Student Profile")
        print("6. Generate Overall Report")
        print("7. Exit")
        print("=" * 56)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            performance_menu()
        elif choice == "2":
            assignment_menu()
        elif choice == "3":
            progress_menu()
        elif choice == "4":
            placement_menu()
        elif choice == "5":
            student_profile()
        elif choice == "6":
            overall_report()
        elif choice == "7":
            print("\nThank you for using Student360.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
