from calculator.operations import add, subtract, multiply, divide

OPERATIONS = {
    "add": add,
    "sub": subtract,
    "mul": multiply,
    "div": divide
}

def run_calculator():
    print("Welcome to Calculator")
    print("Operations: add, sub, mul, div, exit")

    while True:
        operation = input("Enter operation: ").lower()

        if operation == "exit":
            print("Goodbye!")
            break

        if operation not in OPERATIONS:
            print("Invalid operation")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = OPERATIONS[operation](a, b)
            print(f"Result: {result}")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")

        except ValueError:
            print("Error: Invalid number input")


if __name__ == "__main__":  # pragma: no cover
    run_calculator()

