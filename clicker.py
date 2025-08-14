import tkinter as tk
import os

SAVE_FILE = os.path.join(os.path.dirname(__file__), "clicker_score.txt")

def load_score():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                return int(f.read().strip())
        except:
            return 0
    return 0

def save_score(score):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        f.write(str(score))

def click():
    global score
    score += 1
    label.config(text=f"Очки: {score}")
    save_score(score)

score = load_score()

root = tk.Tk()
root.title("Кликер")
root.geometry("300x200")

label = tk.Label(root, text=f"Очки: {score}", font=("Arial", 20))
label.pack(pady=20)

btn = tk.Button(root, text="Клик!", font=("Arial", 18), command=click)
btn.pack(pady=20)

root.protocol("WM_DELETE_WINDOW", lambda: (save_score(score), root.destroy()))
root.mainloop()
