n=int(input())
sum=0
count=0
while(n):
	r=n%10
	sum+=r
	count+=1
	n=n//10
avg=sum/count
print('average is',sum,'/',count,'=',avg)