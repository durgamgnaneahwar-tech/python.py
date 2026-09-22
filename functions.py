# Function-Based Interview Questions – Logic & Practice
# ________________________________________
# 1. Add Two Numbers Using Function
# Problem: Write a function that takes two numbers as arguments and returns their sum.
# Explanation: The function should accept two inputs and return the result of their addition.
# Input:
# Enter first number: 10
# Enter second number: 20
# Output:
# Sum = 30

# from encodings import iso2022_jp


# def add(n,m):
#     total=n+m
#     print(total)
# add(10,20)


# ________________________________________
# 2. Check Even or Odd Using Function
# Problem: Write a function that determines whether a number is even or odd.
# Explanation: Even numbers are divisible by 2. The function should return “Even” or “Odd”.
# Input:
# Enter number: }+}+}+
# Output:
# 15 is Odd

# def checkEvenOdd(n):
#     if n%2==0:
#         print("15 is even")
#     else:
#         print("15 is odd")
# checkEvenOdd(15)



# ________________________________________
# 3. Check Leap Year Using Function
# Problem: Write a function that checks if a given year is a leap year.
# Explanation: A leap year is divisible by 4 but not by 100 unless also divisible by 400.
# Input:
# Enter year: 2020
# Output:
# 2020 is a Leap Year

# def year(y):
#     if (y%4==0 and y%100==0) or y%400==0:
#         print("leap year")
#     else:
#         print("not leap year")
# year(2000)

# ________________________________________
# 4. Check Prime Number Using Function
# Problem: Write a function that checks whether a given number is prime.
# Explanation: A prime number has only two factors: 1 and itself.
# Input:
# Enter number: 13
# Output:
# 13 is a Prime Number

# def primenum(n):
#     count=0
#     if n%i==0:
#         count+=1
#     if count==2:
#         print(i)
# primenum(13)

# ________________________________________
# 5. Print Armstrong Numbers from m to n Using Function
# Problem: Write a function that prints all Armstrong numbers in a given range from m to n.
# Explanation: Armstrong number = sum of digits raised to the power of number of digits.
# Input:
# m = 100
# n = 500
# Output:
# Armstrong Numbers between 100 and 500: 153 370 371 407

# def checkArmstrong(m,n):
#     for i in range(m,n+1):        
#         st=str(i)
#         l=len(st)
#         sum=0
#         for digit in st:
#             sum+=int(digit)**l
#         if sum==i:
#             print(i)
# checkArmstrong(100,500)


# ________________________________________
# 🔁 Recursion-Based Problems
# 6. Factorial Using Recursion
# Problem: Write a recursive function to calculate the factorial of a number.
# Explanation: factorial(n) = n * factorial(n - 1), with base case factorial(0) = 1.
# Input:
# Enter number: 5
# Output:
# Factorial = 120

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))


# ________________________________________
# 7. Fibonacci Series Using Recursion
# Problem: Print the Fibonacci series up to n terms using recursion.
# Explanation: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) with base cases fibonacci(0)=0, fibonacci(1)=1.
# Input:
# Enter terms: 5
# Output:
# Fibonacci Series: 0 1 1 2 3

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
# for i in range(5):
#     print(fibonacci(i), end=" ")

# ________________________________________
# 8. Sum of Digits Using Recursion
# Problem: Write a recursive function to find the sum of digits of a number.
# Explanation: sum(n) = n % 10 + sum(n // 10)
# Input:
# Enter number: 123
# Output:
# Sum of digits = 6

# def sum(n):
#     if n == 0:
#         return 0
#     return n%10 + sum(n//10)
# print(sum(123))

# ________________________________________
# 9. Reverse a Number Using Recursion
# Problem: Write a recursive function to reverse the digits of a number.
# Explanation: Keep multiplying result by 10 and adding the current digit.
# Input:
# Enter number: 1234
# Output:
# Reversed Number = 4321

# def reverse(n,rev=0):
#     if n == 0:
#         return rev
#     return reverse(n//10,rev*10+n%10)
# print(reverse(1234))

# def count(n):
#     if n==0:
#         return 0
#     return 1+count(n//10)
# print(count(1234))

# ________________________________________
# 10. Check Palindrome Using Recursion
# Problem: Write a recursive function to check if a string is a palindrome.
# Explanation: Compare first and last characters and recurse on the substring.
# Input:
# Enter string: madam
# Output:
# The string is a palindrome.

# def palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrome(s[1:-1])

# string = input("Enter string: ")

# if palindrome(string):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# ________________________________________
# ✅ These problems focus on basic function usage and logical thinking, great for beginner interviews.
# Would you like to:
# •	🐍 Add Python code for each question?
# •	📥 Export as a PDF?
# •	➕ Add more recursion/function-based problems?


# def num(n):
#     if n==6:
#         return 0
#     print(n)
#     num(n+1)        #1,2,3,4,5
# num(1)


# def num(n):
#     if n==0:
#         return 0
#     num(n+1)     #5,4,3,2,1
# num(5)



# def num(n):
#     sum=0
#     if n==6:
#         sum+=n+1
#     print(sum)
# num(5)


# def sum(n):
#     if n==6:
#         return 0
#     return n+sum(n+1)
# print(sum(1))









