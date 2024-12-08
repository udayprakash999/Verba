import tkinter as tk
import pyttsx3
from tkinter import font, ttk

engine = pyttsx3.init()

def speak():
    text = text_entry.get()
    if text:
        engine.say(text)
        engine.runAndWait()

def clear_text():
    text_entry.delete(0, tk.END)

def change_voice():
    voice_choice = voice_combo.get()
    voices = engine.getProperty('voices')
    if voice_choice == "Male":
        engine.setProperty('voice', voices[0].id)  # Male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Female voice

def set_volume(val):
    engine.setProperty('volume', float(val)/100)

def set_speed(val):
    engine.setProperty('rate', int(val))

root = tk.Tk()
root.title("Laptop Talk App")
root.geometry("500x400")
root.config(bg="#f5f5f5")

title_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Arial", size=12)
button_font = font.Font(family="Comic Sans MS", size=14, weight="bold")

def on_enter(e):
    e.widget['background'] = '#3b8c5d'  
    e.widget['foreground'] = '#fff'

def on_leave(e):
    e.widget['background'] = '#4CAF50' 
    e.widget['foreground'] = '#fff'

frame = tk.Frame(root, bg='#f5f5f5', width=500, height=400)
frame.pack_propagate(False)

label = tk.Label(frame, text="Enter text for the laptop to speak:", font=label_font, bg='#f5f5f5', fg='black')
label.pack(pady=10)

text_entry = tk.Entry(frame, font=("Arial", 14), width=30, bd=5, relief="solid", justify="center")
text_entry.pack(pady=10)

speak_button = tk.Button(frame, text="Speak", font=button_font, bg='#4CAF50', fg='white', relief="solid", width=15, height=2, command=speak)
speak_button.pack(pady=10)

clear_button = tk.Button(frame, text="Clear Text", font=button_font, bg='#ff704d', fg='white', relief="solid", width=15, height=2, command=clear_text)
clear_button.pack(pady=10)

voice_label = tk.Label(frame, text="Choose Voice:", font=label_font, bg='#f5f5f5', fg='black')
voice_label.pack(pady=5)

voice_combo = ttk.Combobox(frame, values=["Male", "Female"], font=("Arial", 12), width=15)
voice_combo.set("Male")  
voice_combo.pack(pady=5)

voice_button = tk.Button(frame, text="Change Voice", font=button_font, bg='#4CAF50', fg='white', relief="solid", width=15, height=2, command=change_voice)
voice_button.pack(pady=10)

volume_label = tk.Label(frame, text="Volume Control:", font=label_font, bg='#f5f5f5', fg='black')
volume_label.pack(pady=5)

volume_slider = tk.Scale(frame, from_=0, to=100, orient="horizontal", command=set_volume, font=("Arial", 12))
volume_slider.set(100) 
volume_slider.pack(pady=10)

speed_label = tk.Label(frame, text="Speed Control:", font=label_font, bg='#f5f5f5', fg='black')
speed_label.pack(pady=5)

speed_slider = tk.Scale(frame, from_=50, to=200, orient="horizontal", command=set_speed, font=("Arial", 12))
speed_slider.set(150) 
speed_slider.pack(pady=10)

exit_button = tk.Button(frame, text="Exit", font=button_font, bg='#ff6666', fg='white', relief="solid", width=15, height=2, command=root.quit)
exit_button.pack(pady=20)

speak_button.bind("<Enter>", on_enter)
speak_button.bind("<Leave>", on_leave)

clear_button.bind("<Enter>", on_enter)
clear_button.bind("<Leave>", on_leave)

voice_button.bind("<Enter>", on_enter)
voice_button.bind("<Leave>", on_leave)

exit_button.bind("<Enter>", on_enter)
exit_button.bind("<Leave>", on_leave)

frame.pack()

root.mainloop()
