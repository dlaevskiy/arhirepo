# 1.14. Sorting Objects Without Native Comparison Support
# Problem
# You want to sort objects of the same class, but they dont natively support comparison operations.

from operator import attrgetter

class User(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]

print users

# instead of this one we can use attrgetter see below
# print sorted(users, key=lambda u: u.user_id)

# using attrgetter - faster
print sorted(users, key=attrgetter('user_id'))  # here can be several attributes
