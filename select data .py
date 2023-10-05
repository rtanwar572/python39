class acc_info():
    def __init__(self,i):
    def select(self):
        i=input("enter name: ")
        if(i=="ayush"):
            print("\nwelcom to ayush info account: ")
            print("name:ayush\n age: 21\n salary: 32000")
        elif(i=="rohit"):
            print("\nwelcome to rohit info :")
            print("name: ",self.i)
        elif(i=="deepu"):
            print("\nwelcome to deepu info :")
            print("name: deepu\n age: 25\n salary: 42000")
        
        else:
             print("result not found ")

p1=acc_info()
p1.select()
