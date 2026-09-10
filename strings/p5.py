# Check whether a string is a palindrome.
word = "madam"
res = ""
for char in word:
    res = char + res
if res == word:
    print("palindrome")
else:
    print("Not a palindrome")