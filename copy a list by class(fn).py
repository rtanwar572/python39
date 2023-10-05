# copy a list in another list:
class cop():
    def fun(self):
        n=int(input("enter no of times copy : "))
        self.a=input("enter a list: ")
        list=(self.a).split()
        b=[]
        #set1=set(list)
        for i in range(0,n):
            b.append(self.a)
        print("after cpy : ",b)
obj=cop()
obj.fun()
    
