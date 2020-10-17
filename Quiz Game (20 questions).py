score = 0
def check_guess(question,answer):
    global score
    still_guessing = True
    attempt = 1
    while still_guessing and attempt <3:
        if question.lower() == answer.lower():
            print('Correct Answer')
            score = score+1
            still_guessing = False
        else:
            if attempt <3:
                question = input('Sorry wrong answer. Try again: ')
            attempt = attempt +1

    if attempt == 3:
        print('The Correct answer is '+ answer )

Question1 = input('Question 1: What is the Capital City of Argentina?\n a). Madrid\n b). Tblisi\n c). Buenos Aires\n d). Baku\n Which one? ')

check_guess(Question1,'c')

print()

Question2 = input('Question 2: What is the Capital City of Ireland?\n a). Riga\n b). Dublin\n c). Reykjavik''\n d). Warsaw\n Which one? ')

check_guess(Question2,'b')

print()

Question3 = input('Question 3: What is the Capital City of Mongolia?\n a). Ulan Bator\n b). Chișinău\n c). Minsk''\n d). Lisbon\n Which one? ')

check_guess(Question3,'a')


print()

Question3 = input('Question 3: What is the Capital City of Mongolia?\n a). Ulan Bator\n b). Chișinău\n c). Minsk''\n d). Lisbon\n Which one? ')

check_guess(Question3,'a')
