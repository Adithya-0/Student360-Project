class Subject:
    def __init__(self, code, name, marks, credits):
        self.code = code
        self.name = name
        self.marks = marks
        self.credits = credits

    def grade(self):
        if self.marks >= 90:
            return "A+"
        if self.marks >= 80:
            return "A"
        if self.marks >= 70:
            return "B"
        if self.marks >= 60:
            return "C"
        if self.marks >= 50:
            return "D"
        return "F"

    def grade_point(self):
        points = {"A+": 10, "A": 9, "B": 8, "C": 7, "D": 6, "F": 0}
        return points[self.grade()]
