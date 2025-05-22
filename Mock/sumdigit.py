def sum_of_digit(n):
    sum = 0
    while n > 0:
        reminder = n % 10
        n = n // 10
        sum += reminder

    print(sum)



user_input = int(input("Enter a number: "))
sum_of_digit(user_input)

