import random as rd
from tkinter import *


song_Name = "Love the Way you lie"
artist = "Eminem"
featured_Artist = "Rihanna"
album = "Recovery"
released = "2010"
genre = "Hip-hop/rap"


Song1 = {"Artist": artist, "Featured Artist": featured_Artist, "Album": album, "Released": released, "Genre": genre}


# configuration of the GUI
mainBody = Tk()
mainBody.title("Value Guessing")
mainBody.iconbitmap("Melody.ico")
mainBody.geometry("750x300") # widhtxHeight
mainBody.configure(bg="white")
mainBody.resizable(0,0)


# Main frame
Labelframe1 = Label(mainBody, text="Song: Love the Way you lie",font=("times new roman",18,'bold'),bd=12,bg="#12a4d9",fg="white",anchor="w").pack(fill=X)


labelFrame2 = LabelFrame(mainBody, text="Guess the values", font=("times new roman", 11, "bold"),bg="#d9138a",fg="white")
labelFrame2.place(x=0, y=60, relwidth=1, relheight=.4)


labelFrame3 = LabelFrame(mainBody, text="Result", font=("times new roman", 11, "bold"),bg="#e8d21d",fg="black")
labelFrame3.place(x=0, y=200, relwidth=1, relheight=.3)





# followers of mainframe


valueEntry = Entry(labelFrame2,bd=3,width=50)
valueEntry.grid(row=0, column=2)

textField = Text(labelFrame3, height=5, width=92,bg="#E8E8E8",cursor="xterm",undo=True)
textField.grid(row=0,column=0)
textField.configure(state=DISABLED)

def checking():

    getValue = valueEntry.get()
    
    if getValue == Song1["Artist"]:

        textField.configure(state=NORMAL)

        resultLabel = (f'{Song1["Artist"]} is the Artist of this song.\n')

        textField.insert(END, resultLabel)

        textField.configure(state=DISABLED)
    
    if getValue == Song1["Featured Artist"]:

        textField.configure(state=NORMAL)

        resultLabel = (f'{Song1["Featured Artist"]} is the Featured Artist of this song.\n')

        textField.insert(END, resultLabel)

        textField.configure(state=DISABLED)

    
    if getValue == Song1["Album"]:
        textField.configure(state=NORMAL)

        resultLabel = (f'{Song1["Album"]} is the Album of this song.\n')

        textField.insert(END, resultLabel)
        
        textField.configure(state=DISABLED)


    if getValue == Song1["Released"]:

        textField.configure(state=NORMAL)
        resultLabel =(f'This song was released on {Song1["Released"]}.\n')
        textField.insert(END, resultLabel)
        textField.configure(state=DISABLED)
    
    if getValue == Song1["Genre"]:
        textField.configure(state=NORMAL)
        resultLabel = (f'{Song1["Genre"]} is the Genre of this song.\n')
        textField.insert(END, resultLabel)
        textField.configure(state=DISABLED)
        
        

        return
        
 
def checkingWithKeyBind(event):

    getValue = valueEntry.get()
    
    if getValue == Song1["Artist"]:
        textField.configure(state=NORMAL)
        resultLabel = (f'{Song1["Artist"]} is the Artist of this song.\n')
        textField.insert(END, resultLabel)
        textField.configure(state=DISABLED)

        if getValue != Song1["Artist"]:
            textField.configure(state=NORMAL)
            resultLabel = ("Use proper cases or the value doesn't belongs to the of this song.")
            textField.insert(END, resultLabel)
            textField.configure(state=DISABLED)
    
    if getValue == Song1["Featured Artist"]:
        textField.configure(state=NORMAL)
        resultLabel = (f'{Song1["Featured Artist"]} is the Featured Artist of this song.\n')
        textField.insert(END, resultLabel)
        textField.configure(state=DISABLED)

        if getValue != Song1["Featured Artist"]:
            textField.configure(state=NORMAL)
            resultLabel = ("Use proper cases or the value doesn't belongs to the of this song.")
            textField.insert(END, resultLabel)
            textField.configure(state=DISABLED)
    
    if getValue == Song1["Album"]:
        textField.configure(state=NORMAL)
        resultLabel = (f'{Song1["Album"]} is the Album of this song.\n')
        textField.insert(END,resultLabel)
        textField.configure(state=DISABLED)

        if getValue != Song1["Album"]:
            textField.configure(state=NORMAL)
            resultLabel = ("Use proper cases or the value doesn't belongs to the of this song.")
            textField.insert(END, resultLabel)
            textField.configure(state=DISABLED)

    if getValue == Song1["Released"]:
        textField.configure(state=NORMAL)
        resultLabel =(f'This song was released on {Song1["Released"]}.\n')
        textField.insert(END, resultLabel)
        textField.configure(state=DISABLED)

        if getValue != Song1["Released"]:
            textField.configure(state=NORMAL)
            resultLabel = ("Use proper cases or the value doesn't belongs to the of this song.")
            textField.insert(END, resultLabel)
            textField.configure(state=DISABLED)
    
    if getValue == Song1["Genre"]:
        textField.configure(state=NORMAL)
        resultLabel = (f'{Song1["Genre"]} is the Genre of this song.\n')
        textField.insert(END, resultLabel)
        textField.configure(state=DISABLED)
        
        if getValue != Song1["Genre"]:
            textField.configure(state=NORMAL)
            resultLabel = ("Use proper cases or the value doesn't belongs to the of this song.")
            textField.insert(END, resultLabel)
            textField.configure(state=DISABLED)
       
        return
        

def refreshing():
    
    valueEntry.delete(0, END)
    textField.configure(state=NORMAL)
    textField.delete("1.0", END)
    textField.configure(state=DISABLED)
    
    # will also delete the answer
    return

def refreshingBinding(event):
    
    valueEntry.delete(0, END)
  
    # will also delete the answer
    return


# widgets inside second frame

songLabel1 = Label(labelFrame2, text="Search a value realted to this song", font=("times new roman", 11, "bold"), bg="#d9138a", fg="white").grid(row=0, column=0)

blankLabel1= Label(labelFrame2,text="             ",bg="#d9138a",fg="white").grid(row=0,column=1)

blankLabel1= Label(labelFrame2,text="             ",bg="#d9138a",fg="white").grid(row=0,column=3)

checkButton = Button(labelFrame2, text="Check", cursor="hand2",activeforeground="white",bg="#e2d810",font=("times new roman",9,"bold"),relief=RAISED,command=checking)
checkButton.place(x=350,y=60)

refreshButton = Button(labelFrame2, text="Refresh", cursor="hand2",relief=RAISED,activeforeground="white",bg="#e2d810",font=("times new roman",9,"bold"),command=refreshing)
refreshButton.place(x=400,y=60)

exitButton = Button(labelFrame2, text="Exit", cursor="hand2",relief=RAISED,activeforeground="white",bg="#cf1578",font=("times new roman",9,"bold"),command=mainBody.quit)
exitButton.place(x=460,y=60)

# widgets inside third frame

valueEntry.bind("<Return>", checkingWithKeyBind)
valueEntry.bind("<Delete>",refreshingBinding)



mainBody.mainloop()