# String Slicing Operations

s1 = "PythonProgramming"
result_1 = s1[:6]
print(result_1)


result_2 = s1[6:]
print(result_2)

result_3 = s1[-5:]
print(result_3)


result_4 = s1[::2]
print(result_4)


result_5 = s1[::-1]
print(result_5)


s2 = "DataScience"
result_6 = s2[4:]
print(result_6)


s3 = "ArtificialIntelligence"
result_7 = s3[10:]
print(result_7)


s4 = "MachineLearning"
mid_8 = len(s4) // 2
result_8 = s4[mid_8 - 3:mid_8 + 4]
print(result_8)

s5 = "OpenAIChatGPT"
result_9 = s5[::3]
print(result_9)

s6 = "ComputerVision"
result_10 = s6[1:-1]
print(result_10)


# List Slicing Operations


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_result_1 = l1[:5]
print(result_1)

# 2. Extract the last 3 elements from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_result_2 = l1[-3:]
print(list_result_2)

# 3. Extract elements from index 2 to index 7 from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_result_3 = l1[2:8]
print(list_result_3)

# 4. Extract every second element from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_result_4 = l1[::2]
print(list_result_4)

# 5. Reverse [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] using slicing
list_result_5 = l1[::-1]
print(list_result_5)

# 6. Extract ['c', 'd', 'e'] from ['a', 'b', 'c', 'd', 'e', 'f', 'g']
l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list_result_6 = l2[2:5]
print(list_result_6)

# 7. Extract all elements except the first two from ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list_result_7 = l2[2:]
print(list_result_7)

# 8. Extract all elements except the last three from ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list_result_8 = l2[:-3]
print(list_result_8)

# 9. Extract every third element from [10, 20, 30, 40, 50, 60, 70, 80]
l3 = [10, 20, 30, 40, 50, 60, 70, 80]
list_result_9 = l3[::3]
print(list_result_9)

# 10. Extract the list in reverse order skipping every alternate element from [10, 20, 30, 40, 50, 60, 70, 80]
list_result_10 = l3[::-2]
print(list_result_10)

# Complex String Operations

# 1. Input string: "PythonProgramming". Find: first 6 characters, last 5 characters, and concatenate them.
c1 = "PythonProgramming"
complex_result_1 = c1[:6] + c1[-5:]
print(complex_result_1)

# 2. Input string: "DataScience2026". Find: characters from index 2 to 8 and concatenate with reverse string.
c2 = "DataScience2026"
complex_result_2 = c2[2:9] + c2[::-1]
print(complex_result_2)

# 3. Input string: "HelloWorld". Find: positive slice (0:5), negative slice (-5:), and join them.
c3 = "HelloWorld"
complex_result_3 = c3[0:5] + c3[-5:]
print(complex_result_3)

# 4. Input string: "ComputerNetwork". Find: every 2nd character using slicing and concatenate with first 4 characters.
c4 = "ComputerNetwork"
complex_result_4 = c4[::2] + c4[:4]
print(list_result_4)

# 5. Input string: "ArtificialIntelligence". Find: middle part using slicing and last 6 characters using negative slicing.
c5 = "ArtificialIntelligence"
mid_5 = len(c5) // 2
complex_result_5 = c5[mid_5 - 4:mid_5 + 4] + c5[-6:]
print(complex_result_4)

# 6. Input string: "ProgrammingLanguage". Find: characters from index 3 to 12 and concatenate with first 3 characters.
c6 = "ProgrammingLanguage"
complex_result_6 = c6[3:13] + c6[:3]

# 7. Input string: "OpenAIChatGPT". Find: first half and second half using slicing, then concatenate.
c7 = "OpenAIChatGPT"
half_7 = len(c7) // 2
complex_result_7 = c7[:half_7] + c7[half_7:]

# 8. Input string: "MachineLearning". Find: alternate characters using slicing and concatenate with reverse string.
c8 = "MachineLearning"
complex_result_8 = c8[::2] + c8[::-1]

# 9. Input string: "WebDevelopment". Find: last 4 characters using negative slicing and first 5 characters.
c9 = "WebDevelopment"
complex_result_9 = c9[-4:] + c9[:5]

# 10. Input string: "DatabaseManagement". Find: slice from index 4 to 10 and concatenate with slice from -5 to end.
c10 = "DatabaseManagement"
complex_result_10 = c10[4:11] + c10[-5:]

# 11. Input string: "CyberSecurity". Find: characters at even positions and concatenate with characters at odd positions.
c11 = "CyberSecurity"
complex_result_11 = c11[::2] + c11[1::2]

# 12. Input string: "MobileApplication". Find: first 7 characters and last 7 characters using slicing.
c12 = "MobileApplication"
complex_result_12 = c12[:7] + c12[-7:]

# 13. Input string: "CloudComputing". Find: reverse string and concatenate with original first 3 characters.
c13 = "CloudComputing"
complex_result_13 = c13[::-1] + c13[:3]

# 14. Input string: "SoftwareEngineering". Find: substring using negative indexes and concatenate with starting characters.
c14 = "SoftwareEngineering"
complex_result_14 = c14[-11:-1] + c14[:4]

# 15. Input string: "ArtificialNeuralNetwork". Find: characters from index 5 to 15 and concatenate with last 5 characters.
c15 = "ArtificialNeuralNetwork"
complex_result_15 = c15[5:16] + c15[-5:]

# 16. Input string: "DataAnalysisTools". Find: every third character and concatenate with reverse slicing.
c16 = "DataAnalysisTools"
complex_result_16 = c16[::3] + c16[::-1]

# 17. Input string: "Programming12345". Find: remove numbers using slicing and concatenate remaining parts.
c17 = "Programming12345"
complex_result_17 = c17[:11]

# 18. Input string: "StringOperations". Find: first 8 characters, last 8 characters, and combine them.
c18 = "StringOperations"
complex_result_18 = c18[:8] + c18[-8:]

# 19. Input string: "LearningPython". Find: positive slice (2:10), negative slice (-6:-1), and concatenate.
c19 = "LearningPython"
complex_result_19 = c19[2:10] + c19[-6:-1]

# 20. Input string: "ArtificialIntelligence2026". Find: extract year using negative slicing and concatenate with first 10 characters.
c20 = "ArtificialIntelligence2026"
complex_result_20 = c20[-4:] + c20[:10]


# Optional: print results
if __name__ == "__main__":
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)
    print(result_6)
    print(result_7)
    print(result_8)
    print(result_9)
    print(result_10)

    print(list_result_1)
    print(list_result_2)
    print(list_result_3)
    print(list_result_4)
    print(list_result_5)
    print(list_result_6)
    print(list_result_7)
    print(list_result_8)
    print(list_result_9)
    print(list_result_10)

    print(complex_result_1)
    print(complex_result_2)
    print(complex_result_3)
    print(complex_result_4)
    print(complex_result_5)
    print(complex_result_6)
    print(complex_result_7)
    print(complex_result_8)
    print(complex_result_9)
    print(complex_result_10)
    print(complex_result_11)
    print(complex_result_12)
    print(complex_result_13)
    print(complex_result_14)
    print(complex_result_15)
    print(complex_result_16)
    print(complex_result_17)
    print(complex_result_18)
    print(complex_result_19)
    print(complex_result_20)