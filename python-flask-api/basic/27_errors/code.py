# raise start a error

def divide(dividend: int, divisor: int) -> float:
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0')

    return dividend / divisor


# result: float = divide(dividend=15, divisor=0)
# print(result)

# TRY
try:
    result: float = divide(dividend=15, divisor=0)
except ZeroDivisionError:
    print('Error: Divisor has a problem, cannot be 0 ')
