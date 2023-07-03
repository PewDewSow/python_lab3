from src.members import Curator
from src.members import Student


class Group:
    all_groups = []

    def __init__(self, curator: Curator, list_students: list):
        self.curator = curator
        self.list_students = list_students
        self.all_groups.append(self)

    def add_student(self, student: Student):
        self.list_students.append(student)

    def del_student(self, student: Student):
        self.list_students.remove(student)

    def get_all_students_group(self):
        return self.list_students

    def get_all_email_group(self):
        return [student.email for student in self.list_students]

    def check_student_by_group(self, student: Student):
        return student in self.list_students
