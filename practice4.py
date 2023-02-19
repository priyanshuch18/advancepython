a = int(input("enter the first no."))
b = int(input("enter the second no."))
try:
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print(f"it shows {e} error")
print("thank you")