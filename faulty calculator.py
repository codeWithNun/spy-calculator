2#Exercise 2= faulty calculator
# 45*3 = 555, 56+9 = 77, 56/6 = 5
# you program should take operator and then 
# 2 number as input from user and then return the result
"""
a = input("Enter First Number")
b = input("what so you want to do (+ - * /)")
c = input("Enter Second Number")

print(int(a),int(b),int(c))
"""
print ("Enter first number :")
num1 = int(input())
print ("Enter second number :")
num2 = int(input())
print('so what you want =,-,/,* ')
num3 = input()
if num1==45 and num2 == 3 and num3 == '*': 
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
    print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
    print("5")

elif num3 == '*':
    print(num1*num2)
elif num3 == '+':
    print(num1+num2)
elif num3 == '/':
    print(num1/num2)
elif num3 == '-':
    print(num1-num2)

else:
    print("Error! Please check your question")