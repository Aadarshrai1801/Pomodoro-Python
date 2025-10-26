# Pomodoro Technique App using Python

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# CountDown Mechanism




# UI Setup

    # Window

window = Tk()
window.title("Pomodoro")
window.minsize(400, 290)
window.config(padx = 100, pady = 50, bg = YELLOW)

    # Label

timer = Label(text = "Timer", font = (FONT_NAME, 35, "bold"), bg = YELLOW, fg = GREEN)
timer.grid(column = 1, row = 0)

check_mark = Label(text = "🗸", font = (FONT_NAME, 20, "bold"), bg = YELLOW, fg = GREEN)
check_mark.grid(column = 1, row = 3, padx = 5, pady = 5)

    # Canvas Img

canvas = Canvas(width=200, height=224, bg = YELLOW)
img = PhotoImage(file = "28thDay/Tomato.png")
canvas.create_image(102, 112, image = img)
canvas.create_text(102, 130, text = "00:00", fill = "white", font = (FONT_NAME, 30, "bold"))
canvas.grid(column = 1, row = 1)

    # Buttons 

button1 = Button(text  = "Start")
button1.grid(column = 0, row = 2, padx = 5, pady = 5)

button2 = Button(text  = "Restart")
button2.grid(column = 2, row = 2, padx = 5, pady = 5)

window.mainloop()