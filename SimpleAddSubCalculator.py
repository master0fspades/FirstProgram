
num1 = input("Hi! Please input a number here: ")
num2 = input("Please input another number here: ")
userChoice = input("Would you like to add, subtract, multiply, or divide these two numbers? ")

if userChoice == "add":
    result = float(num1) + float(num2)
    print(round(result))

if userChoice == "subtract":
    result = float(num1) - float(num2)
    print(round(result))

if userChoice == "multiply":
    result = float(num1) * float(num2)
    print(round(result))

if userChoice == "divide":
    result = float(num1) / float(num2)
    print(round(result))

input()

