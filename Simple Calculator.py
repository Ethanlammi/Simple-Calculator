def main():
    print("Welcome to the Simple Calculator!")
    print("Type 'exit' anytime to quit.\n")

    while True:
        command = input("Enter a command (add, subtract, multiply, divide): ").strip().lower()

        if command == 'exit':
            print("Goodbye!")
            break

        if command not in ['add', 'subtract', 'multiply', 'divide']:    
            print("Invalid command. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if command =='add':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}\n")
        elif command == 'subtract':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}\n")
        elif command == 'multiply':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}\n")
        elif command == 'divide':
            if num2 == 0:
                print("Error: Division by zero is not allowed.\n")
                continue
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}\n")

if __name__ == "__main__":
    main()