import tkinter as tk

import numpy as np
import sounddevice as sd


def play_sound():
    frequency = 440
    duration = 1
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(signal, sample_rate)
    sd.wait()


def run_program():
    root = tk.Tk()
    root.title("Experimental VST")

    play_button = tk.Button(root, text="Play", command=play_sound)
    play_button.pack(pady=20)

    root.mainloop()
