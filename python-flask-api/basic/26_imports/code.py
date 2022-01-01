from my_module import divide
from lib import calculate
# or just
# import my_module
# my_module.divide()

print('code.py: ', __name__)

result: int = divide(dividend=8, divisor=2)
print(result)

# testing a class
calculate.Calculate.plus(5, 5)
