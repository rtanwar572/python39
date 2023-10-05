# multiplication of list elements by class(constructor)

class lis():
    def __init__(self,item):
        mult=1
        self.item=item
        list=(self.item).split()
        print("entered list is\n: ",list)
        for i in range(0,len(list)):
            mult=mult*int(list[i])
            print("multiplication of list ",i,"ele are: ",mult)
            
obj=lis(input("enter a list: "))
#bj.multi);
