r,c=map(int,input().split())
l=[]
for i in range(r):
    x=list(map(int,input().split()))
    l.append(x)
cornersum=l[0][0]+l[0][-1]+l[-1][0]+l[-1][-1]
print(cornersum)
colomsum=[]
for j in range(r):
    s=0
    for k in range(c):
        s+=l[k][j]
    colomsum.append(s)
print(colomsum)
d1=0
d2=0
for i in range(r):
    for j in range(c):
        if j==i:
            d1+=l[i][j]
        if i==r-j-1:
            d2+=l[i][j]
print(d1,d2)
rs=[]
for i in range(len(l)):
    rs.append(sum(l[i]))
print(rs)
