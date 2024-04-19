from tkinter import *
from math import floor

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW, highlightthickness=0)
stop = False
timer = None


def reset_time():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(start_timer, text="00:00")
    timer_text.config(text="Timer", font=(FONT_NAME, 80, "bold"), bg=YELLOW, fg=GREEN)
    checkmark.config(text="")


def start_count():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 2 != 0:
        timer_text.config(text="Work", bg=YELLOW, fg=GREEN)
        count_down(work_sec)
    elif reps % 2 == 0 and reps % 8 != 0:
        timer_text.config(text="Short Break", bg=YELLOW, fg=PINK)
        count_down(short_break_sec)
    else:
        timer_text.config(text="Long Break", bg=YELLOW, fg=RED)
        count_down(long_break_sec)


def count_down(count):
    global timer
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(start_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ""
        for _ in range(floor(reps/2)):
            mark += "✔"
        checkmark.config(text=mark)
        start_count()


canvas = Canvas(width=512, height=512, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(256, 256, image=tomato_img)
start_timer = canvas.create_text(256, 300, text="00:00", fill="white", font=(FONT_NAME, 80, "bold"))
canvas.grid(row=1, column=1)

start = Button(text="Start", command=start_count)
start.grid(row=2, column=0)

reset = Button(text="Reset", command=reset_time)
reset.grid(row=2, column=2)

timer_text = Label(text="Timer", font=(FONT_NAME, 80, "bold"), bg=YELLOW, fg=GREEN)
timer_text.grid(row=0, column=1)

checkmark = Label(font=(FONT_NAME, 30), bg=YELLOW, fg=GREEN)
checkmark.grid(row=2, column=1)

window.mainloop()
