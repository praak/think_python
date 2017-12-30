# Problem 1&2: Check if sides make a triangle.

triangle = 'Yes'
def is_triangle(side1,side2,side3,counter):
    if side1 > (side2+side3):
        print 'No'
        return
    elif counter > 0:
        is_triangle(side2,side3,side1,counter-1)
    else:
        print 'Yes'
        return

a = int(input('Enter side 1: '))
b = int(input('Enter side 2: '))
c = int(input('Enter side 3: '))
is_triangle(a,b,c,3)
print 'fin.'
