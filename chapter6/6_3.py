# is between

def is_between(x,y,z):
    return (x <= y and y <= z)

print 'Check if value is inbetween:'
a = float(input('Enter first value: '))
b = float(input('Enter second value (middle value): '))
c = float(input('Enter third value: \n'))

print 'Second value is inbetween the other two is a ' , is_between(a,b,c) , 'statement. \n'
