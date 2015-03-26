print '(a) All even numbers from 0 to 20:'
for num in range(21):
    if num % 2 == 0:
        print num,
print

print '(b) All odd numbers form 0 to 20:'
for num in range(21):
    if num % 2 != 0:
        print num,
print

print '(d) Determine if one number divides another.'
num1 = int(raw_input('Please enter a number:'))
num2 = int(raw_input('Please enter another number:'))

if num1 % num2 == 0 or num2 % num1 == 0:
    print True
else:
    print False
