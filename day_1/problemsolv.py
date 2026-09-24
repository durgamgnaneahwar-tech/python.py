
"""PATTERN-BASED PROGRAMMING QUESTIONS
ALL 35 QUESTIONS - INTERVIEW STYLE

Each question is written inside triple quotes.
Each expected output is placed below its code inside triple quotes.
"""

# ============================================================
# 1. Solid Square Pattern
# ============================================================

"""Problem: Print a solid square of stars of size n.
Input: n = 4
"""

n = 4
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

"""Expected Output:
* * * *
* * * *
* * * *
* * * *
"""


# ============================================================
# 2. Solid Rectangle Pattern
# ============================================================

"""Problem: Print a solid rectangle of m rows and n columns.
Input: m = 3, n = 5
"""

m = 3
n = 5
for i in range(m):
    for j in range(n):
        print("*", end=" ")
    print()

"""Expected Output:
* * * * *
* * * * *
* * * * *
"""


# ============================================================
# 3. Right-Angled Triangle (Left-Aligned)
# ============================================================

"""Problem: Print a left-aligned right-angled triangle.
Input: n = 5
"""

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

"""Expected Output:
*
* *
* * *
* * * *
* * * * *
"""


# ============================================================
# 4. Right-Angled Triangle (Right-Aligned)
# ============================================================

"""Problem: Print a right-aligned right-angled triangle.
Input: n = 5
"""

n = 5
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()

"""Expected Output:
        *
      * *
    * * *
  * * * *
* * * * *
"""


# ============================================================
# 5. Inverted Triangle (Left-Aligned)
# ============================================================

"""Problem: Print an inverted left-aligned triangle.
Input: n = 5
"""

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

"""Expected Output:
* * * * *
* * * *
* * *
* *
*
"""


# ============================================================
# 6. Inverted Triangle (Right-Aligned)
# ============================================================

"""Problem: Print an inverted right-aligned triangle.
Input: n = 5
"""

