def add():
    n=int(input("enter no. of elements: "))
    #tuple=();
    list=[]
    for i in range(0,n):
        a=int(input("enter list: "))
        list.append(a)
    print("the given list is:\n",list)
add();
def men():
    n=int(input("enter no. of elements: "))
    #tuple=();
    list=[]
    for i in range(0,n):
        a=int(input("enter tuple ele: "))
        list.append(a)
        tuple1=tuple(list)
    print(tuple1)
men();

