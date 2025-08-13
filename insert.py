n=int(input("enter the new element:   "))
p=int(input("enter the position:  "))
def insert():
    a=[4,325,6,24,25,28,28]
    for i in range(0,a):
        if(i>=p):
            a[i+1]=a[i]
        elif(i==p):
            a[i]=n
       
print(insert)