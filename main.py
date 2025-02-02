import tkinter as tk
import pyperclip
import keyboard

flag = False
input_text = ""

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
        window.after(1000, background_task)

window = tk.Tk()

text = tk.Text(window, width=50, height=10)
text.pack()

button = tk.Button(window, text="START", command=read_text)
button.pack()

button = tk.Button(window, text="STOP", command=stop_text)
button.pack()

window.title("AL Word Spammer")
window.iconbitmap("WORDSPAM.ico")
window.geometry('400x500')
window.minsize(200,300)

window.mainloop()
