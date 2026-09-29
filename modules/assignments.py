from datetime import date
from models.assignment import Assignment
from utils.json_handler import load_json, save_json


DATA_FILE = "data/assignments.json"


def get_assignments():
    data = load_json(DATA_FILE, [])
    return [Assignment(
        item["id"],
        item["subject"],
        item["title"],
        item["due_date"],
        item["marks"],
        item["status"]
    ) for item in data]


def show_assignments():
    assignments = get_assignments()

    print("\n" + "=" * 85)
    print("ASSIGNMENT PERFORMANCE")
    print("=" * 85)
    print(f"{'Subject':<18}{'Assignment':<25}{'Due Date':<14}{'Marks':<10}{'Status':<12}")
    print("-" * 85)

    for a in assignments:
        marks = str(a.marks) if a.marks is not None else "-"
        print(f"{a.subject:<18}{a.title:<25}{a.due_date:<14}{marks:<10}{a.status:<12}")


def show_statistics():
    assignments = get_assignments()
    completed = [a for a in assignments if a.is_completed() and a.marks is not None]
    pending = [a for a in assignments if not a.is_completed()]

    print(f"\nTotal Assignments : {len(assignments)}")
    print(f"Completed         : {len(completed)}")
    print(f"Pending           : {len(pending)}")

    if completed:
        avg = sum(a.marks for a in completed) / len(completed)
        print(f"Average Marks     : {avg:.2f}")

    overdue = []
    today = date.today()

    for a in pending:
        try:
            due = date.fromisoformat(a.due_date)
            if due < today:
                overdue.append(a)
        except ValueError:
            pass

    print(f"Overdue           : {len(overdue)}")


def add_assignment():
    assignments = load_json(DATA_FILE, [])

    next_id = f"A{len(assignments) + 1:03d}"
    subject = input("Subject: ").strip()
    title = input("Assignment title: ").strip()
    due_date = input("Due date (YYYY-MM-DD): ").strip()

    assignments.append({
        "id": next_id,
        "subject": subject,
        "title": title,
        "due_date": due_date,
        "marks": None,
        "status": "Pending"
    })

    save_json(DATA_FILE, assignments)
    print(f"Assignment {next_id} added.")


def mark_completed():
    assignments = load_json(DATA_FILE, [])

    if not assignments:
        print("No assignments available.")
        return

    for item in assignments:
        print(f"{item['id']}: {item['title']} [{item['status']}]")

    assignment_id = input("Enter assignment ID: ").strip().upper()

    for item in assignments:
        if item["id"] == assignment_id:
            try:
                marks = float(input("Enter marks (0-100): "))
                if not 0 <= marks <= 100:
                    raise ValueError
            except ValueError:
                print("Marks must be between 0 and 100.")
                return

            item["marks"] = marks
            item["status"] = "Completed"
            save_json(DATA_FILE, assignments)
            print("Assignment updated.")
            return

    print("Assignment not found.")


def assignment_menu():
    while True:
        print("\n--- Assignment Performance Analyzer ---")
        print("1. View assignments")
        print("2. View statistics")
        print("3. Add assignment")
        print("4. Mark assignment completed")
        print("5. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_assignments()
        elif choice == "2":
            show_statistics()
        elif choice == "3":
            add_assignment()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            return
        else:
            print("Invalid choice.")
