class Assignment:
    def __init__(self, assignment_id, subject, title, due_date, marks, status):
        self.assignment_id = assignment_id
        self.subject = subject
        self.title = title
        self.due_date = due_date
        self.marks = marks
        self.status = status

    def is_completed(self):
        return self.status.lower() == "completed"
