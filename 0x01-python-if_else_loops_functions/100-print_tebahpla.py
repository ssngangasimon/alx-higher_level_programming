# print the ASCII alphabet in reverse order

result = ""
for i in range(25, -1, -1):
    if i % 2 == 0:
        result += chr(122 - i)  # lowercase
    else:
        result += chr(90 - (i - 1))  # uppercase

# Print the result in one line
print(result)

