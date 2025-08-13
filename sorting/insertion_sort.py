# 
# Statik:--
# 
# x=[21,45,6,78,24]
# for i in range(1, len(x)):
#     while (i>0 and x[i]<x[i-1]):
#         a=x[i]
#         x[i]=x[i-1]
#         x[i-1]=a
#         i=i-1
# print(x)


#user input:--

list=[]
n=int(input("enter the number of element: "))
print("Now enter all element one by one")
for i in range(0,n):
    ele=int(input())
    list.append(ele)            
def inser(x):
    for i in range(1, len(x)):
        while (i>0 and x[i]<x[i-1]):
            a=x[i]
            x[i]=x[i-1]
            x[i-1]=a
            i=i-1
inser(list)
print("after sorting the list is: ", list)
