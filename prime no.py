n=int(input("enter a no = "))
if(n>1):
for i in range(2,n):
    if(n%i)==0:
        #n//i==0
        print(" is not prime no ",n)
        break
    else:
        print(" a prime no ")
#else:
#    print("not prime no ")
