n=int(input())
for i in range(1,13):
	if(i%3==0):
		continue
	print(n,'*',i,'=',n*i)