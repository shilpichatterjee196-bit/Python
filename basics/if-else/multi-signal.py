#multi line if
age=int(input("enter the age :"))
if(age>=18):
    print("allow")
else:
    print("not allowed") 
# #single line if
food=input("food:")
eat="yes" if (food=="cake") else "No"
print(eat)

food=input("food:")
print("yes") if (food=="cake") or (food=="jalebi") else print("no")

