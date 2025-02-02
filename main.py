import tkinter as tk
import pyperclip
import keyboard
import sys
import os

flag = False
input_text = ""
selected_value = 0

def read_text():
    global flag, input_text
    input_text = text.get("1.0", tk.END).strip()
    pyperclip.copy(input_text)

    flag = True
    background_task()

def stop_text():
    global flag
    flag = False

def background_task():
    if flag:
        keyboard.press_and_release('ctrl+v')
        keyboard.press_and_release('enter')
        # Schedule the next call after 1000 milliseconds (1 second)
        window.after(selected_value, background_task)

window = tk.Tk()

text = tk.Text(window, width=48, height=5)
text.pack()

def update_slider_from_entry():
    global selected_value
    try:
        value = int(entry.get())
        if slider_from <= value <= slider_to:
            slider.set(value)
            selected_value = value
    except ValueError:
        pass

def update_entry_from_slider(val):
    global selected_value
    entry.delete(0, tk.END)
    entry.insert(0, val)
    selected_value = val

def toggle_buttons():
    global toggle_state
    if toggle_state:
        button.invoke()
    else:
        button2.invoke()
    toggle_state = not toggle_state

slider_from = 1  # Ranges for slider, DO NOT USE APP ON 0 DELAY!!
slider_to = 1000

slider = tk.Scale(window, from_=slider_from, to=slider_to, orient="horizontal", command=update_entry_from_slider)
slider.pack()

entry = tk.Entry(window)
entry.pack()

entry.bind("<Return>", lambda event: update_slider_from_entry())

slider.set(slider_from)
entry.insert(0, slider_from)

empty_space_02 = tk.Label(window, text="^ DELAY ^", width=20, height=2)
empty_space_02.pack()

empty_space_03 = tk.Label(window, text="", width=20, height=2)
empty_space_03.pack()

button = tk.Button(window, text="START (F6)", command=read_text, width=30, height=3)
button.pack()

empty_space_04 = tk.Label(window, text="", width=20, height=0)
empty_space_04.pack()

button2 = tk.Button(window, text="STOP (F6)", command=stop_text, width=30, height=3)
button2.pack()

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

icon_path = os.path.join(base_path, "WORDSPAM.ico")

window.iconbitmap(icon_path)
window.title("AL Word Spammer")
window.geometry('400x370')
window.minsize(300,370)
window.maxsize(400,370)

toggle_state = True

keyboard.add_hotkey('F6', lambda: toggle_buttons())

window.mainloop()

# hi :D A

# Copyright (c) 2025 aperson5647
# Released under the MIT License
# https://opensource.org/licenses/MIT
