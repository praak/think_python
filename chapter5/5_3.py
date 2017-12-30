import sys
# use of sys.argv , on terminal need to pass values for the check_fermat. 

# Fermats last theorem says that there are no positive integers a,b, and c such that
# a^n + b^n = c^n
# for any values of n greater than 2

# Problem 1:

def check_fermat(a,b,c,n):
    if n>2 and (a**n + b**n == c**n):
        print"Holy smokes, Fermat was wrong!"
    else:
        print"No, that doesnt work"

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])

check_fermat(a,b,c,d)
