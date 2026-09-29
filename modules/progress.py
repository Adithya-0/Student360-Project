from models.semester import Semester
from utils.json_handler import load_json
from utils.calculations import percentage_change


DATA_FILE = "data/semesters.json"


def get_semesters():
    data = load_json(DATA_FILE, [])
    return [Semester(item["semester"], item["gpa"]) for item in data]


def show_progress():
    semesters = get_semesters()

    if not semesters:
        print("No semester data available.")
        return

    print("\n" + "=" * 45)
    print("STUDENT PROGRESS TRACKER")
    print("=" * 45)

    for semester in semesters:
        print(f"Semester {semester.semester}: GPA {semester.gpa:.2f}")

    if len(semesters) >= 2:
        first = semesters[0].gpa
        latest = semesters[-1].gpa
        change = percentage_change(first, latest)

        print("-" * 45)
        print(f"Overall Change : {change:+.2f}%")

        if latest > first:
            print("Trend          : Improving")
        elif latest < first:
            print("Trend          : Declining")
        else:
            print("Trend          : Stable")


def progress_menu():
    while True:
        print("\n--- Student Progress Tracker ---")
        print("1. View semester progress")
        print("2. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_progress()
        elif choice == "2":
            return
        else:
            print("Invalid choice.")
