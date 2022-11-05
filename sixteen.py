a=10
b=5
try:
    print("Ticker Opened")
    print(a/b)
    n=int(input("Enter a value : "))
    print(n)
except ZeroDivisionError as e:
    print("Numbers can't be divisible by zero",e)
except ValueError as a:
    print("Enter valid input",a)
except Exception as e:
    print("Invalid Input!")
finally:
    print("Ticket Closed")