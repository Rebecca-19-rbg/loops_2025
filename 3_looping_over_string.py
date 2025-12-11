# Example Practice:
# Ask the user for a word.

word = input("Type in any word: ")


# Use a for loop to print each letter on a new line.\

for letter in word:
    print(letter)



# Challenge:
# Count how many vowels are in the word.


   
vowels = set("aeiou")
count = 0
    
for character in word:
        if character in vowels:
            count += 1
            
print(count)

