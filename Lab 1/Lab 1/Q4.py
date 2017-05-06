"Q 4"


x = input ("Type a sentence:\n")

y=z=0

for s in x:

    if s.isdigit():
        y=y+1
    elif s.isalpha():
        z=z+1


print("No. Of Digits are", y)
print ("No. Of Letters are", z)