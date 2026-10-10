from models.subject import Subject
from utils.json_handler import load_json
from utils.calculations import average


DATA_FILE = "data/subjects.json"


def get_subjects():
    data = load_json(DATA_FILE, [])
    return [Subject(
        item["code"],
        item["name"],
        item["marks"],
        item["credits"]
    ) for item in data]


def show_subject_marks():
    subjects = get_subjects()
    print(subjects)
    print("\n" + "=" * 65)
    print("STUDENT PERFORMANCE")
    print("=" * 65)
    print(f"{'Code':<10}{'Subject':<25}{'Marks':<10}{'Grade':<10}{'Credits':<8}")
    print("-" * 65)

    for subject in subjects:
        print(
            f"{subject.code:<10}{subject.name:<25}"
            f"{subject.marks:<10}{subject.grade():<10}{subject.credits:<8}"
        )


def show_statistics():
    subjects = get_subjects() #List of subject classes
    marks = [s.marks for s in subjects]

    if not subjects:
        print("No subject data available.")
        return

    highest = max(subjects, key=lambda s: s.marks) # highest represents a specific subject class
    lowest = min(subjects, key=lambda s: s.marks)

    print(f"\nAverage Marks : {average(marks):.2f}")
    print(f"Highest       : {highest.name} ({highest.marks})")
    print(f"Lowest        : {lowest.name} ({lowest.marks})")
    print(f"Pass Rate     : {sum(s.marks >= 50 for s in subjects) / len(subjects) * 100:.1f}%")


def calculate_gpa():
    subjects = get_subjects()
    total_credits = sum(s.credits for s in subjects)
    if total_credits == 0:
        return 0
    return sum(s.grade_point() * s.credits for s in subjects) / total_credits


def performance_menu():
    while True:
        print("\n--- Student Performance Analyzer ---")
        print("1. View subject marks")
        print("2. View statistics")
        print("3. Calculate GPA")
        print("4. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_subject_marks()
        elif choice == "2":
            show_statistics()
        elif choice == "3":
            print(f"\nCurrent GPA: {calculate_gpa():.2f}")
        elif choice == "4":
            return
        else:
            print("Invalid choice.")
