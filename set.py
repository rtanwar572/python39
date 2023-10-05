#remove duplicate elements in list/set

"""def stet():
        set.pop()
        print(set)
set={3,2,4,5,6}
for i in range(len(set)):
    stet();"""
set={3,2,5,6,4}
list(set).sort()
print(set)
x=len(set)
print(x)
print("largest ele is : ",list[x-1])