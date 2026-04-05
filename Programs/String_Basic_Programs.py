# 1 - Remove spaces from string

string = input("Enter any text = ")

result = string.replace(" ", "")    #using replace function
result2 = string.strip()            #remove only leading and trailing space
result3 = string.lstrip()           #remove only leading space
result4 = string.rstrip()           #remove only trailing space

print(f"Original Text = {string}")
print(f"Updated Text = {result}")
print(f"Updated Text = {result2}")

# 2- Replace a word in string

import re    # Regular expression
string = input("Enter any text = ")
new_word = input("Enter word to replace = ")

result = string.replace("Java", new_word)
result1 = re.sub("Java", new_word, string, flags=re.IGNORECASE)   # replace the word and ignore the case

print(f"Updated string = {result}")
print(f"Updated string = {result1}")

# 3 - find length of a string without len

string = input("Enter a string = ")

count = 0
for ch in string:
    count += 1

print(f"string is having = {count} character")
