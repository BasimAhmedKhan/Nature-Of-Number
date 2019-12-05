print(" ")
print('"To Check Whether The Number Is Even/Odd!"')
print(" ")

num1 = int(input("Enter Your Number: "))

if num1 / 2 == int(num1 / 2):
    print("Even Number")
elif num1 / 2 == float(num1 / 2):
    print("Odd Number")
else:
    print("Invalid Input")