# Simple Interactive Calculator in Python

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers with zero check"""
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def calculator():
    """Main calculator function"""
    print("🎯 WELCOME TO PYTHON CALCULATOR!")
    print("=" * 45)
    
    while True:
        try:
            # Get user input
            print("\n--- NEW CALCULATION ---")
            num1 = float(input("Enter first number: "))
            operator = input("Enter operation (+, -, *, /) or 'q' to quit: ")
            
            if operator.lower() == 'q':
                print("👋 Thank you for using calculator!")
                break
                
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            else:
                print("❌ Error: Invalid operation! Use +, -, *, or /")
                continue
            
            # Display result
            print(f"✅ Result: {num1} {operator} {num2} = {result}")
            
        except ValueError:
            print("❌ Error: Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n👋 Program stopped by user!")
            break

# Start calculator
if __name__ == "__main__":
    calculator()
