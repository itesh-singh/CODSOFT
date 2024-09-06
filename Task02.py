def calculator():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    op = input("Operation (+, -, *, /): ")

    if op == "+":
        print(f"Result: {num1 + num2}")
    elif op == "-":
        print(f"Result: {num1 - num2}")
    elif op == "*":
        print(f"Result: {num1 * num2}")
    elif op == "/":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero.")
    else:
        print("Error: Invalid operation.")

calculator()