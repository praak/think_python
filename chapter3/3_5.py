# Part 1 & 2:
# Modified for any number of rows or cols based on input.

# Pseudo code for easier thinking
# A:
#     print '+ - - - - ',
#     check number of cols
#     Repeat until end of cols, then
#     print '+'
#     then
#     repeat 4 times
#         print '|         ',
#         check number of cols
#         repeat until end of cols, then
#         print '|'
#     check number of rows
#     if not end of rows repeat A
# print '+ - - - - ',
# check number of cols
# Repeat until end of cols, then
# print '+'

# To run call

def printSpace():
    print '         ',

def printPlus():
    print '+',

def printVerticalLine():
    print '|',

def verticleLinePrinting(f,g):
    f()
    g()

def horizontalLinePrinting(f):
    f()
    print ' - - - - ',


def boxIn(Vline):
    Vline(printVerticalLine,printSpace)
def boxOut(Hline):
    Hline(printPlus)

def printPattern(rows,cols):
    for numberofrows in range(0,rows):
        for horizontalLine in range(0,cols):
            boxOut(horizontalLinePrinting)
            # print'Hi'
        print'+'
        for rowsoflines in range(0,4):
            for linesgoingright in range(0,cols):
                boxIn(verticleLinePrinting)
            print'|'

    for endingline in range(0,cols):
        boxOut(horizontalLinePrinting)
        # print'Hi'
    print'+'

print('Box pattern design')
numOfRows = int(input('Enter number of Rows for box: '))
numOfCols = int(input('Enter number of Cols for box: '))
print('Pattern loading ... ')
print ''
printPattern(numOfRows,numOfCols)
print ''
