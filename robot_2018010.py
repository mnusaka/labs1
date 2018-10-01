print('do you want to give specific coordinates? (y/n)')
x=input()
if(x=='n'):
	x1=0
	y1=0
else:
	x1=input('starting point x coordinate: ',)
	y1=input('starting point y coordinate: ',)
a=input('input direction and number of steps: it will not be considerd as a step').split()
while a[0]!='STOP':
	a=input('input direction and number of steps: ').split()
	if(a[0]=='RIGHT'):
		n=1
		x1=int(x1)+int(n*int(a[1]))
	elif(a[0]=='LEFT'):
		n=-1
		x1=int(x1)+int(n*int(a[1]))
	elif(a[0]=='UP'):
		n=1
		y1=int(y1)+int(n*int(a[1]))
	elif(a[0]=='DOWN'):
		n=-1
		y1=int(y1)+int(n*int(a[1]))
	elif(a[0]=='STOP'):
		print('initial coordinates are',x1 ,y1)
		print('POSITION IS',x1 ,y1)
	else:
		print('wrong input. please give correct input of form UP 2')



