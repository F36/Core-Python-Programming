one_to_nineteen = [None,'one','two','three','four','five','six','seven','eight',
                   'nine','ten','eleven','twelve','thirteen','fourteen',
                   'fifteen','sixteen','seventeen','eighteen']
twenty_to_ninety = [None,None,'twenty','thirty','forty','fifty','sixty',
                    'seventy','eighty','ninety']

value = raw_input('Enter a intger value between 0 and 1,000: ').strip()

result = ''

if len(value) == 3:
    result += one_to_nineteen[int(value[0])] + '-hundred'
    value = value[1:]
if len(value) == 2:
    if len(result) > 0:
        result += '-'
    if value > '19':
        result += twenty_to_ninety[int(value[0])]
        value = value[1:]
    else:
        result += one_to_nineteen[int(value)]
        del value
if len(value) == 1:
    if value != '0':
        if len(result) > 0:
            result += '-'
        result += one_to_nineteen[int(value)]

print result
