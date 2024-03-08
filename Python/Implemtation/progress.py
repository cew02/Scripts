from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')

def update_progress_label():
    return f"Current Progress: {pb['value']}%"

def progress():
    if pb['value'] < 100:
        pb['value'] += 20
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The Progress Completed!')

def stop():
    pb.stop()
    value_label['text'] = update_progress_label()