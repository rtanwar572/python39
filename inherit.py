class men():
    def fun(self):
        x=45000
        y="rohit"
        print("name: ",y,"salary: ",x)
class women(men):
    def mjak(self):
        x=23
        y="ayush"
        print("name of student : ",y,"roll no: ",x)
class b(women):
    def jok(self):
        self.x=22
        self.y="deepu"
        print("name of student : ",self.y,"roll no: ",self.x)
obj=b()
obj.jok()
        
