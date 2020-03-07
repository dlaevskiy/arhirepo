def my_shiny_new_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("I am the code which work before call of the function")
        function_to_decorate()  # function
        print("I am the code calling after")
        #  return this function
    return the_wrapper_around_the_original_function

def stand_alone_function():
    print("I am a standalone function! Do not change me!")

@my_shiny_new_decorator
def another_stand_alone_function():
    print 'Leave me!'

# -------------------------------------------------------------------------------

def bread(func):
    def wrapper():
        print '<HH>'
        func()
        print '<\______/>'
    return wrapper

def ingredients(func):
    def wrapper():
        print 'tomatoes'
        func()
        print 'salads'
    return wrapper

@bread
@ingredients
def sandwich(food='--ham--'):
    print food

if __name__ == '__main__':
    print '-----------------------'
    stand_alone_function()
    print '-----------------------'
    stand_alone_function = my_shiny_new_decorator(stand_alone_function)
    stand_alone_function()
    print '-----------------------'
    another_stand_alone_function()
    print '---Multi-decorators---'
    sandwich()


