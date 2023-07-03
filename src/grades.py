class Grade:
    grade_dict = {2: range(0, 50), 3: range(50, 70), 4: range(70, 90), 5: range(90, 101)}

    @classmethod
    def translate_grade(cls, points):
        return [key for key, value in cls.grade_dict.items() if points in value][0]
