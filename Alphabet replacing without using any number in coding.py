decoy = list(range((ord('A')),ord('D')))
Alphabets = list(range((ord('A')),(ord('Z'))+(decoy.index(ord('B')))))
AlphabetsTwo = ['A','G','C','T']
AlphabetsOne =['U','C','G','A']

def alphabetReplacer (removeAlphabet,NewAlphabet,listName):
    position = listName.index(ord(removeAlphabet))
    remove = listName.remove(ord(removeAlphabet))
    insert = listName.insert((position),ord(NewAlphabet))

    return remove,insert

Gee = input("Enter an Alphabet: ")
for i in Gee:

    if Alphabets[Alphabets.index(ord('A'))] == ord(Gee):
        g = alphabetReplacer('A', 'U', listName=Alphabets)
        print(chr(Alphabets[Alphabets.index(ord('U'))]))


    elif Alphabets[Alphabets.index(ord('G'))] == ord(Gee):
        g = alphabetReplacer('G', 'C', listName=Alphabets)
        print(chr(Alphabets[Alphabets.index(ord('C'))]))

    elif Alphabets[Alphabets.index(ord('C'))] == ord(Gee):
        g = alphabetReplacer('C', 'G', listName=Alphabets)
        print(chr(Alphabets[Alphabets.index(ord('G'))]))

    elif Alphabets[Alphabets.index(ord('T'))] == ord(Gee):
        g = alphabetReplacer('T', 'A', listName=Alphabets)
        print(chr(Alphabets[Alphabets.index(ord('A'))]))

