# IMPORTANT
# Variable set outside __init__ belong to the class. They're shared by all instances.
# Variables created inside __init__ (and all other method functions) and prefaced with self. belong to the object instance.

class ClassTest:
    def __init__(self, info):
        self.info = info

    def instance_method(self):
        print(f'Called instance_method of {self}')

    @classmethod
    def class_method(this_class):
        print(f'Called class_methd of {this_class}')

    @staticmethod
    def static_method():
        print(f'Calle static_method')

    def __str__(self):
        return f'Person: {self.info}'


# We just can acess this method from an instance of this Class
test = ClassTest('info 1')
test.instance_method()

# We can call class_method because this is like a STATIC method but it receive the same class with parameter by python compiler
ClassTest.class_method()

# Static method doesn't receive a parameter like the same class
ClassTest.static_method()
