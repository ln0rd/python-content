grades = [35, 67, 98, 100, 100]
total = 0
total_with_sum = sum(grades)  # return de sum about all elements in a list
amount = len(grades)  # return the number of items in a list


for grade in grades:
    total += grade

print(f'Average {total / amount}')
print(f'Average {total_with_sum / amount}')
