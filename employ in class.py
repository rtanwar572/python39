class men():
    emp_count=0
    def __init__(self,a,b):
        self.a=a
        self.b=b
        men.emp_count +=1
    def fun(self):
        print("name: ",self.a,"\nage: ",self.b)
p1=men("rohit",19)
p2=men("ayush",20)
p3=men("deepu",25)
p1.fun()
p2.fun()
p3.fun()
print("total no. of employ's are : ",men.emp_count)
