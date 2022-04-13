a,b=map(int,input().split())
bc=0
t=b
while(b):
	b=b//10
	bc+=1
r=a*10**bc+t
print(r)
print(r*r)
print(r**3)
	