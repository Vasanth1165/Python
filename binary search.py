#binary search
arr=[int(i) for i in input().split()]
target=int(input())
low=0
high=len(arr)-1
while(low<=high):
    mid=(low+high)>>1
    if arr[mid]==target:
        print(mid)
        break
    elif arr[mid]>target:
        high=mid-1
    else:
        low=mid+1
else:
    print("Not found")
    

    
