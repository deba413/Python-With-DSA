def fact(n):
    if n<0:
        return "does not exist"
    elif n==0:
        return 1
    else:
        return n*fact(n-1)
num=int(input("enter require number:  "))
print("the result is",fact(num))












































    


