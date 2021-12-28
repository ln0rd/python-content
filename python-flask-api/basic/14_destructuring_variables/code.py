t = 5, 11
print(t)

x, y = t

print(x, y)

# example with list of tuples
people = [
    ('Bob', 42, 'Mechanic'),
    ('James', 24, 'Artist'),
    ('Harry', 32, 'Lecturer')
]
for name, age, profession in people:
    print(f'name {name}, age {age}, profession {profession}')

for name, _, profession in people:
    print(f'name {name}, profession {profession}')


head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
