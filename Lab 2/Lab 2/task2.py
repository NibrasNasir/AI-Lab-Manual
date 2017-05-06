import math

def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def sub(x,y):
    return x-y

def div(x,y):
    return x/y

print ("Calculator")
print ("1. Addition")
print ("2. Multiplication")
print ("3. Subtraction")
print ("4. Division")

n = input("Enter choice:")

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

if n == '1':
    print (x , "+" , y, "=", add(x,y))

elif n == '2':
    print (x, "*" , y, '=', mul(x,y))

elif n == '3':
    print (x, '-',y,'=', sub(x,y))

elif n == '4':
    print (x, '/', y, '=', div(x,y))

else:
    print ("Invalid choice! Try Again.")




