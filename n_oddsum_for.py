n=int(input())
s=0
i=2
for i in range(1,n+1,i):
	print(s,'+',i,'=',s+i)
	s+=i
	i+=1
print(s)