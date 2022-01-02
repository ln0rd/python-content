import functools

# We would do it, but we will use decorator


def secury_get_admin(user):
    if user['acess_level'] == 'admin':
        return '12345#'
    return None

# using decorator below!

# It will pass this functions always how argument in make_secure_function when It would be called


@make_secure
def get_admin_password():
    return '12345#'


def acess_denied():
    return 'Acess Denied'

# Decorator


def make_secure(func):

    # it will tell to python compiler that @Make_secure is this function
    @functools.wraps(get_admin_password)
    def secure_function():
        if user['acess_level'] == 'admin':
            return func()

    return secure_function


user = {'username': 'jose', 'acess_level': 'guest'}
print(get_admin_password())


user = {'username': 'jose', 'acess_level': 'admin'}
print(get_admin_password())
