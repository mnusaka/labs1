def hexfun(s):
	num=0
	for i in range(len(s)):
		if s[i]=='1':
			num+=1*(16**(len(s)-i-1))
		elif s[i]=='2':
			num+=2*(16**(len(s)-i-1))
		elif s[i]=='3':
			num+=3*(16**(len(s)-i-1))
		elif s[i]=='4':
			num+=4*(16**(len(s)-i-1))
		elif s[i]=='5':
			num+=5*(16**(len(s)-i-1))
		elif s[i]=='6':
			num+=6*(16**(len(s)-i-1))
		elif s[i]=='7':
			num+=7*(16**(len(s)-i-1))
		elif s[i]=='8':
			num+=8*(16**(len(s)-i-1))
		elif s[i]=='9':
			num+=9*(16**(len(s)-i-1))
		elif s[i]=='a' or s[i]=='A':
			num+=10*(16**(len(s)-i-1))
		elif s[i]=='b' or s[i]=='B':
			num+=11*(16**(len(s)-i-1))
		elif s[i]=='c' or s[i]=='C':
			num+=12*(16**(len(s)-i-1))
		elif s[i]=='d' or s[i]=='D':
			num+=13*(16**(len(s)-i-1))
		elif s[i]=='e' or s[i]=='E':
			num+=14*(16**(len(s)-i-1))
		elif s[i]=='f' or s[i]=='F':
			num+=15*(16**(len(s)-i-1))
	return num
def hexmod5(num):
	q=int((num-num%5)/5)
	return q
def tohex(q):
	a=[]
	while q>=1:
		a.append(str(q%16))
		q=q//16	
	a.reverse()
	a= ''.join(a)
	return(a)
s=input('type a hexadecimal number',)
q=print('number in decimal is ',hexfun(s))
R=print('quotient is',tohex(hexmod5(hexfun(s))))
