from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = ""
# timer variable to enable stopping the timer
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_func():
    global checks
    global reps
    # stopping the timer (timer is the variable to which we put the delay)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_lable.config(text="Timer", fg=GREEN)
    check_marks.config(text="      ")
    checks = ""
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_func():
    global reps
    global title_lable
    reps += 1
    # configuring number of seconds to count down
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60

    if reps % 2 == 8:
        title_lable.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_lable.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_lable.config(text="Work ", fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global checks
    global timer
    # calculating minutes and seconds in count
    # math.floor() gets the integer part of the result (not rounding, just taking the integer part)
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")

    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:
            checks += "✔"
            check_marks.config(text=checks)
        start_func()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create a canvas with the size of the image. We can put on the canvas an image and text in layers. bg is for
# background colour, highlightthickness makes the seem between the image and the canvas to have the same colour
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# For the canvas we need the image to be loaded as a PhotoImage. We need to specify x,y
# coordinates (of the middle of the image) and image file
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)

# Text
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Labels
title_lable = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_lable.grid(column=1, row=0)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14))
check_marks.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", command=start_func, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_func, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
