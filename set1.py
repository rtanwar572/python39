x=[2,3,4,5]
y=[2,3,4,7,8]
for i in x:
    for j in y:
        if(i==j):
            print("",j)
            break
    print(j==i," is repeat")

print("given list are ",x,y)
