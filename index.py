# ---------- FUNCTIONS ----------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# ---------- SAFE INPUT FUNCTION ----------
def get_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None


# ---------- CONTINUE MODE ----------
def continue_mode():
    print("\n CONTINUE MODE STARTED")

    result = get_number("Start number enter karo: ")
    if result is None:
        return

    while True:
        print("\nCurrent Result:", result)
        print("Operations: +  -  *  /  |  type 'exit' to stop")

        op = input("Enter operation: ")

        if op == "exit":
            print("Exit from continue mode")
            break

        num = get_number("Next number enter karo: ")
        if num is None:
            continue

        if op == "+":
            result = add(result, num)
        elif op == "-":
            result = subtract(result, num)
        elif op == "*":
            result = multiply(result, num)
        elif op == "/":
            result = divide(result, num)
            if isinstance(result, str):  # error case
                print(result)
                result = 0
        else:
            print("Invalid operation")


# ---------- MAIN PROGRAM ----------
while True:
    print("\n===== ADVANCED CLI CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Continue Mode ")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "6":
        print("Calculator closed")
        break

    elif choice == "5":
        continue_mode()

    elif choice in ["1", "2", "3", "4"]:
        a = get_number("First number: ")
        b = get_number("Second number: ")

        if a is None or b is None:
            continue

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))

    else:
        print("Invalid choice! Select 1-6")