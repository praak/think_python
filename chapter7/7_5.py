# Estimation of pi
# Use of algorithms

import math
from math import factorial as fact


def estimate_pi():
    summation = 0.0
    epsilon = 1e-25
    new = 1.0
    counter = 0.0
    while new > epsilon:
        numerator = (fact(4.0*counter) * (1103.0 + (26390.0 * counter)))
        denmominator = (((fact(counter))**4.0) * (396.0**(4.0*counter)))
        new = numerator/denmominator
        print 'new: ' , new
        summation = summation + new
        print 'sum: ' , summation
        counter = counter + 1

    summation = (((2.0 * math.sqrt(2))) / (9801.0)) * summation

    print 'Algorithm: %f \nMath.pi: %f' %(summation,1/math.pi)

estimate_pi()
