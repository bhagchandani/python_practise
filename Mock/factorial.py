def factorial(num):
    result = num
    for i in range(1,num):
        result *= i
    return result

num = int(input("Enter a number? "))
print(factorial(num))