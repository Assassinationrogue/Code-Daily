print("Guess the Animal!")
count = 0
q1 = input("Which animal lives in the North Pole? ")
if q1.lower() == "polar bear":
    count  += 1
    answer = "Correct!"
    print(answer)
else:
    answer = "Wrong"
    print(answer)
    q1 = input("Try again: ")
    if q1.lower() == "polar bear":
        count += 1
        answer = "Correct!"
        print(answer)
    else:
        answer = "Wrong"
        print(answer)
        q1 = input("Try again: ")
        if q1.lower() == "polar bear":
            count += 1
            answer = "Correct!"
            print(answer)
        else:
            answer = "Wrong"
            print(answer +"!"+" " + "Your turns for this question is over")


q2 = input("Which is the fastest land animal? ")
if q2.lower() == "cheetah":
    count += 1
    answer = "Correct!"
    print(answer)

else:
    answer = "Wrong"
    print(answer)
    q2 = input("Try again: ")
    if q2.lower() == "cheetah":
        count += 1
        answer = "Correct!"
        print(answer)
    else:
        answer = "Wrong"
        print(answer)
        q2 = input("Try again: ")
        if q2.lower() == "cheetah":
            count += 1
            answer = "Correct!"
            print(answer)
        else:
            answer = "Wrong"
            print(answer +"!"+" " + "Your turns for this question is over")

q3 = input("Which is the largest animal? ")
if q3.lower() == "blue whale":
    count   += 1
    answer = "Correct!"
    print(answer)

else:
    answer = "Wrong"
    print(answer)
    q3 = input("Try again: ")
    if q3.lower() == "blue whale":
        count += 1
        answer = "Correct!"
        print(answer)
    else:
        answer = "Wrong"
        print(answer)
        q3 = input("Try again: ")
        if q3.lower() == "blue whale":
            count += 1
            answer = "Correct!"
            print(answer)
        else:
            answer = "Wrong"
            print(answer +"!"+" " + "Your turns for this question is over")




print(f"Your Score is {count}")
if count == 3:
    print("You are a Genius! Nice!")
elif count == 2:
    print( "You did Well")
else:
    print("You should increase your knowledge")