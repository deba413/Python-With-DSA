def fact(x):
    f=1
    if x==0:
        return 1
    else:
        for i in range(1,x+1):
            f=f+i
        return f
n=int(input("Enter the number of terms: "))
sum=0
if n<0:
    print("Please enter posiitve number")
else:
    for i in range(1,n+1):
        if i%2==0:
            sum=sum-i/fact(i)
        else:
            sum=sum+i/fact(i)
print(sum)                                     