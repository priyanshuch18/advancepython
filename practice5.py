a= int(input("enter the no."))
# b=[]
# for i in range(1,11):
#     i=i*a
#     b.append(i)
# print(b)
table= [a*i for i in range(1, 11)]
print(table)
with open("tab.txt","a") as f:
    f.write(str(table))
    f.write("\n")