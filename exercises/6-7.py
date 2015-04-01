#!/usr/bin/env python

# get a string from user
num_str = raw_input('Enter a number: ')

# turn string to int
num_num = int(num_str)

# a list 1 to num
non_fac_list = range(1, num_num+1)
print "BEFORE:", repr(non_fac_list)

# index
i = 0

result = []

# loop through non_fac_list
while i < len(non_fac_list):

    # check fac
    if num_num % non_fac_list[i] != 0:
        result.append(non_fac_list[i])

    #
    i = i + 1

#
print "AFTER:", repr(result)
