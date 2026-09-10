# Take a sentence and count the number of words.
sentence = "Hello world"
count =0
for char in sentence:
    if char == " ":
        count +=1
print(count+1)