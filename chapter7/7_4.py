import math

# Using "eval" function on a loop to check different python functions and variable types.
#evaluate things. :)

def eval_loop():
    print 'type "done" to end loop'
    while True:
        print '>',
        userInput = raw_input()
        if userInput == 'done':
            break
        print eval(userInput)

eval_loop()
