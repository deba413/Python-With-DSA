def odd(l,r):
    if(r<r):
        return
    if(r%2==1):
        odd(l,r-2)
    else:
        odd(l,r-1)
    if(r%2==1):
        print(r,end="")
#l=10
#r=20
print("odd: ",odd(10,20))
        

