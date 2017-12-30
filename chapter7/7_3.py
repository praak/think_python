import math

def test_square_root(squareOf,secondNum):
    epsilon = 0.000001
    inBuiltFn = math.sqrt(squareOf)
    x = secondNum

    while True:
        y = (x + squareOf/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y

    print 'Number    \t Inbuilt    \t Algorithm    \t Difference'
    print '%.4f \t %.4f \t %.4f \t %.4f' %(squareOf, inBuiltFn, y, abs(inBuiltFn-y))

test_square_root(16.0,16.0-1)
