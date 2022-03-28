l=list(map(int,input().split()))
print("normal list:",l)
n=len(l)
for i in range(n//2):
	l[i],l[n-i-1]=l[n-i-1],l[i]
print("reversed list:",l)