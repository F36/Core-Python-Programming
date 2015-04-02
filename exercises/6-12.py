# (a)
def findchr(string, char):
    for index in range(len(string)):
        if string[index] == char:
            break
    else:
        index = -1
    return index

# (b)
def rfindchr(string, char):
    for index in range(len(string) - 1, -1, -1):
        if string[index] == char:
            break
    else:
        index = -1
    return index

# (c)
def subchr(string, origchar, newchar):
    newstring = ''
    for char in string:
        if char == origchar:
            newstring += newchar
        else:
            newstring += char
    return newstring

if __name__ == "__main__":
    teststring = 'this is a test.'
    print findchr(teststring, 'i')
    print findchr(teststring, 'b')
    print rfindchr(teststring, 'i')
    print rfindchr(teststring, 'b')
    print subchr(teststring, 'i', 'b')
    print subchr(teststring, 'b', 'i')
