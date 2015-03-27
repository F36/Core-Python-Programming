openingBalance = float(raw_input('Enter opening balacne:'))
monthlyPayment = float(raw_input('Enter monthly payment:'))

months = int(openingBalance / monthlyPayment)
if openingBalance % monthlyPayment != 0:
    months += 1

widthForMont = len(str(months))
widthForPaid = max(5, len('%.2f' % monthlyPayment))
widthForBala = max(6, len('%.2f' % openingBalance))

print

print ' '*(widthForMont + 7),
print ' '*((widthForPaid - 5)/2) + 'Amount',
print ' '*(widthForPaid - (widthForPaid - 5)/2 - 3),
print ' '*((widthForBala - 6)/2) + 'Remaining'

print ' '*((widthForMont - 1)/2) + 'Pymt#',
print ' '*(widthForMont - (widthForMont - 1)/2 + 1),
print ' '*((widthForPaid - 5)/2) + ' Paid ',
print ' '*(widthForPaid - (widthForPaid - 5)/2 - 3),
print ' '*((widthForBala - 6)/2) + ' Balacne'

print '-'*(widthForMont + 4) + ' '*3,
print '-'*(widthForPaid + 1) + ' '*3,
print '-'*(widthForBala + 3)

print '  %*d     ' % (widthForMont, 0),
print '$%*.2f   ' % (widthForPaid, 0),
print ' $%*.2f' % (widthForBala, openingBalance)

bala = openingBalance
paid = monthlyPayment
for month in range(1, months + 1):
    paid = min(paid, bala)
    bala -= paid
    print '  %*d     ' % (widthForMont, month),
    print '$%*.2f   ' % (widthForPaid, paid),
    print ' $%*.2f' % (widthForBala, bala)
