
# Hello and welcome to my project : simplecalculator. This simple calculator was made by 4zuj
# At the start a friendly greeting, because why not right?

print("Welcome to the calculator!")

# Here is the code asking for the Numbers that should be used to calculate.

a = int(input("Tell me a Number you want to use to calculate something : "))
b = int(input("Tell me a second Number you want to calculate the other Number with : "))

# Now the code is going to ask the user what Operator he wants to use.

print("Great! What Operator do you want to use to calculate?")
op = input("+, -, *, /? : ")

# This is the system how the 2 Numbers get calculated with the additional operator the user selected.

if op == "+":
    print("Your result is : ",a+b)

if op == "-":
    print("Your result is : ",a-b)

if op == "*":
    print("Your result is : ",a*b)

if op == "/":
    if a == 0:
        print("Error")
    if b == 0:
        print("Error")
    else:
        print("Your result is : ",a/b)

# A little exit function because I like things to be fancy.

input("Press ENTER to exit.")