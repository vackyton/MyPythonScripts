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
type = input ("Enter Method (/ for div, * for x, + to add, - to subtract): ")

num1 = input("First Number: ")
num2 = input("Second Number: ")
morenum = input('do you want more numbers? If yes how many?(limit 5 numbers)(type n for no): ')

if morenum == "n":
    if type == "/":
        print(float(num1) / float(num2))

    if type == "*":
        print(float(num1) * float(num2))

    if type == "+":
        print(float(num1) + float(num2))

    if type == "-":
        print(float(num1) - float(num2))

if morenum == 3:
    num3 = input('Enter third number')
    if type == "/":
        print(float(num1) / float(num2) / float(num3))

    if type == "*":
        print(float(num1) * float(num2) * float(num3))

    if type == "+":
        print(float(num1) + float(num2) + float(num3))

    if type == "-":
        print(float(num1) - float(num2) - float(num3))

if morenum == 4:
    num3 = input('Enter third number')
    num4 = input('Enter third number')
    if type == "/":
        print(float(num1) / float(num2) / float(num3) / float(num4))

    if type == "*":
        print(float(num1) * float(num2) * float(num3) * float(num4))

    if type == "+":
        print(float(num1) + float(num2) + float(num3) + float(num4))

    if type == "-":
        print(float(num1) - float(num2) - float(num3) - float(num4))

if morenum == 5:
    num3 = input('Enter third number')
    num4 = input('Enter third number')
    num5 = input('Enter third number')
    if type == "/":
        print(float(num1) / float(num2) / float(num3) / float(num4) / float(num5))

    if type == "*":
        print(float(num1) * float(num2) * float(num3) * float(num4) * float(num5))

    if type == "+":
        print(float(num1) + float(num2) - float(num3) - float(num4)  - float(num5))

    if type == "-":
        print(float(num1) - float(num2) - float(num3) - float(num4)  - float(num5))

close = input('Press Enter to close ')
