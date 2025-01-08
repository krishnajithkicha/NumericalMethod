def BinarySearch(Lb,Ub,key,A):
    if Lb<=Ub:
        mid=(Lb+Ub)//2
        if A[mid]<key:
            return BinarySearch(mid+1,Ub,key,A)
        elif A[mid]>key:
            return BinarySearch(Lb,mid-1,key,A)
        elif A[mid]==key:
            return mid
    return -1
n=int(input("Enter the number of elements:"))
print("Enter the elements:")
A=list()
for i in range(n):
        num=int(input())
        A.append(num)
s=int(input("Enter the element to search:"))
m=BinarySearch(0,n-1,s,A)
if m==-1:
     print("Element not found")
else:
     print("Element found at",m)
