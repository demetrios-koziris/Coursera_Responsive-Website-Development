def say_hello():
    # block belonging to the function
    print('hello world')
# End of function

say_hello()  # call the function
say_hello()  # call the function again

def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


c=10
func(3, 7)
func(25, c=24)
func(c=50, a=100)
