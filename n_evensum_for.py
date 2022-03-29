n=int(input())
s=0
i=2
for i in range(2,n,i):
	print(s,'+',i,'=',s+i)
	s+=i
	i+=1
print(s)