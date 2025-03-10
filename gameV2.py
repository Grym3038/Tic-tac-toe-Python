from tkinter import *
from tkinter import messagebox
import random
from MiniMax import Minimax

root = Tk()
root.title('Tic-Tac-Toe Game')

# Score Frame
SFrame = Frame(root)
SFrame.pack(fill="x", pady=10)
SFrame.columnconfigure(0, weight=1)
SFrame.columnconfigure(1, weight=1)

p1_label = Label(SFrame, text="X: 0", font=("Helvetica", 16))
p1_label.grid(row=0, column=0, sticky="w", padx=40)
p2_label = Label(SFrame, text="O: 0", font=("Helvetica", 16))
p2_label.grid(row=0, column=1, sticky="e", padx=40)

# Board Frame
BFrame = Frame(root)
BFrame.pack(padx=40, pady=20)
for i in range(3):
    BFrame.columnconfigure(i, weight=1)

minimax = Minimax()

# Global game state variables
clicked = True        # True means it's human ("X") turn; False means AI ("O") turn.
count = 0
AiSet = False
GameMode = 0          # 1: Easy, 2: Impossible
P1_Score = 0
P2_Score = 0
winner = False
Available_Positions = []  # Will hold the Button objects

# Dictionary to hold buttons by their name
buttons = {}

def Start():
    global clicked, count, winner, Available_Positions, buttons
    # Reset GUI board and minimax board
    clicked = True
    count = 0
    winner = False
    minimax.board = ["" for _ in range(9)]
    
    # Create buttons and store with an identifier
    buttons = {
        "b1": Button(BFrame, text="", font=("Helvetica", 20), height=3, width=6,
                     bg="SystemButtonFace", command=lambda: b_click(buttons["b1"], "b1")),
        "b2": Button(BFrame, text="", font=("Helvetica", 20), height=3, width=6,
                     bg="SystemButtonFace", command=lambda: b_click(buttons["b2"], "b2")),
        "b3": Button(BFrame, text="", font=("Helvetica", 20), height=3, width=6,
                     bg="SystemButtonFace", command=lambda: b_click(buttons["b3"], "b3")),
        "b4": Button(BFrame, text="", font=("Helvetica", 20), height=3, width=6,
                     bg="SystemButtonFace", command=lambda: b_click(buttons["b4"], "b4")),
        "b5": Button(BFrame, text="", font=("Helvetica", 20), height=3, width=6,
                     bg="SystemButtonFace", command=lambda: b_click(buttons["b5"], "b5")),
        "b6": Button(BFrame, text="", font=("Helvetica", 20), height=3, width=6,
                     bg="SystemButtonFace", command=lambda: b_click(buttons["b6"], "b6")),
        "b7": Button(BFrame, text="", font=("Helvetica", 20), height=3, width=6,
                     bg="SystemButtonFace", command=lambda: b_click(buttons["b7"], "b7")),
        "b8": Button(BFrame, text="", font=("Helvetica", 20), height=3, width=6,
                     bg="SystemButtonFace", command=lambda: b_click(buttons["b8"], "b8")),
        "b9": Button(BFrame, text="", font=("Helvetica", 20), height=3, width=6,
                     bg="SystemButtonFace", command=lambda: b_click(buttons["b9"], "b9"))
    }
    
    # Reset the available positions list
    Available_Positions.clear()
    for key in buttons:
        Available_Positions.append(buttons[key])
    
    # Place the buttons on the grid
    buttons["b1"].grid(row=0, column=0)
    buttons["b2"].grid(row=0, column=1)
    buttons["b3"].grid(row=0, column=2)
    buttons["b4"].grid(row=1, column=0)
    buttons["b5"].grid(row=1, column=1)
    buttons["b6"].grid(row=1, column=2)
    buttons["b7"].grid(row=2, column=0)
    buttons["b8"].grid(row=2, column=1)
    buttons["b9"].grid(row=2, column=2)

def reset():
    global AiSet, P1_Score, P2_Score, GameMode
    Start()
    AiSet = False
    P1_Score = 0
    P2_Score = 0
    GameMode = 0
    p1_label.config(text="X: " + str(P1_Score))
    p2_label.config(text="O: " + str(P2_Score))
    ai_on_var.set(False)
    ai_mode_var.set("")

