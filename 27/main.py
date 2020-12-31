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

reps = 8

timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    timer_title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_text.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_secs = WORK_MIN * 60
    short_secs = SHORT_BREAK_MIN * 60
    long_secs = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 8 == 0:
        count_down(long_secs)
        timer_title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_secs)
        timer_title.config(text="Break", fg=PINK)
    else:
        count_down(work_secs)
        timer_title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    global timer

    minutes = count // 60
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        checkmarks = ""

        for _ in range(reps//2):
            checkmarks += "✓"
        
        checkmark_text.config(text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row = 1)

timer_title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_title.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME,12), bg=GREEN, fg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME,12), bg=GREEN, fg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_text = Label(font=(FONT_NAME,18, "bold"), fg=GREEN, bg=YELLOW)
checkmark_text.grid(column=1, row=3)

window.mainloop()