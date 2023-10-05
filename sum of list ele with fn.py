# addition of list elements by class(constructor):

class lis():
    
    def fun(self,item):
        sum=0
        self.item=item
        list=(self.item).split()
        print(list)
        for i in range(0,len(list)):
            sum=sum+int(list[i])
            
            print("sum of list ",i, "is: ",sum)
obj=lis();
obj.fun(input("enter a list: "))        
