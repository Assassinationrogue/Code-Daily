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

hangman_frames = [r""""
    +============o
    |  /         |   
    | /          |   
    |/
    |
    |
    |
    |
    |
    |
   / \
 ======================= """, r"""
    +============o
    |   /        |   
    |  /         | 
    | /         _|_
    |/         (___)     
    |
    |
    |
    |
    |
    |
   / \
 ======================= """, r"""
    +============o
    |   /        |   
    |  /         | 
    | /         _|_
    |/         (___)     
    |            |   
    |
    |
    |
    |
    |
   / \
 ======================= """, r"""
    +============o
    |   /        |   
    |  /         | 
    | /         _|_
    |/         (___)     
    |          __|__   
    |           
    |
    |
    |
    |
   / \
 ======================= """, r"""
    +============o
    |   /        |   
    |  /         | 
    | /         _|_
    |/         (___)     
    |          __|__   
    |         /  |  \  
    |        /   |   \   
    |
    |
    |
   / \
 ======================= """, r"""
    +============o
    |   /        |   
    |  /         | 
    | /         _|_
    |/         (___)     
    |          __|__   
    |         /  |  \  
    |        /   |   \   
    |            |
    |
    |
   / \
 ======================= """, r"""
    +============o
    |   /        |   
    |  /         | 
    | /         _|_
    |/         (___)     
    |          __|__   
    |         /  |  \  
    |        /   |   \   
    |            |
    |           / \
    |          
   / \
 ======================= """, r"""
    +============o
    |   /        |   
    |  /         | 
    | /         _|_
    |/         (___)     
    |          __|__   
    |         /  |  \  
    |        /   |   \   
    |        |   |   | 
    |           / \
    |          /   \     
   / \
 ======================= """, r"""
   +============o
    |   /        |   
    |  /         | 
    | /         _|_
    |/         (___)     
    |          __|__   
    |         /  |  \  
    |        /   |   \   
    |        |   |   | 
    |           / \
    |          /   \     
   / \        _|   |_
 ======================= """]


def random_Word():
    return word_List[rd.randint(0, len(word_List) - 1)]


selected_Word = list(random_Word())

dummy = (''.join(selected_Word))
dummy2 = []

clue = list('-' * len(selected_Word))

Player_One_Guess = []  # stores the values guessed by Player 1
Player_Two_Guess = []  # stores the values guessed by Player 2
AI_Guess = []  # stores the values guessed by AI

# Ai will select random letters from word
for num in range(len(selected_Word)):
    if selected_Word[num] != '_':
        dummy2.clear()
        dummy2.append(selected_Word[num])

random_pick = rd.choice(dummy2)

Player = 1

Score = 0

Player_One_Life = 8
Player_Two_Life = 8

print("""
        Select mode:
        a) 1-Player
        b) 2-Player
        """, end="")

mode_Input = input('-')
print('\n')

