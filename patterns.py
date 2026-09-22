# Pattern-Based Programming Questions (All 35 Questions - Interview Style)
# ________________________________________
# 🔷 Square, Rectangle, and Triangle Patterns (1–15)
# 1.	Solid Square Pattern
# Problem: Print a solid square of stars of size n.
# Input: n = 4
# Output:
# * * * *
# * * * *
# * * * *
# * * * *

# n=4
# for i in range(1,n+1):
#     res=""
#     for j in range(1,n+1):
#         res+="* "
#     print(res)

# 2.	Solid Rectangle Pattern
# Problem: Print a solid rectangle of m rows and n columns.
# Input: m = 3, n = 5
# Output:
# * * * * *
# * * * * *
# * * * * *
# n=5
# m=3
# for i in range(1,m+1):
#     res=""
#     for j in range(1,n+1):
#         res+="* "+" "
#     print(res)

# 3.	Right-Angled Triangle (Left-Aligned)
# Problem: Print a left-aligned right-angled triangle.
# Input: n = 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

# n=5
# for i in range(1,n+1):
#     res=" "
#     for j in range(0,i):
#         res+=" *"
#     print(res)


# 4.	Right-Angled Triangle (Right-Aligned)
# Input: n = 5
# Output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# n=5
# for i in range(1,n+1):
#     for space in range(n-i):
#         print(" ",end=" ")
#     for star in range(1,i+1):
#         print("*",end=" ")
#     print()

# 5.	Inverted Triangle (Left-Aligned)
# Input: n = 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# 6.	Inverted Triangle (Right-Aligned)
# Input: n = 5
# Output:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print("",end ="  ")
#     for k in range(1,i+1):
#             print("*",end=" ")
#     print()

# 7.	Centered Pyramid Pattern
# Input: n = 4
# Output:
#       *
#     * * *
#   * * * * *
# * * * * * * *

# n=4
# for i in range(1,n+1):
#     for space in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print(" *",end="")
#     print()


# 8.	Diamond Pattern
# Input: n = 3
# Output:
#     *
#   * * *
# * * * * *
#   * * *
#     *
# n=3
# for i in range(1,n+1):
#     for space in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print(" *",end="")
#     print()
# for i in range(n-1,0,-1):
#     for space in range(n-i):
#         print("  ",end="")
#     for j in range(2*i-1):
#          print("* ",end="")
#     print()


# 9.	Butterfly Pattern
# Input: n = 4
# Output:
# *       *
# * *   * *
# * * * * *
# * *   * *
# *       *


# 10.	Left-Aligned Half Diamond
# Input: 
# Output:
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
# n=4
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(n-1,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# 11.	Right-Aligned Half Diamond
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *
# n=4
# for i in range(1,n+1):
#     print()
#     for k in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
# print()
# for i in range(n-1,0,-1):
#     for s in range(n-i):
#         print("  ",end="")
#     for j in range(i):
#         print("* ",end="")
#     print()
    
# 12.	Sandglass Pattern
# Input: n = 4
# Output:

# * * * *
#   * * *
#     * *
#       *
#     * *
#   * * *
# * * * *

# n=4
# for i in range(n,0,-1):
#     for s in range(n-i):
#         print("  ",end="")
#     for j in range(i):
#         print("* ",end="")
#     print()
# for i in range(2,n+1):
#     for k in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# 13.	Increasing Width Triangle
# Input: n = 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print( )

# 14.	Decreasing Width Triangle
# Input: n = 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

# n=5
# for i in range(1,n +1):
#     print("",end=" ")
#     for j in range(n-i+1):
#         print("* ",end="")
#     print()

# 15.	Right-Aligned Hill Pattern
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *


# n=4
# for i in range(1,n+1):
#     print()
#     for k in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
# print()

# ________________________________________
# 🔲 Hollow Patterns (16–25)
# 16.	Hollow Square Pattern
# Problem: Print a hollow square of stars of size n.
# Input: n = 4

# Output:

# * * * *
# *     *
# *     *
# * * * *

# n = 4
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == 1 or i == n or j == 1 or j == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# for i in range(4,0):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()

# 17.	Hollow Rectangle Pattern
# Problem: Print a hollow rectangle of m rows and n columns.
# Input: m = 4, n = 5
# Output:
# * * * * *
# *       *
# *       *
# * * * * *

# n = 5
# for i in range(1, n + 1):
#     for j in range(1, n+1):
#         if i == 1 or i == n or j == 1 or j == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 18.	Hollow Right-Angled Triangle (Left-Aligned)
# Input: n = 5
# Output:
# *
# * *
# *   *
# *     *
# * * * * *
# n = 5

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if i == 1 or i == n or j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 19.	Hollow Right-Angled Triangle (Right-Aligned)
# Input: n = 5
# Output:
#         *
#       * *
#     *   *
#   *     *
# * * * * *

# n = 5

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print("  ", end="")
#     for j in range(1, i + 1):
#         if i == 1 or i == n or j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 20.	Hollow Inverted Triangle (Left-Aligned)
# Input: n = 5
# Output:
# * * * * *
# *     *
# *   *
# * *
# *

# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         if i == 1 or j == 1 or j == (n - i + 1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 21.	Hollow Inverted Triangle (Right-Aligned)
# Input: n = 5
# Output:
# * * * * *
#   *     *
#     *   *
#       * *
#         *

# n = 5

# for i in range(1, n + 1):
    # for space in range(n-i):
    #     print(" ",end=" ")
    # for j in range(1,n-i+2):
    #     if i == 1 or j == 1 or j == (n - i + 1):
    #         print("*", end=" ")
    #     else:
    #         print(" ", end=" ")

    # print()

# 22.	Hollow Pyramid Pattern
# Input: n = 4
# Output:
#       *
#     *   *
#   *       *
# * * * * * * *

n=4
for i in range(1,n+1):
    for j in range(n-i):
        print("  ",end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()

# 23.	Hollow Diamond Pattern
# Input: n = 3
# Output:
#     *
#   *   *
# *       *
#   *   *
#     *

# 24.	Hollow Butterfly Pattern
# Input: n = 4
# Output:
# *       *
# * *   * *
# *   *   *
# *       *
# *   *   *
# * *   * *
# *       *
# 25.	Hollow Hourglass Pattern
# Input: n = 5
# Output:
# * * * * *
# *       *
#   *   *
#     *
#   *   *
# *       *
# * * * * *


# ________________________________________
# 🔢 Number-Based Patterns (26–35)
# 26.	Increasing Number Triangle
# Problem: Print numbers from 1 to n in triangle form.
# Input: n = 5
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 27.	Repeating Row Number Triangle
# Input: n = 5
# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n=5
for i in range(1,n+1):
   for j in range(1,i+1):
      print(i,end=" ")
   print()

# 28.	Continuous Number Triangle
# Input: n = 4
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# 29.	Reverse Row Number Triangle
# Input: n = 5
# Output:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# 30.	Inverted Number Triangle
# Input: n = 5
# Output:5
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# 31.	Right-Aligned Number Triangle
# Input: n = 5
# Output:
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
# 32.	Pyramid Number Pattern
# Input: n = 4
# Output:
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1
# 33.	Even Number Triangle
# Input: n = 5
# Output:
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
# 34.	Odd Number Triangle
# Input: n = 5
# Output:
# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9
# 35.	Pascal’s Triangle
# Input: n = 5
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# ________________________________________
# ✅ All 35 pattern questions are now fully formatted in an interview-style layout with problem statements, inputs, and expected outputs.
# Would you like to:
# •	🐍 Add Python code for each?
# •	📥 Export as a PDF?









