n=int(input())
s=0
i=2
for i in range(2,n*2+1,i):
	print(s,'+',i,'=',s+i)
	s+=i
	i+=2
print(s)
	
	