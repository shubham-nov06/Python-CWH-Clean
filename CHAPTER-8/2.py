def calclutaor():
    num1 = int(input("Enter your number = "))
    num2 = int(input("Enter your number = "))

    operator = input("Enter your operation = ")
    if operator == "*":
        print("Multiplication is = ", num1 * num2)
    elif operator == "%":
        print("Remainder is = ", num1 % num2)
calclutaor()
