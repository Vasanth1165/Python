from math import *
def disarium(n):
	d=int(log10(n)+1)
	t=n
	s=0
	while n:
		r=n%10
		s+=r**d
		d-=1
		n=n//10
	return t==s
n=int(input())
if(disarium(n)):
	print('Disarium')
else:
	print('Not a Disarium')