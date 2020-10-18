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

Question4 = input('Question 4: What is the Capital City of Bosnia and Herzegovina?\n a). Sarajevo\n b). Chișinău\n c). Manila''\n d). Sydney\n Which one? ')

check_guess(Question4,'a')

print()

Question5 = input('Question 5: What is the Capital City of Cuba?\n a). Tegucigalpa\n b). Havana\n c). Belmopen''\n d). Malabo\n Which one? ')

check_guess(Question5,'b')

print()

Question6 = input('Question 6: What is the Capital City of Mayanmar?\n a). New Delhi\n b). Dhaka\n c). Laos''\n d). Ney pi daw\n Which one? ')

check_guess(Question6,'d')


print()

Question7 = input('Question 7: What is the Capital City of Peru?\n a). Lima\n b). Havana\n c). Belmopen''\n d). Malabo\n Which one? ')

check_guess(Question7,'a')


print()

Question8 = input('Question 8: What is the Capital City of Sweden?\n a). Oslo\n b). Sri Jayawardenepura Kotte\n c). Sofia''\n d). Stockholm\n Which one? ')

check_guess(Question8,'d')


print()

Question9 = input('Question 9: What is the Capital City of United Arab Emirates?\n a). Abuja\n b). Accra\n c). Abu Dhabi''\n d). Amman\n Which one? ')

check_guess(Question9,'c')


print()

Question10 = input('Question 10: What is the Capital City of Samoa?\n a). Tegucigalpa\n b). Apia\n c). Honiara''\n d). Kingstown\n Which one? ')

check_guess(Question10,'b')


print()

Question11 = input('Question 11: What is the Capital City of Hungary?\n a). Hanoi\n b). Havana\n c). Budapest''\n d). Lisbon\n Which one? ')

check_guess(Question11,'c')


print()

Question12 = input('Question 12: What is the Capital City of Nigeria?\n a). Abuja\n b). Managua\n c). Niamey''\n d). Pyongyang\n Which one? ')

check_guess(Question12,'a')


print()

Question13 = input('Question 13: What is the Capital City of Turkey?\n a). Istanbul\n b). Tunis\n c). Dushanbe''\n d). Ankara\n Which one? ')

check_guess(Question13,'d')


print()


Question14 = input('Question 14: What is the Capital City of Norway?\n a). Oslo\n b). Copenhagen\n c). Belmopen''\n d). Helsinki\n Which one? ')

check_guess(Question14,'a')


print()

Question15 = input('Question 15: What is the Capital City of Qatar?\n a). Kuwait City\n b). Zanzibar\n c). Doha''\n d). Jeddah\n Which one? ')

check_guess(Question15,'c')


print()

Question16 = input('Question 16: What is the Capital City of Finland?\n a). Budapest\n b). Rio\n c). Karakas''\n d). Helsinki\n Which one? ')

check_guess(Question16,'d')


print()

Question17 = input('Question 17: What is the Capital City of France?\n a). Rome\n b). Paris\n c). Madrid''\n d). Warsaw\n Which one? ')

check_guess(Question17,'b')


print()

Question18 = input('Question 18: What is the Capital City of Portugal?\n a). Pnom Phen\n b). Port. Moresby\n c). Port. Lois''\n d). Lisbon\n Which one? ')

check_guess(Question18,'d')


print()

Question19 = input('Question 19: What is the Capital City of Yemen?\n a). Sanna\n b). Mascut\n c). Mogadishu''\n d). Malabo\n Which one? ')

check_guess(Question19,'a')


print()

Question20 = input('Question 20: What is the Capital City of Syria?\n a). Amman\n b). Beirut\n c). Damuscus''\n d). Malabo\n Which one? ')

check_guess(Question20,'c')


if score >= (20):
     print(f'Excellent!!! YOU HAVE SCORED  {score}!')
elif score >= (20*.9):
    print(f'Well done! you have scored {score}!')
elif score >= (20*.8):
    print(f'Good job! you have scored {score}')
elif score >= (20*.75):
    print(f'Nice try! you have scored {score}')
elif score >= (20*.6):
    print(f'Good! you have scored {score}')

