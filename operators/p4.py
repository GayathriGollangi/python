# Take a number from the user and find the sum of its digits.
nums = input()
res = 0
for num in nums:
    res = res + int(num)
print(res)

# without using a string
number = 123456
res = 0
while number>0:
    res = res+number%10
    number = number//10
print(res)