numbers = [1, 3, 5]
doubled = []

# Think that you want to put the list numbers multiplied by two

# way 1
for number in numbers:
    doubled.append(number * 2)
print(doubled)

# way 2
doubled = [number * 2 for number in numbers]
print(doubled)

# Think that you want put in the start_with_s just names that start with s from friends list

# way 1
friends = ['Rolf', 'Sam', 'Samantha', 'Saurabh', 'Jen']
start_with_s = []

for friend in friends:
    if friend.startswith('S'):
        start_with_s.append(friend)
print(start_with_s)

# way 2
start_with_s = [friend for friend in friends if friend.startswith('S')]
print(start_with_s)
