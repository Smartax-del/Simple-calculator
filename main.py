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

import json

def add(a, b):     return a + b
def sub(a, b):     return a - b
def mul(a, b):     return a * b
def div(a, b):     return a / b if b != 0 else "Cannot divide by zero"
def power(a, b):   return a ** b 
def fl_div(a, b):  return a // b if b != 0 else "Cannot be divided by zero!"   
def mod (a, b):    return a % b if b != 0 else "Cannot be divided by zero!"

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '**': power,
    '//': fl_div,
    '%': mod
}

History_file = "calculator_history.json"

def load_history():
    try:
        with open(History_file, "r" , encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_history(history):
    try:        
        with open(History_file, "w", encoding="utf-8") as file:
            json.dump(history, file, ensure_ascii=False, indent=2)
            print(f"History saved to ({len(history)}) tasks")
    except Exception as e:
        print(f"Error saving history: {e}")
    
def show_history(history):
    if not history:
        print("No history found")
        return
    print("\n History:")
    for i, entry in enumerate(history,1):
        print(f"{i}. {entry}")

def calculator():
    history = load_history()   
    print("Calculator  (supported operations: + - * / // ** %)")
    print("Commands:  s / save  → save history")
    print("   h / history → show history")
    print("   ex / exit   → exit\n")
     
    while True:
        action = input("Operation:(+ - * / // ** % or h/s/ex ): ").strip().lower()
        if action in ("ex", "exit"):
            print("Good bye!")
            break
        
        if action in ("h", "history"):
            show_history(history)
            continue
        
        if action in ("s", "save"):
            save_history(history)
            continue
        
        if action not in operations:
            print("Invalid operation. Please try again.")
            continue 
        
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")   
            continue
        result = operations[action](a, b)
        entry = f"{a} {action} {b} = {result}"
        history.append(entry)
        print(f"Result: {result}\n")
                
if __name__ == "__main__":    
    calculator() 