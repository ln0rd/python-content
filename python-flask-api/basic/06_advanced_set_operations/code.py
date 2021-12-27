friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne', 'Jasper'}

# this will return just Rolf, only not exist in abroad
local_friends = friends.difference(abroad)
print(local_friends)


# I can union my friends
# Remember sets not repeat elements
all_friends = friends.union(abroad)
print(all_friends)


art = {'Bob', 'Rolf', 'Anne'}
science = {'Bob', 'Anne', 'Jasper'}

# exist in both sets
both = art.intersection(science)
print(both)
