# Lambda functions doesn't has a name just used to return values
def my_lambda(x, y): return x + y


print(my_lambda(1, 1))

# function to double


def double(value):
    return value * 2


# if you want to run the list and multiply every item for 2
sequence = [1, 3, 5, 9]
sequece_doubled = [item * 2 for item in sequence]
sequece_doubled_from_function = [double(item) for item in sequence]
print(sequece_doubled)
print(sequece_doubled_from_function)


# you can apply a function in each element in a list using map
doubled = list(map(double, sequence))
print(doubled)
