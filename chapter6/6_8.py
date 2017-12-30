# GCD (Greatest common divisor)
# Test: 2313 and 1233 -> GCD = 9
def gcd(num1,num2):
    if num1>num2:
        # print 'num1>num2'
        if num2 == 0:
            # print 'num2 = 0'
            value = num1
            return value
        else:
            r = num1%num2
            # print 'r=', r
            value = gcd(num2,r)
            return value
    elif num1 == num2:
        value = num1
        return value
    else:
        value = gcd(num2,num1)
        return value

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

print 'The GCD of' , a, 'and', b , 'is :' ,gcd(a,b)
