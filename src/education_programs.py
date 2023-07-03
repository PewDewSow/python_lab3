class EducationProgram:
    all_programs = []

    def __init__(self, program_name, list_disciplines: list):
        self.program_name = program_name
        self.list_disciplines = list_disciplines
        self.all_programs.append(self)

    def add_discipline(self, discipline):
        self.list_disciplines.append(discipline)

    def del_discipline(self, discipline):
        try:
            self.list_disciplines.remove(discipline)
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def get_all_programs(cls):
        return cls.all_programs


class Discipline:
    all_disciplines = []

    def __init__(self, discipline_name, list_lessons: list, list_teachers: list):
        self.discipline_name = discipline_name
        self.list_lessons = list_lessons
        self.list_teachers = list_teachers
        self.all_disciplines.append(self)

    def add_lesson(self, lesson):
        self.list_lessons.append(lesson)

    def remove_lesson(self, lesson):
        try:
            self.list_lessons.remove(lesson)
            return True
        except Exception as e:
            print(e)
            return False

    def check_teacher_by_discipline(self, teacher):
        return teacher in self.list_teachers

    def get_teachers_by_discipline(self):
        return self.list_teachers

    @classmethod
    def get_all_disciplines(cls):
        return cls.all_disciplines


class Lesson:
    all_lessons = []

    def __init__(self, lesson_name, list_themes: list):
        self.lesson_name = lesson_name
        self.list_themes = list_themes
        self.all_lessons.append(self)

    def add_theme(self, theme):
        self.list_themes.append(theme)

    def del_theme(self, theme):
        try:
            self.list_themes.remove(theme)
            return True
        except Exception as e:
            print(e)
            return False

    def check_theme(self, theme):
        return theme in self.list_themes

    @classmethod
    def get_all_lessons(cls):
        return cls.all_lessons


class Theme:
    all_themes = []

    def __init__(self, theme_name, materials: list, tests: list):
        self.theme_name = theme_name
        self.materials = materials
        self.tests = tests
        self.all_themes.append(self)

    @classmethod
    def get_all_themes(cls):
        return cls.all_themes

    def add_test(self, test):
        self.tests.append(test)

    def del_test(self, test):
        try:
            self.tests.remove(test)
            return True
        except Exception as e:
            print(e)
            return False

    def add_material(self, material):
        self.materials.append(material)

    def del_material(self, material):
        try:
            self.materials.remove(material)
            return True
        except Exception as e:
            print(e)
            return False

    def get_all_materials(self):
        return self.materials

    def get_all_tests(self):
        return self.tests
