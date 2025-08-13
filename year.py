n=int(input("Enter any year:  "))
if n%100==0:
    if n%400==0:
        print(n,"the year is leap year")
    else:
        print(n,"year is not leap year")
else:       
    if n%4==0:
        print(n,"year is leap year")  
    else:
        print(n,"the year is not leap year")     

