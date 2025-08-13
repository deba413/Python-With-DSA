# x=[45,8,78,65,21,45,63,52,45,89]
# for i in range(0,len(x)):
#     for j in range(0,len(x)-1):
#         if x[j]>x[j+1]:
#             c=x[j]
#             x[j]=x[j+1]
#             x[j+1]=c
# print(x)


#User input:--

list=[]
n=int(input("enter the number of element: "))
print("Now enter all element one by one")
for i in range(0,n):
    ele=int(input())
    list.append(ele) 
def bubble(x):
    for i in range(0,len(x)):
        for j in range(0,len(x)-1):
            if x[j]>x[j+1]:
                c=x[j]
                x[j]=x[j+1]
                x[j+1]=c
bubble(list)
print("after sorting the list is: ", list)                