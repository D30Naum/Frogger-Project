# COMP 123
# Devi Naum
# Blake Kell
""" This file contains the start page for the game where the player can choose the difficulty of the game. """
# Import the necessary modules, especially tkinter.
from tkinter import *
from Game_level1 import *

class FroggerApp:
    def __init__(self):
        """This function intends to create the first window of the game where the player can start the game by pressing
        the Play button, which activates the other Python file. Further, this creates the Tutorial button which shows
        the player how this game is supposed to be played."""
        root = Tk()
        bg = PhotoImage(file="background-easy2.png")
        root.geometry("600x650")

        label1 = Label(root, image=bg)
        label1.place(x=0, y=-70)

        label2 = Label(root, text="Frogger", font = "DroidSans 40", justify = CENTER, bg = "#1F7DB9")
        label2.pack(pady=85)

        button1 = Button(text="Play the Game", command = gameStart, bg = "#000000", font= "DroidSans 17")
        button1.pack(pady=20)

        button1 = Button(text="Easy", command=gameStart, bg="#000000", font="DroidSans 17")
        button1.pack(pady=20)

        button1 = Button(text="Medium", command=gameStart1, bg="#000000", font="DroidSans 17")
        button1.pack(pady=20)

        button1 = Button(text="Hard", command=gameStart2, bg="#000000", font="DroidSans 17")
        button1.pack(pady=20)


        root.mainloop()
        exit()


myApp = FroggerApp()
myApp.__init__()

""" For this user interface tkinter file, I needed to position the images and the buttons in a specific position. 
 To that end, I used trial and error to make sure the positions were correct and the button commands were working 
 properly."""