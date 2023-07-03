class Material:
    all_materials = []

    # переделать на хранение в sql где нить
    def __init__(self, name, path):
        self.name = name
        self.path = path
        Material.all_materials.append(self)


class Test:
    all_tests = []

    # переделать на хранение в sql где нить
    def __init__(self, name, path):
        self.name = name
        self.path = path
        Test.all_tests.append(self)
