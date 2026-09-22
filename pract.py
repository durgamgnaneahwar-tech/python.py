# ## 1
# n=6
# if n%2==0:
#     print("even")
# else:
#     print("odd")

# ## 2
# n=int(input("enter the number: "))
# if n%5==0 and n%10!=0:
#     res="satisfy"
#     print(res)
# else:
#     res="not satisfied"
#     print(res)

# ## 3
# num1=int(input("enter the number: "))
# num2=int(input("enter the numbere: "))
# if num1>num2:
#     print(num1,"is greater")
# else:
#     print(num2,"is greater")

# ## 4
# num1=int(input("enter the number: "))
# num2=int(input("enter the number: "))
# if num1<num2:
#     print("num1 is small")
# else:
#     print("num2 is small")


# ##5
# num=int(input("enter the number: "))              #18

# if num%2==0 and num%3==0 and num%6==0:
#     print("satisfied")
# else:
#     print("not satisfied")

# ## 6
# n=19
# if n>=18:
#     print("elgible")
# else:
#     print("not elgible")

# ## 7
# maths=40
# physics=36
# chemistry=30

# if maths >= 35 and physics>=35 and chemistry>=35:
#     print("pass")
# else:
#     print("fail")

# ## 8
# maths=35
# physics=38
# chemistry=25

# if maths>=35 or physics>=35 or chemistry>=35:
#     print("pass")
# else:
#     print("fail")

# ## 9
# maths = 40
# physics = 20
# chemistry = 36 

# if ((maths >= 35 and physics >= 35) or
#     (maths >= 35 and chemistry >= 35) or
#     (physics >= 35 and chemistry >= 35)):
#     print("Pass")
# else:
#     print("Fail")

# ## 10
# a = 7
# b = 4
# c = 9 

# if a>b and a>c:
#     print(a,"a biggest")
# elif b>a and b>c:
#     print(b,"b biggest")
# else:
#     print(c,"c biggest")


# ## 11
# a = 7
# b = 4
# c = 9

# if a<b and a<c:
#     print(a,"a small")
# elif b<a and b<c:
#     print(b,"b smallt")
# else:
#     print(c,"c small")

# ## 12
# a=49

# if a**0.5==int(a**0.5):
#     print("perfect square")
# else:
#     print("not")


# ## 13
# n=17
# if n%5==0:
#     cars=n//5
#     print(cars)
# else:
#     cars=n//5+1
#     print("cars needed :",cars)


# ## 14
# a=10
# b=25
# c=18
# if (a > b and a < c) or (a > c and a < b):
#     print(a)
# if (b > a and b < c) or (b > c and b < a):
#     print(b)
# else:   
#   print(c)


# ## 15
# year=2024
# if year%4==0 and year%100!=0 or year%400==0:
#     print("leap year")
# else:
#     print("not")


# ## 16
# n="$"
# if ord(n)>26 and ord(n)<47:
#     print(n,"is special charecter")
# else:
#     (print("not"))


# n="gnan"
# print(len(n))

# ## 17
# inp=int(input("enter marks: "))

# if inp<=100 and inp>90:
#     print("grade A")
# elif inp<=90 and inp>80:
#     print("grade B")
# elif inp<=80 and inp>60:
#     print("grade C")
# elif inp<=60 and inp>35:
#     print("grade d")
# else:
#     print("fail")

# # 1.Write a program to check whether a number is positive, negative, or zero.

# inp=int(input("enter a num: "))
# if inp>0:
#     print("positive")
# if inp<0:
#     print("nagitive")
# if inp==0: 
#     print("zero")

# # 2.Write a program to check whether a number is even or odd. 

# inp=int(input("enter a number: "))
# if inp%2==0:
#     print("even")
# else:
#     print("odd")

# # 3.Write a program to find the biggest of two numbers. 

# n1=int(input("enter n1: "))
# n2=int(input("enter n2: "))
# if n1>n2:
#     print(n1,"is biggest")
# else:
#     print(n1,"is biggest")

# # 4.Write a program to find the biggest of three numbers using nested if.

# a=10
# b=15
# c=20
# if a>b:
#     if a>c:
#         print(a,"is biggest")
#     else:
#         print(c,"is biggest")
# else:
#     if b>c:
#         print(b,"is biggest")
#     else:
#         print(c,"is biggest")

