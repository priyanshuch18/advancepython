#TRY WITH ELSE 


try:
    i = int(input("enter the no."))
    c= 1/i 
except Exception as e:
    print(e)
else:
    print("we are successfull") #it run when the try statement is correct