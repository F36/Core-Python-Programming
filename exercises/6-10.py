def case_inverted(input):
    output = ''
    for char in input:
        if char.isalpha():
            if char.islower():
                output += char.upper()
            else:
                output += char.lower()
        else:
            output += char
    return output

if __name__ == '__main__':
    print 'Test function:'
    print 'Mr. Ed'
    print case_inverted('Mr. Ed')
