# Find the factorial of a number without using any built-in function.

num = int(input())
res = 1
while num>0:
    res = res*num
    num = num-1
print(res)