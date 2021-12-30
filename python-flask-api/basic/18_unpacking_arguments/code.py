# running the tuple of arguments and multplying them
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


total = multiply(1, 3, 5)
print(total)


# sum the values
def sumValues(x, y):
    return x + y


nums = [3, 5]
value = sumValues(*nums)
print(value)


# sum from dictionarie
nums = {'x': 15, 'y': 25}
result = sumValues(nums['x'], nums['y'])
print(result)


# When the name of parameters and the name of the properties expeted in a function it would be calling passing just the dictionerie with two **
result = sumValues(**nums)
print(result)


# apply like operator
def apply(*args, operator):
    if operator == '*':
        # use star because you want to pass just the first tuple of arguments
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        print('Not identified operator')


result = apply(10, 20, 15, 5, operator='+')
print(result)
result = apply(10, 20, 15, 5, operator='*')
print(result)
