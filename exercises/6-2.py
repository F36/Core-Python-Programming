#!/usr/bin/env python

import string
import keyword

alphas = string.ascii_letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v2.0'
myInput = raw_input('Identifier to test? ')

if len(myInput) > 0:
    if myInput[0] not in alphas:
        print 'invalid: first symbol must be alphabetic'
    else:
        if len(myInput) > 1:
            for otherChar in myInput[1:]:
                if otherChar not in alphas + nums:
                    print 'invalid: remaining symbols must be alphanumeric'
                    break
        if myInput in keyword.kwlist:
            print 'Error: keyword name'
        else:
            print 'okey as an Identifier'
