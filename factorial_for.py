n=int(input())
f=1
for i in range(n,0,-1):
	print(f,'*',i,'=',f*i)
	f=f*i
print(f)