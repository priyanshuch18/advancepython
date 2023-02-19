#TRY WITH FINALLY
try:
    i = int(input("enter the no."))
    c= 1/i 
except Exception as e:
    print(e)
finally:
    print("we are done") #it  run irrespective the exception occur