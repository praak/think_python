# Modify find function to start at a given index

def find(word, letter, searchIndex):
    while searchIndex < len(word):
        if word[searchIndex] == letter:
            return searchIndex
        searchIndex = searchIndex+ 1
    return -1
