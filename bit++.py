n = int(input())
y = 0
for i in range(0,n):
    x = str(input())
    if (x=="++X"):
        y = y+1
    elif (x=="X++"):
        y = y+1
    elif (x=="X--"):
        y = y-1
    elif (x=="--X"):
        y = y-1
    

print(y)