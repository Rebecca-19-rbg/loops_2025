
# # **Python Practice Problems (No Code Included)

# **Directions:** Solve each problem by writing your own Python code. Show outputs where required.


# ### **Problem 1: Print Numbers 1 to 10

# Write a program that prints the numbers from **1 to 10**, each on a new line.
for x in range(1,11):
    print(x)

# ### **Problem 2: Sum of Numbers

# Ask the user for a number **n**, then calculate and display the **sum of all numbers from 1 to n**.

num = int(input("Print any number: "))
sum = 0
for number in range(1, num+1):
    sum += number
print("The sum of the numbers from 1 to", num, "is", sum)


# ### **Problem 3: Factorial Calculator

# Ask the user for a number **n**, then calculate the **factorial** of that number.

def factorial(n):

    factorial = 1

    for i in range(n):
        factorial *= i+1

    return factorial

print(factorial(5))

# *(Example: factorial of 5 is 120)


# ### **Problem 4: Count Vowels**

# Ask the user for a string. Count and print how many **vowels (a, e, i, o, u)** are in the string.
word = input("Type in any word: ")



vowels = set("aeiou")
count = 0
    
for character in word:
        if character in vowels:
            count += 1
            
print(count)




# ### **Problem 5: Print Even Numbers**

# Ask the user for a number **n**, then print all **even numbers** from 2 up to n.

n = int(input("Pick a number: "))

for x in range(0,n+1,2):
    print(x)

# ### **Problem 6: Reverse a String**

# Ask the user for a string, then print the string **backwards**.

string = input("Enter a string: ")

reversed_string = ""

for char in string:
     reversed_string = char + reversed_string
print("Reversed String: ", reversed_string)

print(reversed_string[::-1])

# ### **Problem 7: Multiplication Table**

# Ask the user for a number **n**, then print the **multiplication table** for n from
# n × 1 up to n × 10.



# ### **Problem 8: Count Occurrences**

# Ask the user for **two strings**, a and b.
# Determine how many times **string b appears inside string a**.



# ### **Problem 9: Fibonacci Sequence**

# Ask the user for a number **n**, then print the first **n numbers** of the Fibonacci sequence.

# recursion means a function calls itself


def fibonacci(n):
     if n ==1 or n ==2:
          return 1
     
     return fibonacci(n-1)+fibonacci(n-2)

for i in range(1,10):
     print(fibonacci(i))
     





# ### **Problem 10: Pattern Printing**

# Ask the user for a number **n**, then print a pattern of stars where the first row has 1 star, the second has 2, and so on until row n.

# *(Example for n = 4)*
# *
# **
# ***
# ****



# If you want, I can also turn this into a **Google Doc**, **worksheet**, **PDF**, or **Canvas/Schoology assignment format**.
