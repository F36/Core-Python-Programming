def thing(s):
    if isinstance(s, str):
        while True:
            if len(s) > 0:
                if s[0] == ' ':
                    s = s[1:]
                else:
                    break
        while True:
            if len(s) > 0:
                if s[len(s) - 1] == ' ':
                    s = s[:len(s) - 1]
                else:
                    break
        return s

if __name__ == '__main__':
    print thing('     test   ')
    print thing(' t')
    print thing(6)
