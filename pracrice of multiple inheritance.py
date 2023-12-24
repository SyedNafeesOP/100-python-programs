class Ansar:
    def __init__(self, name, study):
        self.name = name
        self.study = study

    def show(self):
        print(f"name is {self.name}")

class Nafees:
    def __init__(self, name, study):
        self.name = name
        self.study = study

    def show(self):
        print(f"name is {self.name}")
        print(f"study in {self.study}")

class Masroor(Nafees, Ansar):
    def __init__(self, name, study, nickname):
        Nafees.__init__(self, name, study)
        Ansar.__init__(self, name, study)
        self.nickname = nickname

    def show(self):
        Nafees.show(self)
        print(f"nickname is {self.nickname}")

o1 = Masroor("Masroor", "Computer Science", "china is a nickname")
o1.show()
