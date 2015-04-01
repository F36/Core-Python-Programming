def grade(score):
    if score > 89:
        return 'A'
    elif score > 79:
        return 'B'
    elif score > 69:
        return 'C'
    elif score > 59:
        return 'D'
    else:
        return 'F'

scores = []

while True:
    score = int(raw_input('Enter a score, enter -1 to finish: '))
    if score == -1:
        break;
    scores.append(score)

for score in scores:
    print score, grade(score)

average = sum(scores) / float(len(scores))
print 'average socre:', average, grade(average)
