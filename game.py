from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe Game')
# root.iconbitmap
# set icon

# Reset the game
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

#check to see if someone won




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
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("ERROR", "Hey! thats not how you play")


    if count == 9 and winner == False:
        messagebox.showwarning("Game over","No one wins :(")
        reset()

#creat menue
my_menu = Menu(root)
root.config(menu=my_menu)

# create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()

root.mainloop()