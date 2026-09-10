# Check whether a number is a palindrome without converting it to a string.

num = int(input())
original = num
res =0
while num>0:
    res = num%10+res*10
    num = num//10
print(res)
if original == res:
    print("palindrome")
else:
    print("Not palindrome")