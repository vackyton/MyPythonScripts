type = input ("Enter Method (/ for div, * for x, + to add, - to subtract): ")

num1 = input("First Number: ")
num2 = input("Second Number: ")

if type == "/":
    print(float(num1) / float(num2))

if type == "*":
    print(float(num1) * float(num2))

if type == "+":
    print(float(num1) + float(num2))

if type == "-":
    print(float(num1) - float(num2))
