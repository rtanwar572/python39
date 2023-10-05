class men():
    def __init__(self,a,b):
        self.a=a
        self.b=b        
    def add(self):
        print("add of two no. is = ",self.a+self.b)
    def sub(self):
        print("sub of two no. is = ",self.a-self.b)
    def mult(self):
        print("mult of two no. is = ",self.a*self.b)
p1=men(int(input("enter 1st no. =")),int(input("enter 2nd no. =")))
p1.add()
p1.sub()
p1.mult()
