# 1 - map words and its length in dictionary

words = input("Enter Words with spaces = ").split()

word_length = {word: len(word) for word in words}

print(f"Words = {words}")
print(f"Dictionary = {word_length}")

# 2- Using loop

words = input("Enter words with spaces = ").split()

dictionary = {}
for word in words:
    dictionary[word] = len(word)

print(f"Words = {words}")
print(f"Dictionary = {dictionary}")