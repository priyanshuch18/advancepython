#RAISING EXCEPTION
def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("this is not good")
a = increment('dref54')
print(a)
