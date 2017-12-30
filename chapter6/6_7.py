# a is a power of b if it is divisible by b, and a/b is a power of b
# Write "is_power" Function

def is_power(num1,num2):
    if num1%num2 == 0:
        # print num1, ''
        # print num2, ''
        # print num1/num2
        # print'here \n'
        if num1/num2 != num2:
            vall = is_power(num1/num2,num2)
            #print 'not 2 :O '
        elif num1/num2 == num2:
            vall = True
            #print 'yolo'
        else:
            vall = False
        return vall
    else:
        #print 'we in here now?'
        vall = False
        return vall


value = ''
a = 27
b = 3
print 'Is %d power of %d?: ' %(a,b), is_power(a,b)
