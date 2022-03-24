n=int(input())
arr=list(map(int,input().split()))
pre=[]
pre.append(arr[0])
for i in range(1,n):
    pre.append(pre[i-1]+arr[i])
print(pre)
