from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Tic-Tac-Toe Game')


SFrame = Frame(root)
SFrame.pack(pady=10)
SFrame.columnconfigure(0, weight=1)

p1sl = Label(SFrame, text="X: ", font="Arial")
p1sl.grid(row=0, column=0, sticky=W+E)
p1s = Label(SFrame, text="", font="Arial")
p1s.grid(row=0, column=0, sticky=W+E)

p2sl = Label(SFrame, text="O: ", font="Arial")
p2sl.grid(row=1, column=0, sticky=W+E)
p2s = Label(SFrame, text="", font="Arial")
p2s.grid(row=1, column=0, sticky=W+E)

BFrame = Frame(root)
BFrame.pack(padx=40, pady=20)
BFrame.columnconfigure(0, weight=1)
BFrame.columnconfigure(1, weight=1)
BFrame.columnconfigure(2, weight=1)


# root.iconbitmap

# intialize global values
global b1, b2, b3, b4, b5, b6, b7, b8, b9
global clicked, count, AiSet, GameMode, Available_Positions, winner, P1_Score, P2_Score
AiSet = False
GameMode = 0
P2_Score = 0
P1_Score = 0

#==============================================================================================================================================================
# core game functions
# Start the game
def Start():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count, AiSet, GameMode, Available_Positions, winner
    clicked = True
    count = 0
    winner = False
    
    b1 = Button(BFrame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(BFrame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(BFrame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(BFrame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(BFrame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(BFrame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(BFrame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(BFrame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(BFrame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    Available_Positions = [b1, b2, b3, b4, b5, b6, b7, b8, b9]   

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


#resets all values
def reset():
    Start()
    global AiSet, P1_Score, P2_Score, GameMode
    AiSet = False
    P2_Score = 0
    P1_Score = 0
    GameMode = 0



def check_winner():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    winning_combinations = [
    (b1, b2, b3),  # Top row
    (b4, b5, b6),  # Middle row
    (b7, b8, b9),  # Bottom row
    (b1, b4, b7),  # Left column
    (b2, b5, b8),  # Middle column
    (b3, b6, b9),  # Right column
    (b1, b5, b9),  # Diagonal from top-left to bottom-right
    (b3, b5, b7)   # Diagonal from top-right to bottom-left
    ]
    global winner
    winner = False
    for combo in winning_combinations:
        if combo[0]['text'] == combo[1]['text'] == combo[2]['text'] != " ":
            combo[0].config(bg="red")
            combo[1].config(bg="red")
            combo[2].config(bg="red")
            winnerTxt = combo[0]['text']
            winner = True
            messagebox.showinfo("Game Over", f"{winnerTxt} wins the game")
            reset()






# button clicked function
def  b_click(b):
    global clicked, count, AiSet, Available_Positions, winner

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        Available_Positions.remove(b)
        check_winner()
        if winner == False:
            gameloop()
        
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        Available_Positions.remove(b)
        check_winner()
        if winner == False:
            gameloop()

    else:
        messagebox.showerror("ERROR", "Hey! thats not how you play")


    if count == 9 and winner == False:
        messagebox.showwarning("Game over","No one wins :(")
        reset()


def SetAi():
    global AiSet
    AiSet = True
    gameloop()

def SetModeEasy():
    global GameMode
    GameMode = 1
    gameloop()

#creat menue
my_menu = Menu(root)
root.config(menu=my_menu)

# create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

AiMenu = Menu(my_menu, tearoff=False)
AiSettings = Menu(AiMenu, tearoff=False)

my_menu.add_cascade(label="Ai Settings", menu=AiMenu)

AiMenu.add_command(label="Turn On Ai", command=SetAi)
AiMenu.add_cascade(label="Ai Mode", menu=AiSettings)
AiSettings.add_command(label="Easy", command=SetModeEasy)


def gameloop():
    global clicked, count, AiSet, GameMode, Available_Positions, winner
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    all_pos = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    
    if AiSet == True and clicked == True and GameMode == 1 and winner == False:
        r = random.randint(0, len(Available_Positions))
        for i in all_pos:
                i.config(state=DISABLED)
        b_click(Available_Positions[r])
    else:
        for i in all_pos:
                i.config(state=NORMAL)
        root.after(1200, gameloop)
    



Start()
gameloop()


root.mainloop()

#==============================================================================================================================================================

