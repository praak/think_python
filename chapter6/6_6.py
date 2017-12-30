# Palindrome

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

# Part 1:
# a = 'aaa'
# print a
# print 'first:  ' , first(a)
# print 'middle: ' , middle(a)
# print 'last:   ' , last(a)

# Part 2:
def is_palindrome(stringArg):
    if (first(stringArg) == last(stringArg)):
        # tests to check where in the code you are.
        # print 'here'
        # print middle(stringArg)
        if len(middle(stringArg)) > 1:
            # print 'inside middle check'
            value = is_palindrome(middle(stringArg))
        # print 'out of middle check'
        return True
    else:
        return False
# Change string a to anything to check if it is a Palindrome
# Pythons string comparison is ASCII, so it is case sensitive.
a = 'racecar'
isit = is_palindrome(a)
print 'Is',a, 'a Palindrome? [True/False]: ' , isit
