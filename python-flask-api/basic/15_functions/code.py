def user_age_in_seconds():
    user_age = int(input('Enter your age: '))
    age_seconds = user_age * 360 * 24 * 60 * 60
    print(age_seconds)


def add(x, y):
    # Do nothing
    pass


def say_hello(name, otherName):
    print(f' Hello {name} and Hello {otherName}')


say_hello('leo', 'Anne')
say_hello(name='leo', otherName='Anne')


# setting default value on parameter
def with_default_value(x, y='leo'):
    print(x, y)


with_default_value('Hi')


# return
def sum(x, y):
    return x + y


result = sum(1, 1)
print(result)
