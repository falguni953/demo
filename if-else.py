# a = 50
# if a < 55:
#     print("hii") #indentation
#     if a == 60:
#         print("equal to")
#     elif a == 55:
#         print("second time equal to")
#     else:
#         print("not equal to")
# elif a < 60:
#     print("byee")    
# else:
#     print("hello")
# print("hello")

a = int(input("Enter 1st number:"))
b = int(input("Entre second number"))
c = input("Enter your operator")

if c == "+":
    print("Adiition is ",a+b)
    if a > b:
        print("first number is greater")
    else:
        print("Second number is greater")
elif c == "-":
    print("Subtraction is ",a-b)
elif c == "*":
    print("Multiplication is ",a*b)
elif c == "/":
    print("Division is ",a/b)
else:
    print("Enter valid operator")


# 5).write a program to accept percentage from the user and display the grade according to the following criteria:
# mark             grade
# >90               A
# >80 and <=90      B
# >=60 and <=80     C
# >=35  and <=59    D
# below 35          Fail

# ).largest number between three variable.
# 8).lowest number between three variable.




