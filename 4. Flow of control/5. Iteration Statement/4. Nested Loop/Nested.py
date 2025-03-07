""" Nested Loop """


# Example 1: Right-angled triangle pattern using '*'

# Outer loop controls the rows (1 to 5)
for i in range(1, 6):
    for j in range(1, i):  # Inner loop prints '*' (1 less than row number)
        print("*", end='')
    print()  # Moves to the next line after each row


# Example 2: Printing row and column values

# Outer loop runs from 2 to 5
for i in range(2, 6):
    for j in range(1, i):  # Inner loop prints 'i j' format
        print(i, j, end='')
    print()  # Moves to the next line


# Question 1: Number pattern (increasing order)

num = int(input("Enter a Number: "))
for i in range(1, num + 1):  # Outer loop controls the rows
    for j in range(1, i + 1):  # Inner loop prints numbers from 1 to i
        print(j, end=" ")
    print()  # Moves to the next line


# Question 2: Number pattern (decreasing order)

num = int(input("Enter a Number: "))
for i in range(num, 0, -1):  # Outer loop runs in reverse order
    for j in range(1, i + 1):  # Inner loop prints numbers from 1 to i
        print(j, end=" ")
    print()  # Moves to the next line


# Question 3: Alphabet pattern

# Outer loop runs from 1 to 5
for i in range(1, 6):
    for j in range(65, 65 + i):  # Inner loop prints characters from ASCII 65 (A)
        print(chr(j), end=" ")
    print()  # Moves to the next line
