import tkinter as tk
from tkinter import messagebox
import pandas as pd
from matplotlib import pyplot as plt

def select_file():
    data = pd.read_excel('crime.xlsx')
    info_window = tk.Toplevel(root)
    info_window.title("Информация из файла")
    info_window.geometry("1100x300")
    info_table = tk.Text(info_window, height=30, width=500)
    info_table.insert(tk.END, data.to_string(index=False))
    info_table.pack()

root = tk.Tk()
root.title("Программа для вывода информации из файла в Excel")
file_button = tk.Button(root, text="Открыть таблицу", command=select_file)
file_button.pack(padx=10, pady=10)
exit_button = tk.Button(root, text='Закрыть', command=root.destroy)
exit_button.pack(padx=20, pady=10)
root.mainloop()