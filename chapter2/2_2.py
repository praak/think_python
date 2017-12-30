width = 17
height = 12.0
delimiter = '.'

def run(num,a,b=0,c=''):
    if num == 1:
        return a/2
    elif num == 2:
        return a/2.0
    elif num == 3:
        return b/3
    elif num == 4:
        return 1+2*5
    else:
        return c * 5
for num in range(0,6):
    print run(num,width,height,delimiter)
