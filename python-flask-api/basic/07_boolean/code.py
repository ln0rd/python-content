print(1 == 1)
print(1 == 0)
print(1 > 0)
print(1 < 0)
print(1 >= 0)
print(1 <= 0)
print(1 != 0)
print(1 != 1)


friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne', 'Jasper'}

# I can validate if sets are equal``
print(friends == abroad)

# When they are equall
friends = {'Bob'}
abroad = {'Bob'}
print(friends == abroad)

# Is - is the same object in memory
print(friends is friends)
