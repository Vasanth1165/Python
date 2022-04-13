n=int(input())
t=n
e_count=0
o_count=0
while(n):
	r=n%10
	if(r%2==0):
		e_count+=1
	else:
		o_count+=1
	n=n//10
print('there are',e_count,'even number(s)',o_count,'odd numbers(s)','in',t)