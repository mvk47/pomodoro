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
timer_clock = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer_clock)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    tick_mark.config(text="")
    start_button.config(state="normal")
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    start_button["state"] = "disable"
    global REPS
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = WORK_MIN * 60
    break_sec = LONG_BREAK_MIN * 60
    if REPS % 4 == 0 and REPS != 0:
        count_down(break_sec)
        timer.config(text="Break")
    elif REPS % 2 == 1:
        timer.config(text="Break")
        count_down(short_sec)
    else:
        timer.config(text="Work")
        count_down(long_sec)
    REPS += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_clock
        timer_clock = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS/2)):
            mark += "✔"
        tick_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.minsize(width=300, height=300)
window.title("Pomodoro app")
window.config(padx=100, pady=100, bg=PINK)


canvas = Canvas(width=300, height=300, bg=PINK, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(153, 112, image=image)
timer_text = canvas.create_text(153, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# Timer label
timer = Label()

timer.config(text="Timer", font=(FONT_NAME, 40), bg=PINK, fg=YELLOW)
timer.grid(row=0, column=1)

# start button
start_button = Button()
start_button.config(text="Start", command=start_timer, font=(FONT_NAME, 10))
start_button.grid(row=2, column=0)

# reset button
reset_button = Button()
reset_button.config(text="Reset", command=reset_timer, font=(FONT_NAME, 10))
reset_button.grid(row=2, column=2)

# tick mark label
tick_mark = Label()
tick_mark.config(bg=PINK, fg=YELLOW)
tick_mark.grid(row=3, column=1)


window.mainloop()
