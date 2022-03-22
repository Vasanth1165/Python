#linear search
arr=[int(i) for i in input().split()]
target=int(input())
temp=False
for i in range(len(arr)):
    if arr[i]==target:
        temp=True
        break
if(temp):
    print("element found")
else:
    print("element not found")
