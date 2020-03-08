"""
I am: docstr.__doc__
"""

def func(args):
    """I am: docstr.func.__doc__"""
    pass

class Spam(object):
    """I am: spam.__doc__ or docstr.spam.__doc__"""
    def method(self, arg):
        """I am: spam.method.__doc__ or self.method.__doc__"""
        pass

if __name__ == '__main__':
    print __doc__
    print func.__doc__
    print Spam.__doc__
    print Spam.method.__doc__
