song_name = "Love the way you lie"
artist = "Eminem"
featured_artist = "Rihanna"
album = "Recovery"
released = 2010
genre = "Hip-Hop/Rap"
recorded = 2009
length = (4 * 60) + 23  #

songDictionary = {"Song": song_name, "Artist": artist, "Featured Artist": featured_artist, "Album": album,
                  "Released on ": released, "Genre": genre, "Recorded on": recorded, "Length": f"{length} sec."}
key_list = list(songDictionary.keys())
value_list = list(songDictionary.values())
des = ("-"*len(song_name))
print(f'{song_name}\n{des}\nType one word related to this song: ')
Key_values = input()


def guessIt(Keys=None, Values=Key_values):
    if Keys is None:
        Keys = key_list
    if Values in value_list:
        Key = Keys[value_list.index(Key_values)]
        print(f'{Values} is the {Key} of this song.')
    else:
        print('Not in the list')
    return True


guessIt()

print("\n")


for song in songDictionary:
    print(f'{key_list[value_list.index(songDictionary[song])]} : {songDictionary[song]}')
