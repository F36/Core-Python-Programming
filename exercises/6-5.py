string = raw_input('Enter a string: ')

# (a)
rstring = string[::-1]
for char in string:
    print char,
print
for char in rstring:
    print char,
print

# (b)
string2 = raw_input('Enter another string: ')
if len(string) == len(string2):
    for index in range(len(string)):
        if string[index] != string2[index]:
            print "Don't match."
            break
    else:
        print '2 strings matched!'
else:
    print "Don't match"

# (c)
string = raw_input('Enter a string: ')
rstring = string[::-1]
for index in range(len(string)):
    if string[index] != rstring[index]:
        print 'This string is not palindromic'
        break
else:
    print 'This string is palindromic'

# (d)
print string + rstring
