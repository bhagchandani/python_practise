def fibonnaci(length):
    fibo = []
    if length <= 0:
        return []

    fibo = [0]
    if length == 1:
        return fibo

    fibo.append(1)

    for i in range(2,(length)):
        newvalue = fibo[i-1] + fibo[i-2]
        fibo.append(newvalue)

    return fibo

asked_length = int(input("Enter the length: "))
print(fibonnaci(asked_length))