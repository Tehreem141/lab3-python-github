def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    if b==0:
     return "Error: cannot divide by zero"
    return(a/b)
def check_even_odd(n):
    if n%2==0:
      return "even"
    else:
      return "odd"
def percentage(a,b):
    if b==0:
        return "Error: cannot divide by zero"
    return(a/b)*100
while True:
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")
    choice = input("Choose an option (1-7): ")
    if choice == "7":
        print("Goodbye!")
        break
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Wrong choice. Please pick 1 to 7.")
        continue
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    elif choice == "5":
        print(int(a), "is", check_even_odd(int(a)))
    elif choice == "6": 
        print("Result:", percentage(a, b), "%")
