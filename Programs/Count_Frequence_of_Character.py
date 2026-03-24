strng = input("Enter a string: ")

# Count frequency using dictionary
freq = {}
for char in strng:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(f"String : {strng}")
for char, count in freq.items():
    print(f"  '{char}' → {count}")