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
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_label.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 2 == 1:
        count_down(work_sec)
        label.config(text="Work", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
    if REPS == 8:
        count_down(long_break_sec)
        label.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=RED)
    if REPS % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(REPS / 2)):
            marks += "✓"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Title label
label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_photo)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

#start button
my_button = Button(text="Start", command=start_timer)
my_button.grid(column=0, row=3)

#reset button
my_button = Button(text="Reset", command=reset_timer)
my_button.grid(column=2, row=3)

#Check label
check_label = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=4)

window.mainloop()
