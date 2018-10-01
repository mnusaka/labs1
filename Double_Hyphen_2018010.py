# Hyphenator_broken.py
# the CS 1110 profs (cs-1110profs-L@cornell.edu)
# Feb 2016

""" Inserts hyphens into a non-empty odd-length input string as follows:
A hyphen is inserted on either side of the middle character.

Example: "abcde" becomes "ab-c-de"

"""
### This program intentionally has at least one error in it!

s = input('Enter an odd-length string: ')

n = len(s)
print ('n is',n)
if n==0 or n%2==0:
    print('invalid input')
elif n==1:
    print ('string length 1')
else:
    m = int(n/2)
    print ('m is',m)
    first = s[0:m]
    print ('first is',first)
    middle = s[m]
    print ('middle is',middle)
    second = s[m+1:]
    print ('second is',second)
    h = first+'-'+middle+'-'+second
    # final output
    print (s,'becomes',h)
