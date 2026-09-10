# Reverse a number
num = int(input())
res = ""
while num>0:
    res = res + str(num%10)
    num = num//10
print(res)

# Reverse a number without converting it to a string.
num = int(input())
res = 0
while num>0:
    res = res*10+ num%10
    num = num//10
print(res)
