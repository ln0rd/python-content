# self is like this, you need to receive it to use
class Student:
    def __init__(self):
        self.name = 'Rolf'
        self.grades = (90, 90, 93, 78, 90)

    def average_grade(self):
        return f'Average: {sum(self.grades) / len(self.grades)}'


class Car:
    def __init__(self, model, km):
        self.model = model
        self.km = km

    def run(self, km):
        self.km += km


student = Student()
print(student.name)
print(student.grades)
print(student.average_grade())


car = Car('Pajero', 100)
print(car.km)
car.run(10)
print(car.km)
