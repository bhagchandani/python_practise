def prime_number(num):
    if num > 2:
        for x in range(2, num//2):
            if num % x == 0:
                print("Not a prime number.")
                break

        else:
            print("Prime Number")
    else:
        print("Not a prime number.")

num = int(input("Enter your number? "))
prime_number(num)