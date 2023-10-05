# 1st way to sort the dirt by key
x=dict({3:"rr",2:"oo",4:"hh",5:"ii",1:"tt"})
for i in sorted(x.keys()):
    print(i,end=" ")
for j in sorted(x.values()):
    print(j,end=" ")

