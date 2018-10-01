def sum(a,n):
	s=0
	if(a<0 or n<0):
		return('INV')
	else:
		for i in range(1,n+1):
			a=str(a)
			x=int(a*i)
			s=s+x
		return(s)
a=int(input('a= ',))
n=int(input('n= ',))
print('output is :',sum(a,n))

	









