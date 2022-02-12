n = int(input("Enter Number: "))

if (n % 2) != 0:
    print("Wired")

else:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")