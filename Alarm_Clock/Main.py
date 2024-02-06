import tkinter as tk
from tkinter import messagebox
import datetime
import webbrowser
import threading
import time


def set_alarm():
    try:
        hour_val = int(hour.get())
        minute_val = int(minute.get())
        if time_var.get() == "PM":
            hour_val += 12
        alarm_time = datetime.time(hour_val, minute_val)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid hour and minute")
        return

    threading.Thread(target=wait_and_ring_alarm, args=(alarm_time,)).start()
    messagebox.askquestion("Alarm Set", f"Alarm set for {alarm_time.strftime('%I:%M %p')}")


def wait_and_ring_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().time()
        if current_time >= alarm_time:
            ring_alarm()
            break
        time.sleep(1)


def ring_alarm():
    open_youtube_video()


def open_youtube_video():
    user_url = url_entry.get().strip()
    default_url = "https://www.youtube.com/watch?v=eJO5HU_7_1w"
    if user_url:
        url = user_url
    else:
        url = default_url
    webbrowser.open(url)

clock = tk.Tk()
clock.title("Alarm Clock")

tk.Label(clock, text="Enter time in 12-hour format:", fg="red", bg="black", font=("times new roman", 12, "bold")).grid(row=0, column=0, columnspan=4)
tk.Label(clock, text="Hour", fg="white", font=("times new roman", 12)).grid(row=1, column=0)
tk.Label(clock, text="Minute", fg="white", font=("times new roman", 12)).grid(row=1, column=1, padx=70)
tk.Label(clock, text="AM/PM", fg="white", font=("times new roman", 12)).grid( row=1, column=2)

hour = tk.StringVar()
minute = tk.StringVar()
time_var = tk.StringVar(value="AM")
hour_entry = tk.Entry(clock, textvariable=hour, bg="#d1d1d1", width=5)
hour_entry.grid(row=2, column=0)
minute_entry = tk.Entry(clock, textvariable=minute, bg="#d1d1d1", width=5)
minute_entry.grid(row=2, column=1)
time_entry = tk.OptionMenu(clock, time_var, "AM", "PM")
time_entry.grid(row=2, column=2)
tk.Label(clock, text="Insert your song's URL", font=("times new roman", 12)).grid(row=3, columnspan=3)
url_entry = tk.Entry(clock, bg="#d1d1d1", width=30)
url_entry.grid( row=4, column=0,  columnspan=3)
tk.Button(clock, text="Set Alarm", fg="red", font=("times new roman", 12), width=10, command=set_alarm).grid(row=5, columnspan=4)

for i in range(5):
    clock.columnconfigure(i, weight=1)
    clock.rowconfigure(i, weight=1)
clock.mainloop()
