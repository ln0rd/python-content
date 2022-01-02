# We would do it, but we will use decorator


def secury_get_admin(user):
    if user['acess_level'] == 'admin':
        return '12345#'
    return None

# using decorator below!


def get_admin_password():
    return '12345#'


def acess_denied():
    return 'Acess Denied'

# Decorator


def make_secure(func):
    def secure_function():
        if user['acess_level'] == 'admin':
            return func()

    return secure_function


user = {'username': 'jose', 'acess_level': 'guest'}
get_admin_password = make_secure(get_admin_password)
print(get_admin_password())


user = {'username': 'jose', 'acess_level': 'admin'}
get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
