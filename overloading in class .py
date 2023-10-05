class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print("Area of Rectangle:",(a*b))
        elif a!=None:
            print("Area of square:",(a*a))
        else:
            return 0;
obj1=Area()
print("area is = ",obj1.find_area())
print("enter for finding area of :(a*a) \n")
obj1.find_area(int(input("enter a no = ")))
print("enter for finding area of Rectangle: (a*b)\n")
obj1.find_area(int(input("enter 1st no = ")),int(input("enter 1st no = ")))
