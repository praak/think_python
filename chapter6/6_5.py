# Ackermanns funciton
# input only takes values convertable to int. floats will be rooted.
def ack(m,n):
    if m == 0:
        return n+1
    elif m>0 and n==0:
        result = ack(m-1,1)
        return result
    elif m>0 and n>0:
        result = ack(m-1,ack(m,n-1))
        return result

print 'Ackermanns Function: '
value1 = int(input('Enter value1: '))
value2 = int(input('Enter value2: '))

print 'Ackermanns result is : ' , ack(value1,value2)
