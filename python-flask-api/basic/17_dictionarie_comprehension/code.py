users = [
    (0, 'Bob', 'password'),
    (1, 'Rolf', 'bob123'),
    (2, 'Jose', 'longp4assword'),
    (3, 'username', '1234')
]

# getting usernames from list of tuples
# it will create {'Bob': (0, 'Bob', 'password'), 'Rolf': (1, 'Rolf', 'bob123'), 'Jose': (2, 'Jose', 'longp4assword'), 'username': (3, 'username', '1234')}
username_mapping = {user[1]: user for user in users}
print(username_mapping)


# getting just names and creating new array from them

def getting_name(user):
    return {'name': user}


usernames = [getting_name(user) for user in users]
print(usernames)

# getting just names and creating new array from them
# it will return [{'name': 'Bob'}, {'name': 'Rolf'}, {'name': 'Jose'}, {'name': 'username'}]
usernames_example_two = [{'name': user[1]} for user in users]
print(usernames_example_two)