def check_winner():
    global P1_Score, P2_Score, winner
    # Use "" (empty string) for unclicked buttons instead of " "
    winning_combinations = [
        (buttons["b1"], buttons["b2"], buttons["b3"]),
        (buttons["b4"], buttons["b5"], buttons["b6"]),
        (buttons["b7"], buttons["b8"], buttons["b9"]),
        (buttons["b1"], buttons["b4"], buttons["b7"]),
        (buttons["b2"], buttons["b5"], buttons["b8"]),
        (buttons["b3"], buttons["b6"], buttons["b9"]),
        (buttons["b1"], buttons["b5"], buttons["b9"]),
        (buttons["b3"], buttons["b5"], buttons["b7"])
    ]
    winner = False
    for combo in winning_combinations:
        # Check that the text is not empty
        if combo[0]['text'] == combo[1]['text'] == combo[2]['text'] != "":
            for btn in combo:
                btn.config(bg="red")
            winnerTxt = combo[0]['text']
            if winnerTxt == "X":
                global P1_Score
                P1_Score += 1
                p1_label.config(text="X: " + str(P1_Score))
            else:
                global P2_Score
                P2_Score += 1
                p2_label.config(text="O: " + str(P2_Score))
            winner = True
            messagebox.showinfo("Game Over", f"{winnerTxt} wins the game")
            Start()
            return  # Exit after a win

def b_click(b, btn_name):
    global clicked, count, Available_Positions, winner, minimax
    if b["text"] == "":
        # Human move (always "X")
        if clicked:
            b["text"] = "X"
            clicked = False  # Now it will be AI's turn ("O")
            count += 1
            if b in Available_Positions:
                Available_Positions.remove(b)
            minimax.fillPos(btn_name, b["text"])
            check_winner()
        # AI move (plays as "O")
        else:
            b["text"] = "O"
            clicked = True  # Switch back to human's turn
            count += 1
            if b in Available_Positions:
                Available_Positions.remove(b)
            minimax.fillPos(btn_name, b["text"])
            check_winner()
    else:
        messagebox.showerror("ERROR", "That space is already taken!")

    if count == 9 and not winner:
        messagebox.showwarning("Game Over", "No one wins :(")
        Start()

def SetAi():
    global AiSet
    AiSet = True
    gameloop()

def SetModeEasy():
    global GameMode
    GameMode = 1
    gameloop()

def SetModeImposible():
    global GameMode
    GameMode = 2
    gameloop()

def gameloop():
    global clicked, Available_Positions, winner, minimax
    all_buttons = list(buttons.values())
    if AiSet and not clicked and not winner:
        for btn in all_buttons:
            btn.config(state=DISABLED)
        if GameMode == 1:
            if Available_Positions:
                r = random.choice(Available_Positions)
                for name, btn_obj in buttons.items():
                    if btn_obj == r:
                        ai_btn_name = name
                        break
                b_click(r, ai_btn_name)
        elif GameMode == 2:
            move = minimax.find_best_move()
            if move[0] != -1:
                ai_btn = buttons[move[1]]
                b_click(ai_btn, move[1])
        for btn in all_buttons:
            btn.config(state=NORMAL)
    root.after(300, gameloop)

my_menu = Menu(root)
root.config(menu=my_menu)
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

AiMenu = Menu(my_menu, tearoff=False)
AiSettings = Menu(AiMenu, tearoff=False)
ai_on_var = BooleanVar(value=False)
ai_mode_var = StringVar(value="")

my_menu.add_cascade(label="Ai Settings", menu=AiMenu)
AiMenu.add_checkbutton(label="Turn On Ai", command=SetAi, variable=ai_on_var)
AiMenu.add_cascade(label="Ai Mode", menu=AiSettings)
AiSettings.add_radiobutton(label="Easy", command=SetModeEasy, variable=ai_mode_var, value="Easy")
AiSettings.add_radiobutton(label="Impossible", command=SetModeImposible, variable=ai_mode_var, value="Impossible")

Start()
gameloop()
root.mainloop()
