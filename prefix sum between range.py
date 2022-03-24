n=int(input())
s,e=map(int,input().split())
arr=list(map(int,input().split()))
pre=[]
pre.append(arr[0])
for i in range(1,n):
    pre.append(pre[i-1]+arr[i])
if s==0:
    print(pre[e])
else:
    print(pre[e]-pre[s-1])
