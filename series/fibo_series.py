n=int(input("enter the numbers of terms: "))
f=0
s=1
for i in range(0,n):
    print(f)
    fibo=f+s
    f=s
    s=fibo

