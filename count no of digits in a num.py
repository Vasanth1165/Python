n=int(input())
count=0
while(n):
	r=n%10
	count+=1
	n=n//10
print(count)