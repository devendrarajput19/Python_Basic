# 1- Reverse each word in sentence

sent = input("Enter a sentence = ")

reversed_words = " ".join(word[::-1] for word in sent.split())

print(f"Original Sentence = {sent}")
print(f"Reversed sentence = {reversed_words}")

# 2 - Using Loop

sent = input("Enter a sentence = ")

words = sent.split()
reversed_list = []

for word in words:
    reversed_list.append(word[::-1])

reversed_words = " ".join(reversed_list)

print(f"Original Sentence = {sent}")
print(f"Reversed Sentence  = {reversed_words}")