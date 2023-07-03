class Member:
    def __init__(self, name, surname, email, age, tel, position):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        self.tel = tel
        self.position = position


class Employee(Member):
    def __init__(self, post, experience, salary, type_contract, **kwargs):
        super().__init__(**kwargs)
        self.post = post
        self.experience = experience
        self.salary = salary
        self.type_contract = type_contract


class Student(Member):
    all_students = []

    def __init__(self, **kwargs):
        self.knowledge = []
        super().__init__(**kwargs)
        self.type = "student"
        self.all_students.append(self)

    def learning_lesson(self, lesson):
        self.knowledge += lesson

    @classmethod
    def get_all_students(cls):
        return cls.all_students

    def check_student(self):
        return self in self.all_students


class Teacher(Employee):
    all_teachers = []

    def __init__(self, grade, title, **kwargs):
        super().__init__(**kwargs)
        self.grade = grade
        self.title = title
        self.type = "teacher"
        self.all_teachers.append(self)

    @classmethod
    def get_all_teachers(cls):
        return cls.all_teachers

    def check_teacher(self):
        return self in self.all_teachers

    def hold_lesson(self):
        pass


class Curator(Employee):
    all_curators = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "curator"
        self.all_curators.append(self)

    @classmethod
    def get_all_curators(cls):
        return cls.all_curators

    @staticmethod
    def create_event(name_event, participants: list, date_event: datetime):
        try:
            # Дописать функцию создания события
            print(f"Сохранено событие {name_event} в {date_event} со следующими участниками: {participants}")
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def sending_notifications(message, list_recipient):
        try:
            # Дописать функцию отправки письма
            print(f"Отправлено письмо {message} на {list_recipient}")
            return True
        except Exception as e:
            print(e)
            return False


Vladislav = Teacher(grade=9, title="Bigger", post="Python", experience=100, salary=1000000, type_contract="main",
                    name="Vladislav", surname="Petrov", email="asds@vladislav", age=20, tel="1234567890",
                    position="employee")

print(Vladislav.__dict__)
