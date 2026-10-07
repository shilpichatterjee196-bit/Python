a=float(input("enter the 1st number:"))
b=float(input("enter the 2nd number:"))
c=float(input("enter the 3rd number:"))
# if(a>b):
#     if(a>c):
#          print("a is the greatest")
#     else:
#          print("c is the greatest")

# elif(b>c):
#     print("b is the greatest")
# else:
#      print("c is the greatest")
if(a>b and a>c):
    print("a is the greatest")
elif(b>c):
    print("b is greatest")
else:
    print("c is the greatest")