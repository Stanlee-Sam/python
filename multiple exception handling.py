x = input("Enter 1st number: ")
y = input("Enter 2nd number: ")

try:  
    z = x / int(y)
except ZeroDivisionError as e:
    print("Division by error exception")
    z = None
except TypeError as e:
    print("Type error exception")
    z = None
# this block to get the type of error
"""
except Exception as e:
    print('exception type:', type(e).__name__)
    z = None
"""

print("Division is", z)


