class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # It will use to show to some people normal log for example
    def __str__(self):
        return f'Person name={self.name} age={self.age}'

    # It will use to use for compiler log, and some external Log for example
    def __repr__(self):
        return f'<Person({self.name}, {self.age})>'


bob = Person('Bob', 35)
print(bob)
