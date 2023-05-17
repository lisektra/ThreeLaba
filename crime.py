import tkinter as tk
from tkinter import messagebox
import pandas as pd
from matplotlib import pyplot as plt

def DiagramData():
    file = pd.read_excel('crime.xlsx')
    df = pd.DataFrame(file)
    name = df['Статья УК РФ']
    crime = df.iloc[:, 1:16]
    dates = pd.date_range(start='2008-01-01', end='2023-01-01', freq='Y').strftime('%Y').tolist()
    crime.rename(columns=dict(zip(crime.columns, dates)), inplace=True)
    data = pd.DataFrame({'Преступление': name})
    for i in range(crime.shape[1]):
        data[f'{dates[i]}'] = crime.iloc[:, i]
    data.set_index('Преступление', inplace=True)
    ax = data.plot(kind='barh', figsize=(15, 6), color=[f'C{i}' for i in range(crime.shape[1])])
    ax.set_title('Данные о преступности в России за последние 15 лет')
    ax.set_xlabel('Количество преступлений')
    ax.set_ylabel('Преступление')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    ax.grid(True, color='grey', linestyle='-.', linewidth=0.5)
    ax.invert_yaxis()
    for i, value in enumerate(data.values.flatten()):
        plt.text(value, i, str(value), fontsize=8, va='center')
    plt.show()

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
diagram_button = tk.Button(root, text='Показать диаграмму', command=DiagramData)
diagram_button.pack(padx=30, pady=10)
exit_button = tk.Button(root, text='Закрыть', command=root.destroy)
exit_button.pack(padx=20, pady=10)
root.mainloop()