n = 5
for i in range(n, 0, -1):
    print("  " * (n - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()

"""Expected Output:
* * * * *
  * * * *
    * * *
      * *
        *
"""


# ============================================================
# 7. Centered Pyramid Pattern
# ============================================================

"""Problem: Print a centered pyramid.
Input: n = 4
"""

n = 4
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

"""Expected Output:
      *
    * * *
  * * * * *
* * * * * * *
"""


# ============================================================
# 8. Diamond Pattern
# ============================================================

"""Problem: Print a diamond pattern.
Input: n = 3
"""

n = 3
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

for i in range(n - 1, 0, -1):
    print("  " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

"""Expected Output:
    *
  * * *
* * * * *
  * * *
    *
"""


# ============================================================
# 9. Butterfly Pattern
# ============================================================

"""Problem: Print a butterfly pattern.
Input: n = 4
"""

n = 4
for i in range(1, n + 1):
    print("* " * i + "  " * (2 * (n - i)) + "* " * i)

for i in range(n - 1, 0, -1):
    print("* " * i + "  " * (2 * (n - i)) + "* " * i)

"""Expected Output:
*             *
* *         * *
* * *     * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *
"""


# ============================================================
# 10. Left-Aligned Half Diamond
# ============================================================

"""Problem: Print a left-aligned half diamond.
Input: n = 4
"""

n = 4
for i in range(1, n + 1):
    print("* " * i)

for i in range(n - 1, 0, -1):
    print("* " * i)

"""Expected Output:
*
* *
* * *
* * * *
* * *
* *
*
"""


# ============================================================
# 11. Right-Aligned Half Diamond
# ============================================================

"""Problem: Print a right-aligned half diamond.
Input: n = 4
"""

n = 4
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

for i in range(n - 1, 0, -1):
    print("  " * (n - i) + "* " * i)

"""Expected Output:
      *
    * *
  * * *
* * * *
  * * *
    * *
      *
"""


# ============================================================
# 12. Sandglass Pattern
# ============================================================

"""Problem: Print a sandglass pattern.
Input: n = 4
"""

n = 4
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)

for i in range(2, n + 1):
    print("  " * (n - i) + "* " * i)

"""Expected Output:
* * * *
  * * *
    * *
      *
    * *
  * * *
* * * *
"""


# ============================================================
# 13. Increasing Width Triangle
# ============================================================

"""Problem: Print an increasing-width triangle.
Input: n = 5
"""

n = 5
for i in range(1, n + 1):
    print("* " * i)

"""Expected Output:
*
* *
* * *
* * * *
* * * * *
"""


# ============================================================
# 14. Decreasing Width Triangle
# ============================================================

"""Problem: Print a decreasing-width triangle.
Input: n = 5
"""

n = 5
for i in range(n, 0, -1):
    print("* " * i)

"""Expected Output:
* * * * *
* * * *
* * *
* *
*
"""


# ============================================================
# 15. Right-Aligned Hill Pattern
# ============================================================

"""Problem: Print a right-aligned hill pattern.
Input: n = 4
"""

n = 4
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

"""Expected Output:
      *
    * *
  * * *
* * * *
"""


# ============================================================
# 16. Hollow Square Pattern
# ============================================================

"""Problem: Print a hollow square of stars of size n.
Input: n = 4
"""

n = 4
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""Expected Output:
* * * *
*     *
*     *
* * * *
"""


# ============================================================
# 17. Hollow Rectangle Pattern
# ============================================================

"""Problem: Print a hollow rectangle of m rows and n columns.
Input: m = 4, n = 5
"""

m = 4
n = 5
for i in range(m):
    for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""Expected Output:
* * * * *
*       *
*       *
* * * * *
"""


# ============================================================
# 18. Hollow Right-Angled Triangle (Left-Aligned)
# ============================================================

"""Problem: Print a hollow left-aligned right-angled triangle.
Input: n = 5
"""

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""Expected Output:
*
* *
*   *
*     *
* * * * *
"""


# ============================================================
# 19. Hollow Right-Angled Triangle (Right-Aligned)
# ============================================================

"""Problem: Print a hollow right-aligned right-angled triangle.
Input: n = 5
"""

n = 5
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""Expected Output:
        *
      * *
    *   *
  *     *
* * * * *
"""


# ============================================================
# 20. Hollow Inverted Triangle (Left-Aligned)
# ============================================================

"""Problem: Print a hollow inverted left-aligned triangle.
Input: n = 5
"""

n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""Expected Output:
* * * * *
*     *
*   *
* *
*
"""


# ============================================================
# 21. Hollow Inverted Triangle (Right-Aligned)
# ============================================================

"""Problem: Print a hollow inverted right-aligned triangle.
Input: n = 5
"""

n = 5
for i in range(n, 0, -1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""Expected Output:
* * * * *
  *     *
    *   *
      * *
        *
"""


# ============================================================
# 22. Hollow Pyramid Pattern
# ============================================================

"""Problem: Print a hollow pyramid.
Input: n = 4
"""

n = 4
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, 2 * i):
        if i == n or j == 1 or j == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""Expected Output:
      *
    *   *
  *       *
* * * * * * *
"""


# ============================================================
# 23. Hollow Diamond Pattern
# ============================================================

"""Problem: Print a hollow diamond.
Input: n = 3
"""

n = 3
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n - 1, 0, -1):
    print("  " * (n - i), end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""Expected Output:
    *
  *   *
*       *
  *   *
    *
"""


# ============================================================
# 24. Hollow Butterfly Pattern
# ============================================================

"""Problem: Print a hollow butterfly.
Input: n = 4
"""

n = 4

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print("  " * (2 * (n - i)), end="")

    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print("  " * (2 * (n - i)), end="")

    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

"""Expected Output:
*             *
* *         * *
*   *     *   *
*     * *     *
*   *     *   *
* *         * *
*             *
"""


# ============================================================
# 25. Hollow Hourglass Pattern
# ============================================================

"""Problem: Print a hollow hourglass.
Input: n = 5
"""

n = 5

for i in range(n, 0, -1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(2, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""Expected Output:
* * * * *
*       *
  *   *
    *
  *   *
*       *
* * * * *
"""


# ============================================================
# 26. Increasing Number Triangle
# ============================================================

"""Problem: Print numbers from 1 to n in triangle form.
Input: n = 5
"""

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

"""Expected Output:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""


# ============================================================
# 27. Repeating Row Number Triangle
# ============================================================

"""Problem: Print the row number repeatedly.
Input: n = 5
"""

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

"""Expected Output:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""


# ============================================================
# 28. Continuous Number Triangle
# ============================================================

"""Problem: Print continuous numbers in triangle form.
Input: n = 4
"""

n = 4
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

"""Expected Output:
1
2 3
4 5 6
7 8 9 10
"""


# ============================================================
# 29. Reverse Row Number Triangle
# ============================================================

"""Problem: Print numbers in reverse order in every row.
Input: n = 5
"""

n = 5
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

"""Expected Output:
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""


# ============================================================
# 30. Inverted Number Triangle
# ============================================================

"""Problem: Print an inverted number triangle.
Input: n = 5
"""

n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

"""Expected Output:
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""


# ============================================================
# 31. Right-Aligned Number Triangle
# ============================================================

"""Problem: Print a right-aligned number triangle.
Input: n = 5
"""

n = 5
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

"""Expected Output:
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""


# ============================================================
# 32. Pyramid Number Pattern
# ============================================================

"""Problem: Print a number pyramid.
Input: n = 4
"""

n = 4
for i in range(1, n + 1):
    print("  " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()

"""Expected Output:
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1
"""


# ============================================================
# 33. Even Number Triangle
# ============================================================

"""Problem: Print an even number triangle.
Input: n = 5
"""

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j * 2, end=" ")
    print()

"""Expected Output:
2
2 4
2 4 6
2 4 6 8
2 4 6 8 10
"""


# ============================================================
# 34. Odd Number Triangle
# ============================================================

"""Problem: Print an odd number triangle.
Input: n = 5
"""

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j * 2 - 1, end=" ")
    print()

"""Expected Output:
1
1 3
1 3 5
1 3 5 7
1 3 5 7 9
"""


# ============================================================
# 35. Pascal's Triangle
# ============================================================

"""Problem: Print Pascal's Triangle.
Input: n = 5
"""

n = 5
for i in range(n):
    value = 1
    print("  " * (n - i - 1), end="")

    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)

    print()

"""Expected Output:
        1
      1 1
    1 2 1
  1 3 3 1
1 4 6 4 1
"""
