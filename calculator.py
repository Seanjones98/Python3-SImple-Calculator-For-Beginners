# Python Calculator For Beginners With Python
#Enjoy!!



num01 = input("Enter First Number ")
Operator = input("Enter An Input ""eg +,-,/,*,%,""\n")
num02 = input("Enter Second Number ")

if Operator == '*' :
    print("\n")
    print(int(+ num01)*int(num02))

elif Operator == '-':
    print("\n")
    print(int(num01)-int(num02))

elif Operator == '+' :
    print("\n")
    print(int(num01)+int(num02))

elif Operator == '/' :
    print("\n")
    print(int(num01)/int(num02))

elif Operator == '%' :
    print("\n")
    print(int(num01)%int(num02))

else:
    print("You Have entered An Invalid Option")