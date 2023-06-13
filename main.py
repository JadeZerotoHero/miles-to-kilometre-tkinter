import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# functionality of the convert
def convert():
    try:
        mile_input = entry_int.get()
        km_output = mile_input * 1.61
        output_string.set(km_output)
    except Exception:
        output_string.set("Enter a value")

# window
window = ttk.Window(themename = 'darkly')
window.title('Miles to kilometres')
window.geometry('300x150') #height

# title (widget)
title_label = ttk.Label(master = window, text = 'Miles to kimometers', font = 'Calibri 24 bold') # label - text, master is the parent, font = font, font size
title_label.pack()

# input field - need 3 widget
input_frame = ttk.Frame(master = window) # need parent/master
entry_int = tk.IntVar() # create a separate variable that can store and update values
entry = ttk.Entry(master = input_frame, textvariable = entry_int) # need to get content of entry field
button = ttk.Button(master = input_frame, text = 'Convert', command = convert) # only want to pass a function but not call the function
entry.pack(side = 'left', padx = 10) # padding x put distance horizontally between each other
button.pack(side = 'left')
input_frame.pack(pady = 10) 
# pack defaults places widget below each other

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window,
    text = 'Output',
    font = 'Calibri 24',
    textvariable=output_string
    )
output_label.pack(pady = 5)

# run 
window.mainloop() # create a window