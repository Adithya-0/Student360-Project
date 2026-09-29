from utils.json_handler import load_json


DATA_FILE = "data/placement.json"


def load_profile():
    data = load_json(DATA_FILE, {})
    return data


def readiness_score(profile):
    weights = {
        "academic": 0.25,
        "programming": 0.20,
        "dsa": 0.20,
        "projects": 0.15,
        "aptitude": 0.10,
        "communication": 0.10
    }

    return sum(profile.get(key, 0) * weight for key, weight in weights.items())


def placement_menu():
    while True:
        print("\n--- Placement Readiness Analyzer ---")
        print("1. View readiness profile")
        print("2. Calculate readiness score")
        print("3. View improvement areas")
        print("4. Back")

        choice = input("Enter your choice: ").strip()
        profile = load_profile()

        if choice == "1":
            print("\nPLACEMENT READINESS")
            print("-" * 35)
            labels = {
                "academic": "Academic Performance",
                "programming": "Programming Skills",
                "dsa": "Data Structures & Algorithms",
                "projects": "Projects",
                "aptitude": "Aptitude",
                "communication": "Communication"
            }
            for key, label in labels.items():
                print(f"{label:<30}: {profile.get(key, 0):.0f}%")

        elif choice == "2":
            score = readiness_score(profile)
            print(f"\nOverall Placement Readiness: {score:.1f}%")

        elif choice == "3":
            labels = {
                "academic": "Academic Performance",
                "programming": "Programming Skills",
                "dsa": "Data Structures & Algorithms",
                "projects": "Projects",
                "aptitude": "Aptitude",
                "communication": "Communication"
            }
            weak = [
                label for key, label in labels.items()
                if profile.get(key, 0) < 70
            ]

            if weak:
                print("\nAreas to improve:")
                for item in weak:
                    print(f"- {item}")
            else:
                print("\nNo area is currently below the 70% threshold.")

        elif choice == "4":
            return
        else:
            print("Invalid choice.")
