from functools import wraps

def home_decorator():
    def _home_decorator(f):
        @wraps(f)
        def __home_decorator(*args, **kwargs):

            # just do here everything what you need

            print('before home')
            result = f(*args, **kwargs)
            print('home result: %s' % result)
            print('after home')
            return result
        return __home_decorator
    return _home_decorator