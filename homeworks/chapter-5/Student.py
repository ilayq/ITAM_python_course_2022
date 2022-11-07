class WrongData(Exception):
    pass


class Student:
    id: int
    name: str
    group: str

    def __init__(self, student_id: int, name: str, group: str) -> None:
        self.id = student_id
        self.name = name
        self.group = group
        if not self.validate():
            raise WrongData

    def validate(self):
        return type(self.id) == int and type(self.group) == str and type(self.name) == str
