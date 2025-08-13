# list1=[21,45,6,78,24]
# def selection(data):
#     n=len(list1)
#     swapped = False
#     for i in range(n-1):
#         minId=i
#         for j in range(0,n-i-1):
#             if(data[i]<data[minId]):
#                 minId=j

#         temp=data[minId]
#         data[minId]=data[i]
#         data[i]=temp        




# selection(list1)
# print(list1)
# for i in range(len(list1)):
# 	print("% d" % list1[i], end=" ")


list=[]
n=int(input("enter the element: "))
print("Now enter element one by one")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
def selection(x):
    for i in range(0,len(x)-1):
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                temp=x[i]
                x[i]=x[j]
                x[j]=temp
selection(list)
print("after sorting the list is: ", list)