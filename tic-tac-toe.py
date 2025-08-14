import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                b = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                              command=lambda i=i, j=j: self.make_move(i, j))
                b.grid(row=i, column=j)
                self.buttons[i][j] = b

    def make_move(self, i, j):
        if self.buttons[i][j]["text"] == "":
            self.buttons[i][j]["text"] = self.current_player
            if self.check_win():
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} победил!")
                self.reset_board()
                return
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.current_player = "X"

root = tk.Tk()
TicTacToe(root)
root.mainloop()
