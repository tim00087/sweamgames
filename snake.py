import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
SEG_SIZE = 20
SPEED = 100  # меньше = быстрее

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.segments = []
        self.direction = "Right"
        self.create_snake()
        self.running = True
        self.bind_keys()

    def create_snake(self):
        for i in range(3):
            x = SEG_SIZE * (3 - i)
            y = SEG_SIZE
            self.segments.append(self.canvas.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="green"))

    def move(self):
        if not self.running:
            return
        x1, y1, x2, y2 = self.canvas.coords(self.segments[0])
        if self.direction == "Up":
            y1 -= SEG_SIZE
        elif self.direction == "Down":
            y1 += SEG_SIZE
        elif self.direction == "Left":
            x1 -= SEG_SIZE
        elif self.direction == "Right":
            x1 += SEG_SIZE

        # Телепорт при выходе за границы
        if x1 < 0:
            x1 = WIDTH - SEG_SIZE
        elif x1 >= WIDTH:
            x1 = 0
        if y1 < 0:
            y1 = HEIGHT - SEG_SIZE
        elif y1 >= HEIGHT:
            y1 = 0

        self.canvas.move(self.segments[-1], x1 - self.canvas.coords(self.segments[-1])[0], y1 - self.canvas.coords(self.segments[-1])[1])
        self.segments = [self.segments[-1]] + self.segments[:-1]

        if (x1, y1, x1+SEG_SIZE, y1+SEG_SIZE) == tuple(self.canvas.coords(food)):
            self.add_segment()
            place_food()

        self.canvas.after(SPEED, self.move)

    def add_segment(self):
        x1, y1, x2, y2 = self.canvas.coords(self.segments[-1])
        seg = self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
        self.segments.append(seg)

    def bind_keys(self):
        keys = {
            "w": "Up", "W": "Up", "ц": "Up", "Ц": "Up", "Up": "Up",
            "s": "Down", "S": "Down", "ы": "Down", "Ы": "Down", "Down": "Down",
            "a": "Left", "A": "Left", "ф": "Left", "Ф": "Left", "Left": "Left",
            "d": "Right", "D": "Right", "в": "Right", "В": "Right", "Right": "Right"
        }
        for k, d in keys.items():
            root.bind(k, lambda e, dir=d: self.change_direction(dir))
        root.bind("r", lambda e: restart_game())
        root.bind("R", lambda e: restart_game())
        root.bind("к", lambda e: restart_game())
        root.bind("К", lambda e: restart_game())

    def change_direction(self, new_dir):
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_dir != opposites.get(self.direction):
            self.direction = new_dir

def place_food():
    global food
    canvas.delete(food)
    x = random.randrange(0, WIDTH, SEG_SIZE)
    y = random.randrange(0, HEIGHT, SEG_SIZE)
    food = canvas.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="red")

def restart_game():
    global snake
    canvas.delete("all")
    snake = Snake(canvas)
    place_food()
    snake.move()

root = tk.Tk()
root.title("Змейка")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

food = None
snake = Snake(canvas)
place_food()
snake.move()

root.mainloop()
