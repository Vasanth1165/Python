from math import *
n=int(input())
count=0
f=0
for i in range(2,isqrt(n)+1):
	print(i)
	if(n%i==0):
		f+=1
		if f>0:
			break
	count += 1
if(f!=0):
	print('not a prime')
else:
	print('prime')
print(count)
	