def binary_search(list1,n):
    low=0
    high=len(list1)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if list1[mid]<n:
            low=mid+1
        elif list1[mid]>n:
            high=mid-1
        else:
            return mid
    return -1
list1=[23,25,45,89]
n=int(input("enter any number in list: "))
res=binary_search(list1,n)
if res !=-1:
    print(str(res))
else:
    print("element is not found in list")