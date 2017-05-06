x= int (input("Enter a number"))
x=x-1

l=[[0,0,0,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,1,1,0,0],[1,0,1,1,0]]

for z in range (0,5):
    p=l[x][z]
    if(p==1):
       print(z+1)
print ("are adjacent")


