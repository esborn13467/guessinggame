#this is a calculator project

number1=eval(input("Enter first number"))
number2=eval(input("Enter second number"))


operator=input("Enter operator:")


def add(num1,num2):
    result=num1+num2
    print(result)

def substract(num1,num2):
    result=num1-num2
    print(result)

def divide(num1,num2):
    result=num1/num2
    print(result)

def multiply(num1,num2):
    result=num1*num2
    print(result)

if operator=="+":
    add(number1,number2)
elif operator=="-":
    substract(number1,number2) 
elif operator=="/":
    divide(number1,number2)
elif operator=="X" or operator=="x" or operator=="*":
    multiply(number1,number2)

