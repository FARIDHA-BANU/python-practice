lower = int(input("Enter lower value: "))
upper = int(input("Enter upper value: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for a in range(2, num):
            if (num % a) == 0:
                break
        else:
            print(num)
