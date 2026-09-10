# Count how many vowels are present in a string.
word = "hEllo"
word = word.lower()
count = 0
for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char =='o' or char == 'u':
        count = count+1
print(count)
