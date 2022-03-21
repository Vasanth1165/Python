a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
	print('a is greater')
elif(b>a and b>c):
	print('b is greater')
elif(c>a and c>b):
	print('c is greater')
else:
	print('all are equal')