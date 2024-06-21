import random
arr = [random.randint(1,1000),random.randint(1,1000), random.randint(1,1000)]
def sum(num1, num2, num3):
    sum = 0
    for num in arr:
        sum = sum + num
    return sum

print(sum(*arr))


