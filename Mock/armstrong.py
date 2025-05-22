def arm_strong(n):
    digitlen = len(n)
    n = int(n)
    sum = 0

    while n > 0:
        reminder = n % 10
        n = n // 10
        sum += reminder ** digitlen

    return sum



user_input = input("Enter a number: ")
sum = arm_strong(user_input)

if sum == int(user_input):
    print("Arm Strong")
else:
    print("Not Arm Strong")