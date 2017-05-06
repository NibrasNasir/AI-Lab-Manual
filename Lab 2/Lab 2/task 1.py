import math
n = int(input("Enter a value"))
z = {}
for i in range(n+1):
    z[i] = math.sqrt(i)

print (z)