# # 5.Write a program to check whether a year is a leap year or not.

# year=2024
# if (year%4==0 and year%100==0) or year%400!=0:
#     print("is leap year")
# else:
#     print("not")

# # 6.Write a program to check whether a person is eligible to vote (age ≥ 18).

# age=int(input("enter age: "))
# if age>=18:
#     print("elgible")
# else:
#     print("not elgible")

# # 7.Write a program to check whether a character is a vowel or a consonant.

# char=input("enter char: ")
# if char in "aeiouAEIOU":
#     print("vowel")
# else:
#     print("consonant")

# # 8.Write a program to check whether a number is divisible by both 3 and 5.

# num=int(input("enter a num: "))
# if num%3==0 and num%5==0:
#     print("divisible")
# else:
#     print("not divisable")

# # 9.Write a program to calculate a student's grade based on
# # marks: 90–100: A 80–89: B 70–79: C 60–69: D Below 60: Fail 

# marks=int(input("enter marks: "))
# if 90<=marks<=100:
#     print("Grade A")
# elif 80 <=marks<=89:
#     print("Grade B")
# elif 70<=marks<=79:
#     print("Grade C")
# elif 60<=marks<=69:
#     print("Grade D")
# else:
#     print("fail")

# # 10.Write a program to find the smallest of three numbers.

# a=45
# b=64
# c=79
# if a<b :
#     if a<c:
#         print(a,"is small")
#     else:
#         print(c ,"is small")
# else:
#     print(b,"is small")

# # 11.Write a program to check whether a given alphabet is uppercase or lowercase.

# # 65
# # 90
# # 97
# # 122

# char=input("enter char: ")
# if ord(char)>=65 :
#     if ord(char)<=90:
#         print(char,"char is upercase")
#     else:
#      print(char,"lower case")

# # 12.Write a program to calculate the electricity bill: Up to 100 n: ₹2/unit 101–200 n: ₹3/unit Above 200 n: ₹5/unit 

# n=int(input("enter n: "))
# if 0<n<=100:
#     print(n*2)
# elif 101<=n<=200:
#     print(n*3)
# elif 201<n<=300:
#     print(n*5)
# else:
#     print("no bill")

# # 13.Write a program to check whether a number is a three-digit number or not.

# num=int(input("enter num: "))

# if num >99:
#     if num<999:
#         print(num,"is 3 digit num")
# else:
#     print(num,"is not 3 digit num")

# # 14.Write a program to calculate the discount Purchase ≥ ₹5000 → 20% discount Purchase ≥ ₹3000 → 10% discount Otherwise → No discount

# bill=int(input("enter the bill: "))
# disc=0
   
# if bill>=50000:
#     disc=bill/20
#     print(disc)
#     total=bill+disc
#     print(total)

# elif bill>=3000:
#     disc=bill/10
#     print(disc)
#     total=bill+disc
#     print(total)

# else:
#     print("no disc")


# # 15.Write a program to create a simple login system: If username is admin and password is 1234, print "Login Successful". Otherwise, print "Invalid Username or Password". 

# user=input("enter user name: ")
# password=int(input("enter password: "))

# login=("user_id","_password")
# if user=="gnan" and password==1234:
#     print("login")
# else:
#     print("user not found")





# n=[1,2,3,4,5,6,7,8,9,10]
# res=["even" if i%2==0 else "odd" for i in n]
# print(res)

# =n=[10,85,56,12,26,78,56]
# res=[i**2 if i>30 else i**3 for i in n]
# print(res)


# res=[[j*10+i for i in range(1,4)] for j in range(1,4)]
# print(res)

# res={(i,j) for i in range(1,4) for j in range(3)}
# print(res)

l=[1,2,3,4,5,6,7,8,9]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#       print(i)

# for i in l:
#     k=i+1
#     count=0
#     for j in range(1,k+1):
#         if k%j==0:
#             count+=1
#     if count==2:
#       print(i)


# num=[637,1761,4864,900]
# for i in num:
#     t=i
#     ld=t%10
#     while t!=0:
#         fd=t%10
#         t//=10
#     if ld==fd:
#         print(i)

    



