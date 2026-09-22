# String and Text Manipulation – Interview Questions
# ________________________________________
# 1. Remove Spaces from Given Text
# Problem: Write a function to remove all spaces from the input string. Explanation: Remove any whitespace characters.
# Input: "he llo wor ld" Output: "helloworld"

# def remove_spaces(n):
#     result = n.replace(" ", "")
#     print(result)
# remove_spaces("he llo wor ld")

# n="he llo wor ld"
# st=" "
# for i in n:
#     if i!=" ":
#         st+=i
# print(st)

# ________________________________________
# 2. Reverse a String
# Problem: Write a function to reverse the characters in a string. Input: "hello" Output: "olleh"

# def reverse(n):
#     n=n[::-1]
#     print(n)
# reverse("hello")


# ________________________________________
# 3. Reverse a String After Removing Spaces
# Problem: Write a function to reverse a string after removing all spaces. Input: "he llo world" Output: "dlrowolleh"

# def remove_reverse(n):
#     remove=n.replace(" ","")
#     reverse=remove[::-1]
#     print(reverse)
# remove_reverse("he llo world")

# ________________________________________
# 4. Convert Snake Case to Camel Case
# Problem: Convert a string from snake_case to camelCase. Input: "my_variable_name" Output: "myVariableName"

# def camelcase(n):
#     r1=n.replace("_"," ")
#     # r2=r1.title()
#     replace=r1.replace(" ","")
#     replace.upper(replace[2])
#     print(replace)
# camelcase("my_variable_name")


# ________________________________________
# 5. Convert Snake Case to Pascal Case
# Problem: Convert a string from snake_case to PascalCase. Input: "my_variable_name" Output: "MyVariableName"

# def camelcase(n):
#     r1=n.replace("_"," ")
#     r2=r1.title()
#     replace=r2.replace(" ","")
#     print(replace)
# camelcase("my_variable_name")


# ________________________________________
# 6. Convert Camel Case to Snake Case
# Problem: Convert a string from camelCase to snake_case. Input: "myVariableName" Output: "my_variable_name"

# def new(n):
#     st=""
#     for char in n:
#         if char.isupper():
#             st+="_"+char.lower()
#         else:
#             st+=char
#     return st
# print(new("myVariableName"))

# ________________________________________
# 7. Convert Camel Case to Pascal Case
# Problem: Convert a string from camelCase to PascalCase.
# Input: "myVariable" Output: "MyVariable"

# def new(n):
#     st=""
#     for char in n:
#         if char=="m":
#             st+=char.upper()
#         else:
#             st+=char
#     return st
# print(new("myVariable"))

# ________________________________________
# 8. Convert Pascal Case to Camel Case
# Problem: Convert a string from PascalCase to camelCase.
# Input: "MyVariable" Output: "myVariable"

def new(n):
    st=""
    for char in n:
        if char=="M":
            st+=char.lower()
        else:
            st+=char
    return st
print(new("myVariable"))

# ________________________________________
# 9. Convert Pascal Case to Snake Case
# Problem: Convert a string from PascalCase to snake_case.
# Input: "MyVariable" Output: "my_variable"

# ________________________________________
# 10. Convert Text to Camel Case
# Problem: Convert a space-separated sentence into camelCase. Input: "hello world example" Output: "helloWorldExample"
# ________________________________________
# 11. Convert Text to Snake Case
# Problem: Convert a space-separated sentence into snake_case. Input: "hello world example" Output: "hello_world_example"
# ________________________________________
# 12. Convert Text to Pascal Case
# Problem: Convert a space-separated sentence into PascalCase. Input: "hello world example" Output: "HelloWorldExample"
# ________________________________________
# 13. Swap Upper and Lower Case
# Problem: Swap the case of each letter in a given string. Input: "HeLLo" Output: "hEllO"
# ________________________________________
# 14. Separate Digits from Text
# Problem: Extract all digits from a given alphanumeric string. Input: "abc123d4" Output: "1234"
# ________________________________________
# 15. Print Uppercase, Lowercase, Digits, and Special Characters Separately
# Problem: Print each type of character separately from the string. Input: "Abc123!@#" Output:
# Uppercase: A
# Lowercase: b c
# Digits: 1 2 3
# Special Characters: ! @ #
# ________________________________________
# 16. Count of Uppercase, Lowercase, Digits, and Special Characters
# Problem: Count each type of character in a string. Input: "AbC@123x!" Output:
# Uppercase: 2
# Lowercase: 1
# Digits: 3
# Special Characters: 2
# ________________________________________
# 17. Check Password Strength
# Problem: Check if a password contains at least one uppercase, one lowercase, one digit, and one special character. Input: "Pass123!" Output: "Strong Password"
# ________________________________________
# 18. Remove Duplicates in a Given Input
# Problem: Remove duplicate characters from a string. Input: "aabbcc" Output: "abc"
# ________________________________________
# 19. Print Duplicates in a Given String
# Problem: Identify and print duplicate characters in a string. Input: "aabbccde" Output: a b c

# def duplicate(n):
#     count=0
#     for i in n:
#         if count(i)==:

        

# ________________________________________
# 20. Print Next Characters in a Given String
# Problem: Replace each character in the string with its next character. Input: "abc" Output: "bcd"
# ________________________________________
# Would you like to:
# •	🐍 Add code for each question?
# •	📥 Export this as a PDF?
# •	➕ Add more text/case formatting tasks?

# my_list = [10, 20, 30, 20]

# my_list[0] = 100
# my_list.append(50)

# print(my_list)


# 4. Convert Snake Case to Camel Case
# Problem: Convert a string from snake_case to camelCase. Input: "my_variable_name" Output: "myVariableName"
# n="my_variable_name"
# n=n.replace("_v", "V")
# n=n.replce("_n", "N")
# print(n)