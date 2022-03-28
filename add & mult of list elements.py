l=list(map(int,input().split()))
s=0
m=1
for i in range(len(l)):
	s=s+l[i]
	m=m*l[i]
print(s)
print(m)