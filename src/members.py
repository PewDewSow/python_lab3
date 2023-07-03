class Member:
    def __init__(self, name, surname, email, age, tel, position):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        self.tel = tel
        self.position = position


class Employee:
    def __init__(self, private_data: Member, post, experience, salary, type_contract):
        self.private_data = private_data
        self.post = post
        self.experience = experience
        self.salary = salary
        self.type_contract = type_contract


class Student(Member):
    all_students = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "student"
        self.all_students.append(self)

    def get_all_students(self):
        return self.all_students


class Teacher(Member, Employee):
    all_teachers = []

    def __init__(self, name, surname, email, age, tel, position):
        super().__init__(name, surname, email, age, tel, position)
        self.type = "teacher"
        self.all_teachers.append(self)


Vanya = Student(name="Vanya", surname="Petrov", email="efpyi@example.com", age=25, tel="07912345678",
                position="student")
print(Vanya.name, Vanya.surname, Vanya.email, Vanya.age, Vanya.tel, Vanya.position)
