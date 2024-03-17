import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import webbrowser
import threading
import time

song_urls = {
    "Egzod & Maestro Chives - Royalty": "https://www.youtube.com/watch?v=zO1yc8AVH-M&t=1840s",
    "Kendrick Lammar- Swimming pool": "https://www.youtube.com/watch?v=B5YNiCfWC3A&list=RDB5YNiCfWC3A&start_radio=1",
    "La Fouine - On s'en bat les": "https://www.youtube.com/watch?v=0QKnYud_FUc",
    "NF - The Search": "https://www.youtube.com/watch?v=H0BXMUdyIKA&list=RDC0FoDRS47To&index=3"
}

def set_alarm():
    try:
        hour_val = int(hour.get())
        minute_val = int(minute.get()) if minute.get() else 0
        if time_var.get() == "PM":
            hour_val += 12
        alarm_time = datetime.now().replace(hour=hour_val, minute=minute_val, second=0, microsecond=0)
        if datetime.now() > alarm_time:
            alarm_time += timedelta(days=1)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid hour and minute")
        return

    maintenant = datetime.now()
    difference = alarm_time - maintenant

    heures, reste = divmod(difference.seconds, 3600)
    minutes, secondes = divmod(reste, 60)
    time_left = "{:02}h{:02}".format(heures, minutes) 

    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time.strftime('%I:%M %p')}\nIn {time_left}")

    threading.Thread(target=wait_and_ring_alarm, args=(alarm_time,)).start()

def wait_and_ring_alarm(alarm_time):
    while True:
        current_time = datetime.now()
        if current_time >= alarm_time:
            ring_alarm()
            break
        time.sleep(1)

def ring_alarm():
    open_youtube_video()

def open_youtube_video():
    selected_song = song_var.get()
    url = song_urls.get(selected_song, "https://www.youtube.com/watch?v=eJO5HU_7_1w")
    webbrowser.open(url)

clock = tk.Tk()
clock.title("Alarm Clock")

tk.Label(clock, text="Enter time in 12-hour format:", fg="red", bg="black", font=("times new roman", 12, "bold")).grid(row=0, column=0, columnspan=4)
tk.Label(clock, text="Hour", fg="grey", font=("times new roman", 12)).grid(row=1, column=0)
tk.Label(clock, text="Minute", fg="grey", font=("times new roman", 12)).grid(row=1, column=1, padx=70)
tk.Label(clock, text="AM/PM", fg="grey", font=("times new roman", 12)).grid(row=1, column=2)

hour = tk.StringVar()
minute = tk.StringVar()
time_var = tk.StringVar(value="AM")
song_var = tk.StringVar(clock)
song_var.set("Default: Eminem - The Real Slim Shady")

hour_entry = tk.Entry(clock, textvariable=hour, bg="#d1d1d1", width=5)
hour_entry.grid(row=2, column=0)
minute_entry = tk.Entry(clock, textvariable=minute, bg="#d1d1d1", width=5)
minute_entry.grid(row=2, column=1)
time_entry = tk.OptionMenu(clock, time_var, "AM", "PM")
time_entry.grid(row=2, column=2)

song_menu = tk.OptionMenu(clock, song_var, *song_urls.keys())
song_menu.grid(row=5, columnspan=4)

tk.Button(clock, text="Set Alarm", fg="red", font=("times new roman", 12), width=10, command=set_alarm).grid(row=6, columnspan=4)

for i in range(7):
    clock.columnconfigure(i, weight=1)
    clock.rowconfigure(i, weight=1)

clock.mainloop()
