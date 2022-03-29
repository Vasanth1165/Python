a,b=map(int,input().split())
for i in range(a,b+1):
	print(i,' tabules upto?')
	r=int(input())
	for j in range(1,r+1):
		print(i,'*',j,'=',i*j)
	print('done!')
	print()
	