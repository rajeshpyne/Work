from abc import ABC, ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def person_method(self):
        """interface method"""
        pass


class Student(IPerson):
    def __init__(self):
        pass

    def person_method(self):
        return "This is a Student class"


class Teacher(IPerson):
    def __init__(self):
        pass

    def person_method(self):
        return "This is a Teacher class"


class PersonFactory:
    def __init__(self, type):
        self.type = type

    def get_class(self):
        if self.type == "teacher":
            return Teacher()
        elif self.type == "student":
            return Student()


if __name__ == "__main__":
    p1 = PersonFactory("student")
    # print(p1)
    get_entity = p1.get_class()
    entity = get_entity.person_method()
    print(entity)
