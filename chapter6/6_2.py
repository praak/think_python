# hypotenuse : returns the lenght of the hypotenuse of a right triangle given lenghts of two legs
# Hint: Test with 3 and 4 as the base and adjacent values, hypotenuse should be 5. (3,4,5 triangle)
import math

def find_hypotenuse(leg1, leg2):
    sumsquare = (leg1 ** 2 + leg2 ** 2)
    hypotenuse = math.sqrt(sumsquare)
    return hypotenuse

print 'Finding hypotenuse.. '
base = float(input('Enter base lenght: '))
adjacent = float(input('Enter adjacent lenght: '))
hypoteuse  = find_hypotenuse(base,adjacent)
print 'Hypotenuse is : ', hypoteuse
