def atoc(string):
    length = len(string)
    for index in range(length)[::-1]:
        if index > 0:
            if string[index] in ['+', '-']\
            and string[index - 1] not in ['e', 'E']:
                break
    else:
        if 'j' in string or 'J' in string:
            return complex(0, float(string[0:length-1]))
        else:
            return complex(float(string), 0)
    real = float(string[0:index])
    imag = float(string[index:length-1])
    return complex(real, imag)

if __name__ == '__main__':
    print atoc('-1.23e+4-5.67j')
    print atoc('12345')
    print atoc('+123e-5')
    print type(atoc('533j'))
