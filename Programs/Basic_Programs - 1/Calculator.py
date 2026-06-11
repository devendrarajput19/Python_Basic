def add(a, b):
    "Return the Sum of two numbers..."
    return a + b

def subtract(a, b):
    "Return the Subtract of two numbers..."
    return a - b

def multiply(a, b):
    "Return the Multiplication of two numbers..."
    return a * b

def division(a, b):
    "Return the Division of two numbers..."
    if b==0:
        raise ValueError("Error: Division by zero is not allowed...")
    return a / b

def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 35)
    print("       SIMPLE CALCULATOR")
    print("=" * 35)
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  5. Exit")
    print("=" * 35)

def main():
    print("\nWelcome to the Simple Python Calculator!")

    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()

        # Get operands
        num1 = float(input("Enter first number  : "))
        num2 = float(input("Enter second number : "))

        try:
            if choice=='1':
                result = add(num1, num2)
                operator = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operator = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operator = '*'
            elif choice == '4':
                result = division(num1, num2)
                operator = '/'
            
            fmt_num1 = int(num1) if num1 == int(num1) else num1
            fmt_num2 = int(num2) if num2 == int(num2) else num2
            fmt_result = int(result) if result == int(result) else result
 
            print(f"\n  Result: {fmt_num1} {operator} {fmt_num2} = {fmt_result}")

            
        except ValueError as e:
            print(f"\n  {e}")
 
#  Entry Point
# ============================================================
if __name__ == "__main__":
    main()
