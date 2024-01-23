Num1 = float(input("enter first number "))
Num2 = float(input("enter the second number "))
operation = input("choose an operation  (-, +, *, %, **, /) ")
match operation:
    case "+":
        print(Num1 + Num2)
    case "-":
        print(Num1 - Num2)
    case "*":
        print(Num1 * Num2)
    case "/":
        if Num2 == 0:
            print("Cant devide zero")
        else:
            print(Num1 / Num2)
    case "%":
        print(Num1 % Num2)
    case "**":
        print(Num1 ** Num2)
    case _:
        print("error")

