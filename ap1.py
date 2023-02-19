#ERROR HANDLING.....
while(True):
    print("Press q to quit")
    a = input("Enter the no.")
    if a=='q':
        break
    try:    
        a = int(a)
        if a>6:
            print("you entered a no. greater than 6")
    except Exception as e:
        print(f"your input resulted in error: {e}")
print("thanks for playing the game")