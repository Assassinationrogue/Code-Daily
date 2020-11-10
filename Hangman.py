import random as rd

word_List = ['jump',
             'using',
             'friendly',
             'effect',
             'rise',
             'expenditure',
             'graduate',
             'secure',
             'stay',
             'chop',
             'opposition',
             'allowance',
             'bowel',
             'holiday',
             'full',
             'impact',
             'safe',
             'slant',
             'inquiry'

             ]


def random_Word():
    return word_List[rd.randint(0, len(word_List) - 1)]


selected_Word = list(random_Word())
print(selected_Word)


dummy = (''.join(selected_Word))

clue = list('-' * len(selected_Word))

Player_One_Guess = []  # stores the values guessed by Player 1
Player_Two_Guess = []  # stores the values guessed by Player 2
AI_Guess = []          # stores the values guessed by AI

print(''.join(clue))

Player = 1

while True:
    print(f"\nPlayer {Player} turn.")
    if Player == 1:
        get_User_Input = input('Guess the letter or guess the whole word: ').lower()

        # for 1 letter
        if get_User_Input in selected_Word:
            # will replace the index of selected word with user input if the input exist in the selected word.
            clue[selected_Word.index(get_User_Input)] = get_User_Input
            print(''.join(clue))

            # to replace the selected word/letter with a -
            selected_Word.insert(selected_Word.index(get_User_Input), '_')
            del selected_Word[selected_Word.index(get_User_Input)]

            # to append every correct guess into the player's list
            for number in range(len(get_User_Input)):
                Player_One_Guess.append(get_User_Input[number])

            if ''.join(clue) == dummy:
                print('Win')
                break

        #  for full word
        else:
            if get_User_Input in ''.join(selected_Word):
                multiple_Inputs = list(get_User_Input)

                for i in range(len(multiple_Inputs)):
                    if multiple_Inputs[i] in ''.join(selected_Word):
                        clue[selected_Word.index(multiple_Inputs[i])] = multiple_Inputs[i]
                        selected_Word.insert(selected_Word.index(multiple_Inputs[i]), '_')
                        del selected_Word[selected_Word.index(multiple_Inputs[i])]

                        # to append every correct guess into the player's list
                        for number in range(len(get_User_Input)):
                            Player_One_Guess.append(get_User_Input[number])

                    if ''.join(clue) == dummy:
                        print('Win')
                        break
        # for n letters
            else:
                multiple_Inputs = get_User_Input
                for i in range(len(multiple_Inputs)):

                    if multiple_Inputs[i] in ''.join(selected_Word):
                        clue[selected_Word.index(multiple_Inputs[i])] = multiple_Inputs[i]
                        selected_Word.insert(selected_Word.index(multiple_Inputs[i]), '_')
                        del selected_Word[selected_Word.index(multiple_Inputs[i])]

                        # to append every correct guess into the player's list
                        for number in range(len(get_User_Input)):
                            Player_One_Guess.append(get_User_Input[number])

                        if ''.join(clue) == dummy:
                            print('Win')
                            break
                    else:

                        print("No it doesn't exists in the word.")
                if ''.join(clue) == dummy:
                    break
            print(''.join(clue))
        print(Player_One_Guess)
        Player = 2

    else:
        get_User_Input = input('Guess the letter or guess the whole word: ').lower()

        # for 1 word
        if get_User_Input in selected_Word:
            # will replace the index of selected word with user input if the input exist in the selected word.
            clue[selected_Word.index(get_User_Input)] = get_User_Input
            print(''.join(clue))

            # to replace the selected word with a -
            selected_Word.insert(selected_Word.index(get_User_Input), '_')
            del selected_Word[selected_Word.index(get_User_Input)]

            # to append every correct guess into the player's list
            for number in range(len(get_User_Input)):
                Player_Two_Guess.append(get_User_Input[number])

            if ''.join(clue) == dummy:
                print('Win')
                break

        else:
            if get_User_Input in ''.join(selected_Word):  # for multiple letters
                multiple_Inputs = list(get_User_Input)

                for i in range(len(multiple_Inputs)):
                    if multiple_Inputs[i] in ''.join(selected_Word):
                        clue[selected_Word.index(multiple_Inputs[i])] = multiple_Inputs[i]
                        selected_Word.insert(selected_Word.index(multiple_Inputs[i]), '_')
                        del selected_Word[selected_Word.index(multiple_Inputs[i])]

                        # to append every correct guess into the player's list
                        for number in range(len(get_User_Input)):
                            Player_Two_Guess.append(get_User_Input[number])

                    if ''.join(clue) == dummy:
                        print('Win')
                        break
            else:
                multiple_Inputs = get_User_Input
                for i in range(len(multiple_Inputs)):

                    if multiple_Inputs[i] in ''.join(selected_Word):
                        clue[selected_Word.index(multiple_Inputs[i])] = multiple_Inputs[i]
                        selected_Word.insert(selected_Word.index(multiple_Inputs[i]), '_')
                        del selected_Word[selected_Word.index(multiple_Inputs[i])]

                        # to append every correct guess into the player's list
                        for number in range(len(get_User_Input)):  #
                            Player_Two_Guess.append(get_User_Input[number])

                        if ''.join(clue) == dummy:
                            print('Win')
                            break
                    else:
                        print("No it doesn't exists in the word.")
                if ''.join(clue) == dummy:
                    break
            print(''.join(clue))
        print(Player_Two_Guess)
        Player = 1

    if ''.join(clue) == dummy:
        break
    # for n number of words
