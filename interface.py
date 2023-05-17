import tkinter as tk
import os

def open_program():
    os.system('python crime.py')
def open_program1():
    os.system('python population.py')
def open_program1():
    os.system('python tourists.py')

root = tk.Tk()
open_button = tk.Button(root, text='Открыть вариант Литвиновой', command=open_program)
open_button.pack(padx=20, pady=10)
open_button1 = tk.Button(root, text='Открыть вариант Николаевой', command=open_program)
open_button1.pack(padx=20, pady=10)
open_button2 = tk.Button(root, text='Открыть вариант Костина', command=open_program)
open_button2.pack(padx=20, pady=10)
root.mainloop()
