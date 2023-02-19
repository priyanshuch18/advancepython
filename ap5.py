from platform import java_ver
from re import A


a = 54 #Global variable
def func1():

    a =8 #local variable
    print(a)
func1()
print(a)