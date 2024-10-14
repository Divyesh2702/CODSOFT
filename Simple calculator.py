def addition(a, b):
    return a+b  
def subtraction(a, b):
   return a-b
def multiplication(a, b):
   return a*b
def division(a, b):
    if b == 0:
        print("Math Error: Cannot divide by 0!!!!")
        return None
    return a/b  
operation = {1:addition,2:subtraction,3:multiplication,4:division}
def calculate():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division") 
    choice = input_number("Enter choice(1-4): ")
    num1 = input_number("Enter first number: ")
    num2 = input_number("Enter second number: ")
    func = operation.get(choice)
    if func:
        ans = func(num1, num2)
        if ans is not None:
            print(ans) 
    else:
        print("Invalid operation")
def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue    
calculate()