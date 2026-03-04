# Simple console calculator.
# Supported operations:
# +  addition
# -  subtraction
# *  multiplication
# /  division
# // floor division
# ** exponentiation
# %  modulo
# Includes input validation and error handling.

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot be divided by zero!"

def power(a, b):
    return a ** b 

def fl_div(a, b):
    if b != 0:
        return a // b
    else:
        return "Cannot be divided by zero!"
    
def mod (a, b):
    if b != 0:
        return a % b
    else:
        return "Cannot be divided by zero!"
        
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '**': power,
    '//': fl_div,
    '%': mod
}

def calculator():
    print("Function: +, -, *, /, **, //, %, ex - exit\n ")
     
    while True:
        try:
            num1 = float(input("Enter the first number: "))
        except ValueError:
            print("Please enter valid numbers!\n")
            continue
        
        try:
            action = input("Function (+ - * / ** // %  ex ): ").strip()
        except ValueError:
            print("Please enter a valid operation!\n")
            continue

        if action.lower() in ("ex" , "exit"):
            print("Bye bye")
            break

        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers!\n")
            continue

        if action in operations:
            result = operations[action](num1, num2)
            print(f"Result: {result}\n")
        else:
            print("You chose wrong")
if __name__ == "__main__":    
    calculator() 