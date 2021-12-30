# kwargs use two stars and you can create dictionaries from this
def named(**kwargs):
    print(kwargs)


# here I will get a dictionarie
named(name='leo', age='203')


# IF you want unpack the dictionarie to accept in variables in assignatures
# It will print: Leo 203
def named2(name, age):
    print(name, age)


named2(**{"name": 'Leo', "age": 203})


# another way to acess the values
def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')


print_nicely(name='Bob', age=50)
