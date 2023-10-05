class remov():
        def fun(self):
                self.item=(input("enter a list: "))
                list=(self.item).split()
                list2=[]
                for i in list:
                        if i not in list2:
                                list2.append(i)
                                print("list is: ",list2)
                        
                            
                        
                        
                        else:
                                print("duplicate element is: ",i)
                                print(" ")
                            #print("list is :",list2)
                                       

obj=remov()
obj.fun()
                                    

