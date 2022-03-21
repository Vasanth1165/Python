a=int(input ())
b=int(input ())
c=int(input ())
d=int(input ())
if(a>=b and a>=c and a>=d):
	print('a is greater')
elif(b>=c and b>=d):
	print('b is greater')
elif(c>=d):
	print('c is greater')
else:
	print('d is greater')