if mode_Input == 'b':
    print('   --2-Player Mode selected--     ')
    while True:

        print(f"\nPlayer {Player} turn.")

        if Player == 1:
            if Player_One_Life > 0:
                print(hangman_frames[8 - Player_One_Life])
                print(''.join(clue))
                get_User_Input = input('Guess the letter or guess the whole word: ').lower()

                # for 1 letter
                if get_User_Input in selected_Word:
                    Player_One_Guess.append(get_User_Input)
                    # will replace the index of selected word with user input if the input exist in the selected word.
                    clue[selected_Word.index(get_User_Input)] = get_User_Input
                    print(''.join(clue))

                    # to replace the selected word/letter with a -
                    selected_Word.insert(selected_Word.index(get_User_Input), '_')
                    del selected_Word[selected_Word.index(get_User_Input)]

                    if ''.join(clue) == dummy:
                        print(f'Player: {Player} Win')
                        break

                #  for full word
                else:
                    if get_User_Input in ''.join(selected_Word):
                        multiple_Inputs = list(get_User_Input)

                        for i in range(len(multiple_Inputs)):
                            if multiple_Inputs[i] in ''.join(selected_Word):
                                Player_One_Guess.append(get_User_Input[i])
                                clue[selected_Word.index(multiple_Inputs[i])] = multiple_Inputs[i]
                                selected_Word.insert(selected_Word.index(multiple_Inputs[i]), '_')
                                del selected_Word[selected_Word.index(multiple_Inputs[i])]

                            if ''.join(clue) == dummy:
                                print(f'Player: {Player} Win')
                                break
                    # for n letters
                    else:
                        multiple_Inputs = get_User_Input
                        for i in range(len(multiple_Inputs)):

                            if multiple_Inputs[i] in ''.join(selected_Word):
                                Player_One_Guess.append(get_User_Input[i])
                                clue[selected_Word.index(multiple_Inputs[i])] = multiple_Inputs[i]
                                selected_Word.insert(selected_Word.index(multiple_Inputs[i]), '_')
                                del selected_Word[selected_Word.index(multiple_Inputs[i])]

                                if ''.join(clue) == dummy:
                                    print(f'Player: {Player} Win')
                                    break
                            else:
                                if multiple_Inputs[i] in ''.join(Player_One_Guess):
                                    print(f'{multiple_Inputs[i]} already has been guessed by Player 1')
                                elif multiple_Inputs[i] in ''.join(Player_Two_Guess):
                                    print(f'{multiple_Inputs[i]} already has been guessed by Player 2')
                                else:
                                    print(f"No {multiple_Inputs[i]} doesnt exists in the word.")
                                    Player_One_Life -= 1
                        if ''.join(clue) == dummy:
                            break

            else:
                print(hangman_frames[8 - Player_One_Life])
                print(f'Player: {Player} is hanged.')
            print(chr(27) + "[2J")
            Player = 2

        else:
            if Player_Two_Life > 0:
                print(hangman_frames[8 - Player_Two_Life])
                print(''.join(clue))
                get_User_Input = input('Guess the letter or guess the whole word: ').lower()

                # for 1 word
                if get_User_Input in selected_Word:
                    Player_Two_Guess.append(get_User_Input)
                    # will replace the index of selected word with user input if the input exist in the selected word.
                    clue[selected_Word.index(get_User_Input)] = get_User_Input
                    print(''.join(clue))

                    # to replace the selected word with a -
                    selected_Word.insert(selected_Word.index(get_User_Input), '_')
                    del selected_Word[selected_Word.index(get_User_Input)]

                    if ''.join(clue) == dummy:
                        print(f'Player: {Player} Win')
                        break

                else:
                    if get_User_Input in ''.join(selected_Word):  # for multiple letters
                        multiple_Inputs = list(get_User_Input)

                        for i in range(len(multiple_Inputs)):
                            if multiple_Inputs[i] in ''.join(selected_Word):
                                Player_Two_Guess.append(get_User_Input[i])
                                clue[selected_Word.index(multiple_Inputs[i])] = multiple_Inputs[i]
                                selected_Word.insert(selected_Word.index(multiple_Inputs[i]), '_')
                                del selected_Word[selected_Word.index(multiple_Inputs[i])]

                            if ''.join(clue) == dummy:
                                print(f'Player: {Player} Win')
                                break
                    else:
                        multiple_Inputs = get_User_Input
                        for i in range(len(multiple_Inputs)):

                            if multiple_Inputs[i] in ''.join(selected_Word):
                                Player_Two_Guess.append(get_User_Input[i])
                                clue[selected_Word.index(multiple_Inputs[i])] = multiple_Inputs[i]
                                selected_Word.insert(selected_Word.index(multiple_Inputs[i]), '_')
                                del selected_Word[selected_Word.index(multiple_Inputs[i])]

                                if ''.join(clue) == dummy:
                                    print(f'Player: {Player} Win')
                                    break
                            else:
                                if multiple_Inputs[i] in ''.join(Player_One_Guess):
                                    print(f'{multiple_Inputs[i]} already been has guessed by Player 1')
                                elif multiple_Inputs[i] in ''.join(Player_Two_Guess):
                                    print(f'{multiple_Inputs[i]} already been has guessed by Player 2')
                                else:
                                    print(f"No {multiple_Inputs[i]} doesnt exists in the word.")
                                    Player_Two_Life -= 1
                        if ''.join(clue) == dummy:
                            break
                        if Player_Two_Life == 0:
                            break
            else:
                print(hangman_frames[8 - Player_Two_Life])
                print(f'Player: {Player} is hanged.')
            print(chr(27) + "[2J")
            Player = 1

        if ''.join(clue) == dummy:
            break

