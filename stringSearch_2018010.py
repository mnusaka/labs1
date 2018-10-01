def FindMultipleOccurrence (s1, s2, numX):
    y=s1[0]
    n=ord('y')
    if((n>=65 and n<=90) or (n>=97 and n<=122)):
        x2=s2.lower()
        x1=s1.lower()
        if(x2[0:len(s1)]==x1 and s2[0:1].isupper()==True):
            z=int(x2.count(x1))
        else:
            z=int(s2.count(s1))-1
    if(z>=numX):
        return True
    else:
        return False
s1=input('input string 1 :',)
s2=input('input string 2 :',)
numX=int(input('according to you number of times string 1 occurs in string 2 :',))
print('output is :',FindMultipleOccurrence(s1, s2, numX))
