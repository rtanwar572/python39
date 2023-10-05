#leap yaear
a=int(input("enter year "))
if(a%4==0 and a%100==0 and a%400==0):
    print("is a leap year")
elif(a%4==0):    
    if(a%100==0 and a%400==0):
        print("is a leap year ")
    else:
        print("not a leap year")
else:
    print("not a leap year")
