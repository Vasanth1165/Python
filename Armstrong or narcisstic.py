n=int(input())
t=n
m=n
dc=0
while(n):
	dc+=1
	n=n//10
sum=0
while(t):
	r=t%10
	sum=sum+r**dc
	t=t//10
if(sum==m):
	print('armstrong num')
else:
	print('not an armstrong num')