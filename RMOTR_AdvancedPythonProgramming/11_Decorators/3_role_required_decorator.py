# Write a class based decorator role_required that takes a role (eg: admin, staff, superuser, etc) and restricts the decorated function or method to be executed or not based on the user that's being passed. This decorator should be generic, and could be used in any function, that's why it requires some configuration to be used. Examples:
#
#     @role_required(role='owner', user_arg_name='user', user_role_attr='level')
#     def delete_bank_account(start_date, end_date, user=user):
#       # The user's role is stored under the 'level' attribute
#       print(user.level)  # owner
#
#     @role_required(role='admin', user_arg_name='account', user_role_attr='role')
#     def delete_records(start_date, end_date, account=account):
#       # The user is stored in the 'account' param
#       # The user's role is stored under the 'role' attribute
#       print(account.role)  # admin


import unittest
from collections import namedtuple


Account = namedtuple('Account', ['name', 'role'])


class role_required(object):

    def __init__(self, role, user_arg_name, user_role_attr):
        self.role = role
        self.user_arg_name = user_arg_name
        self.user_role_attr = user_role_attr

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if getattr(kwargs[self.user_arg_name], self.user_role_attr) == self.role:
                return func(*args, **kwargs)
            else:
                raise ValueError
        return wrapper

class User(object):
    def __init__(self, name, level):
        self.name = name
        self.level = level


@role_required(role='owner', user_arg_name='user', user_role_attr='level')
def f1(random_arg, user):
    return "User {} with role {} doing {}".format(
        user.name, user.level, random_arg)


@role_required(role='admin', user_arg_name='account', user_role_attr='role')
def f2(random_arg, account):
    return "Account {} with role {} doing {}".format(
        account.name, account.role, random_arg)


class AssignmentTestCase(unittest.TestCase):
    def test_user_and_level_params_succesful(self):
        res = f1('stuff', user=User(name='John', level='owner'))
        self.assertEqual(res, "User John with role owner doing stuff")

    def test_user_and_level_params_raises(self):
        with self.assertRaises(ValueError):
            f1('playing hockey', user=User(name='Robert', level='staff'))

    def test_account_and_role_params_succesful(self):
        res = f2('stuff', account=Account(name='John', role='admin'))
        self.assertEqual(res, "Account John with role admin doing stuff")

    def test_account_and_role_params_raises(self):
        with self.assertRaises(ValueError):
            f2('playing hockey', account=Account(name='Robert', role='staff'))