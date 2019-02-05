from flask import session
from functools import wraps

def check_logged_in(func) -> 'func':
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are Not logged in.'
    return wrapper
