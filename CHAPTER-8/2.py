def calclutaor():
    for i in range(2):
        num1 = int(input("Enter your number = "))
        num2 = int(input("Enter your number = "))

        operator = input("Enter your operation = ")
        if operator == "*":
            print("Multiplication is = ", num1 * num2)
        elif operator == "%":
            print("Remainder is = ", num1 % num2)
        elif operator == "+":
            print("Sum is = ", num1 + num2)
        elif operator == "-":
            print("Subtraction is ", num1 - num2)


calclutaor()
