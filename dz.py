class Student:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_average_grade(self, average_grade):
        self.average_grade = average_grade

    def get_average_grade(self):
        return self.average_grade

    def display_information(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.average_grade}")


class SeniorStudent(Student):
    def __init__(self, name, age, average_grade, thesis_title):
        super().__init__(name, age, average_grade)
        self.thesis_title = thesis_title

    def set_thesis_title(self, thesis_title):
        self.thesis_title = thesis_title

    def get_thesis_title(self):
        return self.thesis_title

student1 = Student("Акан", 20, 4.5)
student1.set_name("Алихан")
student1.display_information()

senior_student1 = SeniorStudent("Альбина", 22, 4.8, "Анализ социальных сетей")
senior_student1.display_information()
senior_student1.set_thesis_title("Исследование поведения потребителей в онлайн-магазинах")
senior_student1.display_information()
