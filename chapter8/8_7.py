# number of "a"'s in bananas
word = 'bananas'
print word.count('a')

print '-'
print 'Now the debugging section: .. '
# is_reverse : function fixed , had two errors in the book from section 8.11 Debugging. (book asked to fix the bugs)
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i=0
    j = len(word2)-1
    while j > -1:
        # print i,j
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    # print 'out of loop'
    return True

print is_reverse('pots','stop')
