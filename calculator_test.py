def calculator(num1=1,oper="+", num2=1):
    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2

    else:
        try:
            return num1 / num2
        except ZeroDivisionError as err:
            print(err)


print(calculator(4, "/", 0))
