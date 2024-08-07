n = int(input("Enter a number: "))
if n <= 1:
    print("nap")
else:
    for i in range(2, n):
        if n % i == 0:
            print("nap")
            break
    else:
        print("Prime")
