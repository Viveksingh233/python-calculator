import math

def calculator():
    print("Select operation:")
    print("1. Square Root")
    print("2. Square")
    print("3. Inverse")
    print("4. Cube Root")
    print("5. Cube")
    print("6. Addition")
    print("7. Subtraction")
    print("8. Multiplication")
    print("9. Division")

choice = input("Enter choice (1/2/3/4/5/6/7/8/9):")

if choice in ['1','2','3','4','5']:
    num = float(input("Enter a number: "))

if choice == '1':
    
    
    print(f"Square Root of {num} is {math.sqrt(num)}")
elif choice == '2':
    
    print(f"Square of {num} is {num ** 2}")
elif choice == '3':
    

    if num != 0:
        
        print(f"Inverse is not defined for zero.")
elif choice == '4':
    print(f"Cube Root of {num} is {num ** (1/3)}")
elif choice == '5':
    print(f"Cube of {num} is {num ** 3}")
elif choice in ['6','7','8','9']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

if choice == '6':
    print(f"The result of {num1} + {num2} is {num1 + num2}")
elif choice == '7':
    print(f"The result of {num1} - {num2} is {num1 - num2}")
elif choice == '8':
    print(f"The result of {num1} * {num2} is {num1 * num2}")
elif choice == '9':
    if num2 != 0:
        print(f"The result of {num1} / {num2} is {num1 / num2}")
    else:
        
        print("Division by zero is not allowed.")
else:
    
        print("Invalid input")
        if__name__=="__main__";

calculator()

