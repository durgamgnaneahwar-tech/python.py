# # armstrong_num:
# def armstrong_num(n,m):
#     sum=0
#     for i in range(n,m+1):
#         st=str(i)
#         l=len(st)
#         sum=0
#         for j in st:
#             sum += int(j) ** l
#         if i == sum:
#          print(i)
# armstrong_num(1,500)


# # factorial:
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# factorial(4)

# def reverse(n):
#     st=str(n)
#     revers=st[::-1]
#     print(revers)
# reverse(123)

# def rev(a):
#     temp=a
#     r=0
#     while temp>0:
#         digit=temp%10
#         r=r*10+digit
#         temp=temp//10
#     print(r)
# rev(123)


# def add(a):
#     temp=a
#     b=0
#     while temp>0:
#         digit=temp%10
#         b+=digit
#         temp=temp//10
#     print(b)
# add(123)


# def summ(n):
#     st=str(n)
#     sum=0
#     for i in st:
#         sum+=int(i)
#     return sum
# print(summ(123))

# def perfectnum(n):
#     sum=0
#     for i in range(1,n):
#         sum=0
#         if i%j==0:
#             sum+=i
#     if n==sum:
#         print("perfect num")
#     else:
#         print("not perfect")
# perfectnum(6)

# s="ramulu"
# e=s.upper()
# print(e)

# s="GnanEshwaR"
# print(s.swapcase())

# s="hello python"
# print(s.title())
# print(s.capitalize())
# print(s.index("o",6))
# print(s.index("th"))
# print(s.index("on"))
# print(s.rindex("o"))
# print(s.find("L"))
# print(s.find("A"))
# print(s.rfind("o"))

# s="               hello python                  "
# print(s.strip())
# print(len(s))
# print(s.rstrip())
# print(s.lstrip())


# s={10,20,30,40}
# s.update([6,7,8],{99})
# s.add(50)
# s.remove(10)
# s.remove(90)
# s.discard(50)
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.clear()
# del.s
# s1=s.copy()
# issubset
# print(s)

d={"name":"gnaneshwar","role":"aspiring"}
# d.update(20)
# print(d)
print(d.values())
print(list(d.values()))
print(d.values())
print(dict(d.items()))
# print(d.get(10,50))


