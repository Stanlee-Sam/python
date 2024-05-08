x = input("Enter 1st number: ")
y  = input("Enter second number: ")

try: 
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print("Division by zero exception")
    z = None

print("Division is: ", z)


