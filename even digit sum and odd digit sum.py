n=int(input())
t=n
e_sum=0
o_sum=0
while(n):
	r=n%10
	if(r%2==0):
		e_sum+=r
	else:
		o_sum+=r
	n=n//10
print("even digit sum",e_sum)
print("odd digit sum",o_sum)