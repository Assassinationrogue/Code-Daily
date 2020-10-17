numbers = list(range(1,(100)+1))

for i in numbers:
    if i % 15 == 0:
        print("Fizz Buzz")

    elif i % 3 ==0:
        print("Fizz")
    elif i % 5 ==0:
        print('Buzz')

    elif i > 1:
        for b in range(2, i):
            if (i % b) == 0:
                break
        else:
            print("Prime")


