# 2. There is a restriction in the authorization system:
# * the password must begin with a latin letter,
# * the password can consist of Latin letters, numbers, dot and minuses,
# * the password must end only with a latin letter or number;
# * minimum password length is one character
# * maximum password length is 20 characters
# Write a function that checks whether the input string matches this rule.
# (Come up with several ways to solve the problem and compare them.)
# Write a tests using unittest/pytest.

import re
import timeit
import logging


logging.basicConfig(level=logging.DEBUG)


class PasswordValidator:

    def __init__(self):
        self.isvalid = False

    def slow_validator(self, password):
        if re.match(r'^[a-zA-Z0-9.-]+$', password):
            self.isvalid = True
            logging.debug("2 pass")
        else:
            self.isvalid = False
            logging.debug("2 denied")

        if re.match(r'^[a-zA-Z]', password):
            self.isvalid = True
            logging.debug("1 pass")
        else:
            self.isvalid = False
            logging.debug("1 denied")

        if re.search(r'[a-zA-Z0-9]$', password):
            self.isvalid = True
            logging.debug("3 pass")
        else:
            self.isvalid = False
            logging.debug("3 denied")

        if 1 < len(password) < 20:
            logging.debug(len(password))
        else:
            self.isvalid = False
            logging.debug('Password is to long or cannot be empty')

        return self.isvalid

    def fast_validator(self, password):

        check_re1 = re.compile('^[a-zA-Z]')
        check_re2 = re.compile('^[a-zA-Z0-9.-]+$')
        check_re3 = re.compile('[a-zA-Z0-9]$')

        if check_re1.search(password):
            self.isvalid = True
            logging.debug("1 pass")
        else:
            self.isvalid = False
            logging.debug("1 denied")

        if check_re2.match(password):
            self.isvalid = True
            logging.debug("2 pass")
        else:
            self.isvalid = False
            logging.debug("2 denied")

        if check_re3.search(password):
            self.isvalid = True
            logging.debug("3 pass")
        else:
            self.isvalid = False
            logging.debug("3 denied")

        return self.isvalid


def main():
    v_pass = PasswordValidator()
    psw = 'dsadas-.dfs'

    def wrapper(func, *args, **kwargs):
        def wrapped():
            return func(*args, **kwargs)
        return wrapped

    print('raw regex method ', timeit.timeit(wrapper(v_pass.slow_validator, psw), number=100000))
    if v_pass.slow_validator(psw):
        print('Password is valid')
    else:
        print('Password is invalid')

    print('compiled regex method ', timeit.timeit(wrapper(v_pass.fast_validator, psw), number=100000))
    if v_pass.fast_validator(psw):
        print('Password is valid')
    else:
        print('Password is invalid')


if __name__ == "__main__":
    main()
