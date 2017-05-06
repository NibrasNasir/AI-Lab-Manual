"Q 3"



x = int(input("Enter a year: "))

if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:

    print("\n Is a leap-year")

else:

    print("\n Is not a leap-year")
