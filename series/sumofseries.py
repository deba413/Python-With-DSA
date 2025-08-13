def fact(n):
    f=1
    if n==0:
        return 1
    
    else:
        for i in range(1,n+1):
            f=f*i
        return f
x=int(input("Enter number of terms: "))            
sum=0
if x<0:
    print("please enter a positive number")
else:
    for i in range(1,x+1):
        if i%2==0:
            sum=sum-i/fact(i)
        else:
            sum=sum+i/fact(i)
print("The requierd sum is: ",sum)                    