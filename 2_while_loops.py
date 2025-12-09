
#        NOTES ON WHILE LOOPS

# while loop = execute some code WHILE some contition remains true


# i deleted the other one on accident :(



# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old.")




# food = input("Enter a food you like (q to quit):")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit):")
# print("bye")


# food_list = []
# while not food == "quit":
#     print("I like", food, "too!")




# num = int(input("Enter a # between 1- 10:"))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1- 10:"))
# print(f"Your number is {num}")


# Given:
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.

color = 0

while color < len(colors):
    if colors[color] == "yellow":
        break
    print(colors[color])
    color += 1
    






