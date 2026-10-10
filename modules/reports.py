from modules.performance import calculate_gpa, get_subjects
from modules.progress import get_semesters
from modules.placement import load_profile, readiness_score


def overall_report():
    subjects = get_subjects()
    semesters = get_semesters()
    placement = load_profile()

    print("\n" + "=" * 60)
    print("                 STUDENT360 REPORT")
    print("=" * 60)

    gpa = calculate_gpa()
    print(f"\nCurrent GPA              : {gpa:.2f}")
    print(f"Placement Readiness      : {readiness_score(placement):.1f}%")

    if semesters:
        first = semesters[0].gpa
        latest = semesters[-1].gpa
        print(f"Latest Semester GPA      : {latest:.2f}")
        print(f"GPA Change               : {latest - first:+.2f}")

    print("\nStrong Areas:")
    strong = [s.name for s in subjects if s.marks >= 80]
    if strong:
        for item in strong:
            print(f"  + {item}")
    else:
        print("  No subject currently above 80.")

    print("\nAreas to Improve:")
    weak = [s.name for s in subjects if s.marks < 70]
    weak += [
        key.replace("_", " ").title()
        for key, value in placement.items()
        if isinstance(value, (int, float)) and value < 70
    ]
    if weak:
        for item in weak:
            print(f"  - {item}")
    else:
        print("  No immediate improvement areas identified.")

    print("\n" + "=" * 60)
