x = float(input("Enter the first number: "))
operation = input("Enter operation (+ or -): ")
y = float(input("Enter the second number: "))

if operation == "+":
    result = x + y
elif operation == "-":
    result = x - y
elif operation == "*":
    result = x * y
else:
    print("Unknown operation!")
    exit()


print("Result:", result)