class Student:
    def __init__(self, student_id, name, year, branch, college, email, skills=None):
        self.student_id = student_id
        self.name = name
        self.year = year
        self.branch = branch
        self.college = college
        self.email = email
        self.skills = skills or []

    def display(self):
        print(f"{self.name} ({self.student_id}) - Year {self.year} {self.branch}")
