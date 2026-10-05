#grade system
marks=int(input("enter the marks of the student:"))
if(marks>=90):
    print("O")
elif(marks>=80 and marks<89):
    print("A")
elif(marks>=70 and marks<79):
    print("B")
elif(marks>=60 and marks<=69):
    print("C")
else:
    print("fail")
