l=list(map(int,input().split()))
print("normal list:",l)
m=[ ]
for i in range(len(l)-1,-1,-1):
	m.append(l[i])
print("reversed list:",m)
