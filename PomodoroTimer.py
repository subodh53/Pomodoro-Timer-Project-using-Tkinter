
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
from tkinter import *
import math
window = Tk()
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
    check_label.config(text="",bg="black",fg="white")
    window_label.config(text="Timer",bg="black",fg="white",font=(FONT_NAME,35,"bold"),highlightthickness=0)
    global reps
    reps = 0
def start_timer():
    global reps
    reps+=1
    work_secs = WORK_MIN*60
    short_break_secs = SHORT_BREAK_MIN*60
    long_break_secs = LONG_BREAK_MIN*60
    if reps%8 == 0:
        count_down(long_break_secs)
        window_label.config(text="Long Break Break",bg="black",fg="white",font=(FONT_NAME,35,"bold"),highlightthickness=0)
    elif reps%2 == 0:
        count_down(short_break_secs)
        window_label.config(text="Short Break",bg="black",fg="white",font=(FONT_NAME,35,"bold"),highlightthickness=0)
    else:
        count_down(work_secs)
        window_label.config(text="Work",bg="black",fg="white",font=(FONT_NAME,35,"bold"),highlightthickness=0)
def count_down(count):
    tim_min = math.floor(count/60)
    tim_sec = count%60
    if tim_min<10:
        tim_min = f"0{tim_min}"
    if tim_sec<10:
        tim_sec =f"0{tim_sec}"
    canvas.itemconfig(timer_text,text=f"{tim_min}:{tim_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔️"
            check_label.config(text=marks,bg="black",fg="white")
window_label = Label(text="TIMER")
window_label.config(bg="black",fg="white",font=(FONT_NAME,35,"bold"),highlightthickness=0)
window_label.grid(column=1,row=0)
window.config(padx=100,pady=50,bg="black")
window.title("Pomodoro")
canvas = Canvas(width=200,height=224,bg="black",highlightthickness=0)
tom_image = PhotoImage(file="tomato.png")
canvas.create_image(100,111,image=tom_image)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
start_button = Button(text="Start Button",command=start_timer)
start_button.grid(column=0,row=2)
start_button.config(bg="black",fg="white",highlightthickness=0)
reset_button = Button(text="Reset Button",command=reset_timer)
reset_button.grid(column=2,row=2)
reset_button.config(bg="black",fg="white",highlightthickness=0)
check_label = Label(bg="black",fg="white")
check_label.grid(column=1,row=3)
check_label.config(bg="black",fg="white")
window.mainloop()
