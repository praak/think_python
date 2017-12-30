def right_justify(something):
    lenghtOfString = len(something)
    spaceValue = 70 - lenghtOfString
    space = " "
    for x in range(0,spaceValue-1):
        space = space + " "
    finalString = space + something
    return finalString

#use of raw_input was necessary for getting the verbatim use of input
wordToPrint = raw_input('Enter what to print: ')
finalString = right_justify(wordToPrint)
print finalString
