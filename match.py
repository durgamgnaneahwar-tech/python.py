# Defining a Function

# Use the def keyword to define a function.
# function without parameter:
# def greet():
#     print("Hello, World!")
# Calling a Function
# greet()

# from typing import OrderedDict


# def greet():
#     print("hi sir,good morning")
# greet()

# Output:

# Hello, World!

# Function with Parameters

# Parameters allow you to pass data into a function.

# def greet(name):
#     print("Hello,", name)

# greet("Alice")

# Output:

# Hello, Alice
# Function with Return Value

# Use the return statement to send a value back.

# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(result)

# Output:

# 8
# Default Parameters

# You can provide default values for parameters.

# def greet(name="Guest"):
#     print("Hello,", name)

# greet()
# greet("Bob")

# Output:

# Hello, Guest
# Hello, Bob
# Keyword Arguments

# Arguments can be passed by name.

# def student(name, age):
#     print(name, age)

# student(age=20, name="John")

# Output:

# John 20
# Variable-Length Arguments
# *args (Multiple Positional Arguments)
# def total(*numbers):
#     return sum(numbers)

# print(total(1, 2, 3, 4))

# Output:

# 10
# **kwargs (Multiple Keyword Arguments)
# def display(**info):
#     for key, value in info.items():
#         print(key, ":", value)

# display(name="Alice", age=25)

# Output:

# name : Alice
# age : 25
# Lambda (Anonymous) Functions

# A lambda function is a short, single-expression function.

# square = lambda x: x * x

# print(square(5))

# Output:

# 25
# Scope of Variables
# x = 10  # Global variable

# def show():
#     y = 5  # Local variable
#     print(x)
#     print(y)

# show()
# Example Program
# def calculate_area(length, width):
#     return length * width

# area = calculate_area(10, 5)
# print("Area:", area)

# Output:

# Area: 50
# Advantages of Functions
# Avoid code repetition.
# Make programs modular.
# Improve readability.
# Simplify testing and debugging.
# Enable code reuse.

# Functions are one of the most important concepts in Python and are widely used in both small scripts and large applications.

# def vab():
#     a=20
#     b=15
#     c=a+b
#     print(c)
# vab()  

# def bab(a,b):
#     returen a+b
#     print(a+b)
# bab(10,3546312654985) 



# def num(a):
#     if a%2==0:
#         print("even")
#     else:
#         print(("odd"))
# num(2)

# def num(a):
#     if a%7==0:
#         print(a**3)
# num(49)


# def num(n,m):
#     for i in range(n,m+1):
#       count=0
#       for j in range(1,i+1):
#         if i%j==0 :
#             count+=1
#       if count==2:
#         print(i)
# num(1,10)