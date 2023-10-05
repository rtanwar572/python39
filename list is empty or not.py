class empty():
    
    def fun(self,list1):  
        self.list1=list1
        if(len(self.list1)==0):
            print("list is empty")
        else:
            print("list have ",len(list1),"ele: ")
            print("so givem list is: ",self.list1)
obj=empty()
obj.fun([2,3,4,5])
