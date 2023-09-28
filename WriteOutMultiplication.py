def WriteOutMultiplication(x,y):
    newStr = ""
    total = 0
    newStr += "\n" + (str("{:,}".format(x)) + " X " + str("{:,}".format(y)) + " = ") + "\n"
    for i in range(y):
        if i == 0:
            newStr += str("{:,}".format(x))
        else:
            newStr += " + " + str("{:,}".format(x))
        total += x
    newStr += " = " + str(total)
    return newStr

while True:
    firstNumber = int(input("Please type the first number that you want to multiply: "))
    secondNumber = int(input("Pleaser type what you would like to multiply your previous number by: "))
    print()
    print(WriteOutMultiplication(firstNumber, secondNumber))
    print()
