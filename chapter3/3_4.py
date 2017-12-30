# Part 1:
# def do_twice(f):
#     f()
#     f()
#
# def print_spam():
#     print 'spam'
#
# do_twice(print_spam)

# Part 2:
def do_twice(f,g):
    f(g)
    f(g)

def print_spam(arg1):
    print arg1

# do_twice(print_spam,4)

# Part 3:
def print_twice(stringArg):
    print stringArg
    print stringArg

# print_twice('Test')

# Part 4:
# do_twice(print_twice,'spam')

# Part 5:
def do_four(function, argValue):
    do_twice(print_twice,argValue)
    do_twice(print_twice,argValue)

do_four(do_twice,'Four')
