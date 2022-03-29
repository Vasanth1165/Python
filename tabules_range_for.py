a,b,r=map(int,input().split())
for i in range(a,b+1):
	for j in range(1,r+1):
		print(i,'*',j,'=',i*j)
	print()