# to find greatest no in a list by using class(constructor):

item=input("enter a list: ")
list=item.split()
print("entered list is: ",list)

list.sort()
print("sorted list is: ",list)
for i in range(0,len(list)):
    print("greater no is:",list[len(list)-1])
    break;

