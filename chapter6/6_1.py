# compare funciton that returns 1 if x > y, 0 if x == y and -1 if x < y

def compare(x,y):
    if x > y:
        print 'First value > Second'
        return 1
    elif x == y:
        print 'They are the same value'
        return 0
    elif x < y:
        print 'First value < Second'
        return -1
    else:
        print 'none'
        return 'Nope'

print 'Comparing two values:'
value1 = float(input('Enter first value: '))
value2 = float(input('Enter second value: '))
value = compare(value1,value2)
print 'The return value is: ', value , '\n'
