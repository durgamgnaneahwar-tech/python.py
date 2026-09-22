# Interview Questions – Logic-Based Programs
# ________________________________________
# 🔢 Prime and Armstrong Logic Questions
# 1. Print All Prime Numbers from m to n
# Problem: Given a range from m to n, print all prime numbers in that range.
# Input: m = 10, n = 30
# Output: 11 13 17 19 23 29
# Explanation: A prime number has only two factors: 1 and itself.

# n = 10
# m = 30
# for i in range(n,m+1):
#     count=0
#     for j in range(1,i+1):
#      if i%j==0:
#         count+=1
#     if count==2:
#       print(i)


# ________________________________________
# 2. Count of All Prime Numbers from m to n
# Problem: Count how many prime numbers are there between m and n.
# Input: m = 1, n = 10
# Output: 4
# Explanation: Prime numbers are: 2, 3, 5, 7

# n = 1
# m = 10
# prime=0
# for i in range(n,m+1):
#     count=0
#     for j in range(1,i+1):
#      if i%j==0:
#         count+=1
#     if count==2:
#       prime+=1
#       print(i)
# print(prime)

# ________________________________________
# 3. Print All Armstrong Numbers in a Range
# Problem: Print all Armstrong numbers between m and n.
# Input: m = 1, n = 500
# Output: 1 153 370 371 407
# Explanation: Armstrong number = sum of each digit raised to the power of number of digits.



# m = 1
# n = 500
# # sum=0
# for i in range(m,n+1):
#     st=str(i)
#     l=len(st)
#     sum=0
#     for j in st:
#         sum+=int(j)**l
#     if i==sum:
#        print(i)


   


# ________________________________________
# 4. First Prime Number from m to n
# Problem: Find the first prime number in the given range.
# Input: m = 10, n = 25
# Output: 11

# m = 10
# n = 25
# for i in range(m,n+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)
#         break



# ________________________________________
# 5. Last Prime Number from m to n
# Problem: Find the last prime number in the given range.
# Input: m = 10, n = 25
# Output: 23

# m = 10
# n = 25
# last_prime=[]
# for i in range(m,n+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         # print(i)
#         last_prime.append(i)
# print(last_prime[-1])


# ________________________________________
# 6. First Vowel in a Name
# Problem: Given a string, find the first vowel in the string.
# Input: name = "Krishna"
# Output: i
# Explanation: First vowel from left is ‘i’

# name="krishna"
# vowels="aeiouAEIOU"
# for i in name:
#     if i in vowels:
#         print(i)
#         break
        


# ________________________________________
# 7. Last Vowel in a Name
# Problem: Given a string, find the last vowel in the string.
# Input: name = "Ramakrishna"
# Output: a
# Explanation: Last vowel is ‘a’
# ________________________________________
# 8. Print All Even Numbers Using Continue
# Problem: Use continue statement to skip odd numbers and print only even numbers between 1 and n.
# Input: n = 10
# Output: 2 4 6 8 10
# ________________________________________
# 9. Print All Odd Numbers Using Continue
# Problem: Use continue statement to skip even numbers and print only odd numbers.
# Input: n = 10
# Output: 1 3 5 7 9
# ________________________________________
# 10. Count of Prime and Composite Numbers from m to n
# Problem: Count how many are prime and how many are composite numbers in range m to n.
# Input: m = 1, n = 10
# Output: Prime: 4, Composite: 4
# Explanation: Prime: 2,3,5,7 | Composite: 4,6,8,9
# ________________________________________
# Would you like to: - 🐍 Add code for these too? - 📥 Merge this into your main pattern document? - ➕ Add more logic/interview questions?





# n=123
# def sumOfDigits(n):
#     st=str(n)
#     l=len(st)
#     sum=0
#     for i in st:
#         i=n%10
#         sum+=i
#         # return sum
# print(sum)

# def MaxMinDifference(nums):
#   if max-min==difference:
#     min(nums)=min
#     max(nums=max)
#     return difference





