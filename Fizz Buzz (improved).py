numbers = list(range(1, 100 + 1))  # Gives a list of numbers from 1 to 100.

for i in numbers:   # 'i' as temp variable for numbers
    if i % 15 == 0:  # if the element of a list is multiple of both 3 and 5 or (3*5) then it will return 0.
        print("Fizz Buzz")

    elif i % 3 ==0:  # if the element of a list is multiple of 3 then it will return 0.
        print("Fizz")
    elif i % 5 ==0:  # if the element of a list is multiple of 5 then it will return 0.
        print('Buzz')

    elif i > 1:
        for b in range(2, i):
            if (i % b) == 0:
                break
        else:
            print("Prime")


