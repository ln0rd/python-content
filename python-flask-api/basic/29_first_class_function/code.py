# you can pass a function like variable and the variable will be this function

def divide(divided: int, divisor: int) -> int:
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0')

    return int(divided / divisor)


def calculate(*values: int, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(f'result of operator is: {result}')


# function to search something in the index
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f'Could not find an element with {expected}.')


friends: list = [
    {'name': 'Rolf', 'age': 24},
    {'name': 'Anne', 'age': 28},
    {'name': 'Oliver', 'age': 31}
]


def get_friend_name(friend):
    return friend['name']


print(search(friends, 'Oliver', get_friend_name))

# using lambda
print(search(friends, 'Oliver', lambda friend: friend['name']))
