# Taking a string as an argument and display the letters backward, one per line
# added the final backwards in between --

def backward(stringArg):
    index = 0
    new_ = ''
    print '--'
    while index < len(stringArg):
        new_ = new_ + stringArg[-1-index]
        print stringArg[-1-index]
        index = index + 1
        # print new_
    print '--'
    print new_
    print '--'

backward((raw_input('Enter a string to write backwards: ')))