elif mode_Input == 'a':
    print('   --1-Player Mode selected--     ')
    while True:

        print(f"\nPlayer {Player} turn.")

        if Player == 1:
            if Player_One_Life > 0:
                print(hangman_frames[8 - Player_One_Life])
                print(''.join(clue))
                get_User_Input = input('Guess the letter or guess the whole word: ').lower()

                # for 1 letter
                if get_User_Input in selected_Word:
                    Player_One_Guess.append(get_User_Input)
                    # will replace the index of selected word with user input if the input exist in the selected word.
                    clue[selected_Word.index(get_User_Input)] = get_User_Input
                    print(''.join(clue))

                    # to replace the selected word/letter with a -
                    selected_Word.insert(selected_Word.index(get_User_Input), '_')
                    del selected_Word[selected_Word.index(get_User_Input)]

                    if ''.join(clue) == dummy:
                        print(f'Player: {Player} Win')
                        break

                #  for full word
                else:
                    if get_User_Input in ''.join(selected_Word):
                        multiple_Inputs = list(get_User_Input)

                        for i in range(len(multiple_Inputs)):
                            if multiple_Inputs[i] in ''.join(selected_Word):
                                Player_One_Guess.append(get_User_Input[i])
                                clue[selected_Word.index(multiple_Inputs[i])] = multiple_Inputs[i]
                                selected_Word.insert(selected_Word.index(multiple_Inputs[i]), '_')
                                del selected_Word[selected_Word.index(multiple_Inputs[i])]

                            if ''.join(clue) == dummy:
                                print(f'Player: {Player} Win')
                                break
                    # for n letters
                    else:
                        multiple_Inputs = get_User_Input
                        for i in range(len(multiple_Inputs)):

                            if multiple_Inputs[i] in ''.join(selected_Word):
                                Player_One_Guess.append(get_User_Input[i])
                                clue[selected_Word.index(multiple_Inputs[i])] = multiple_Inputs[i]
                                selected_Word.insert(selected_Word.index(multiple_Inputs[i]), '_')
                                del selected_Word[selected_Word.index(multiple_Inputs[i])]

                                if ''.join(clue) == dummy:
                                    print(f'Player: {Player} Win')
                                    break
                            else:
                                if multiple_Inputs[i] in ''.join(Player_One_Guess):
                                    print(f'{multiple_Inputs[i]} already has been guessed by Player 1')
                                elif multiple_Inputs[i] in ''.join(Player_Two_Guess):
                                    print(f'{multiple_Inputs[i]} already has been guessed by Player 2')
                                else:
                                    print(f"No {multiple_Inputs[i]} doesnt exists in the word.")
                                    Player_One_Life -= 1
                        if ''.join(clue) == dummy:
                            break

            else:
                print(hangman_frames[8 - Player_One_Life])
                print(f'Player: {Player} is hanged.')
            print(chr(27) + "[2J")
            print(len(dummy2))
            Player = 'AI'

        else:

            for num in range(len(selected_Word)):
                if selected_Word[num] != '_':
                    dummy2.clear()
                    dummy2.append(selected_Word[num])
            if Player_Two_Life > 0:
                print(hangman_frames[8 - Player_Two_Life])
                print(''.join(clue))
                print(f'AI guessed a letter : {dummy2[0].lower()}')

                # for 1 letter
                if dummy2[0] in selected_Word:
                    AI_Guess.append(dummy2[0])
                    # will replace the index of selected word with user input if the input exist in the selected word.
                    clue[selected_Word.index(dummy2[0])] = dummy2[0]
                    print(''.join(clue))

                    # to replace the selected word/letter with a -
                    selected_Word.insert(selected_Word.index(dummy2[0]), '_')
                    del selected_Word[selected_Word.index(dummy2[0])]

                    if ''.join(clue) == dummy:
                        print(f'{Player} Win')
                        break
                    Player = 1

            else:
                print(hangman_frames[8 - Player_Two_Life])
                print(f'Player: {Player} is hanged.')
            print(chr(27) + "[2J")

            if ''.join(clue) == dummy:
                break
