your_input = input("Give an input: ")
try:
    int(your_input)
except ValueError:
    try:
        float(your_input)
    except ValueError:
        print("This is not a number")

if int(your_input)%15 == 0:
        print("Fizz buzz")

elif int(your_input)%3== 0:
        print("fizz")

elif int(your_input)%5 == 0:
        print("buzz")

else:
    print(int(your_input))