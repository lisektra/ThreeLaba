import tkinter as tk
import pandas as pd
from matplotlib import pyplot as plt

filename = 'population_data.xlsx'
sheetname = 'Население по субъектам'
data = pd.read_excel(filename, sheet_name=sheetname, header=0)

# загрузка данных из файла Excel и вывод в окно
def select_file():
    info_window = tk.Toplevel(root)
    info_window.title("Информация из файла")
    info_window.geometry("1300x500")
    info_table = tk.Text(info_window, height=30, width=200)
    info_table.insert(tk.END, data.to_string(index=False))
    info_table.pack()

# построение графиков для каждого субъекта
def DiagramData():
    for i, row in data.iterrows():
        plt.plot(row.index[1:], row[1:], label=row[0])
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xlabel('Год')
    plt.ylabel('Численность населения')
    plt.title('Динамика численности населения по субъектам РФ')
    plt.show()

# поиск субъекта с наибольшим снижением численности населения
def PopulationData():
    data['Разница'] = data['2022 г.'] - data['2008 г.']
    data_sorted = data.sort_values(by='Разница', ascending=True)
    max_difference_subject = data_sorted.iloc[0]['Субъекты РФ/Год']
    difference_2008_2022 = data_sorted.iloc[0]['Разница']
    result_window = tk.Toplevel(root)
    result_window.title("Результаты")
    result_window.geometry("500x100")
    result_label = tk.Label(result_window, text=f"Субъект РФ с наибольшим снижением численности населения: {max_difference_subject}\nРазница населения между 2008 и 2022 годами: {difference_2008_2022}")
    result_label.pack()

# Графический интерфейс
root = tk.Tk()
root.title("Программа для вывода информации из Excel")
file_button = tk.Button(root, text="Открыть таблицу", command=select_file)
exit_button = tk.Button(root, text='Закрыть', command=root.destroy)
diagram_button = tk.Button(root, text='Показать диаграмму', command=DiagramData)
result_button = tk.Button(root, text='Наибольшее снижение численности', command=PopulationData)
file_button.pack(padx=10, pady=10)
diagram_button.pack(padx=30, pady=10)
result_button.pack(padx=20, pady=10)
exit_button.pack(padx=20, pady=10)
root.mainloop()