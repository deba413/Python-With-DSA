n = [12, 45, 78, 65, 89, 65]
item = int(input("enter element: "))
index = len(n)
for i in range(0, index):
    if (n[i] == item):
        index = i
        # if (item==index):
        print("Element is founded at index",index)
    else:
        print("not found")
            
    #     print("element is found at index",index)
    #     break
    # else:
    #     print("element is not found")
    #     break
# if (index==-1):
#     print("Element not found")    
# else:
#     print("Element is founded at index",index)



# def linear_search(list1,n,key):
#     for i in range(0,n):
#         if(list1[i]==key):
#             return i
#     return -1
# list1=[1,5,6,3,7,8]
# key=int(input("enter element: "))
# n=len(list1)
# res=linear_search(list1,n,key)
# if(res==-1):
#     print("Element not found")
# else:
#     print("elment is founded at index: ",res) 
