import matplotlib.pyplot as plt
import math
import pandas as pd
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Программа для вывода информации из файла в Excel")
    def DiagramData():
        file = pd.read_excel('число въездных поездок в Россию.xlsx')
        df = pd.DataFrame(file)
        name = df['Страны']
        tourists = df.iloc[:, 2:11]
        # Вычисляем количество диаграмм, округляя до ближайшего большего целого
        num_diagrams = math.ceil(tourists.shape[1] / 3)
        # Создаем общую фигуру
        fig, axs = plt.subplots(nrows=num_diagrams, ncols=3, figsize=(16, 6*num_diagrams))
        axs = axs.flatten()  # Преобразуем массив осей в одномерный массив
        # Создаем графики
        for i in range(tourists.shape[1]):
            ax = axs[i]
            ax.barh(name, tourists.iloc[:, i], align='center', color=f'C{i}')
            ax.grid(True, color='grey', linestyle='-.', linewidth=0.5)
            ax.invert_yaxis()
            for j, value in enumerate(tourists.iloc[:, i]):
                ax.text(value, j, str(value), fontsize=6, va='center')
            ax.tick_params(axis='both', labelsize=6)
            ax.legend([tourists.columns[i]], fontsize=8, loc='upper right')

        # Убираем лишние оси
        for i in range(tourists.shape[1], num_diagrams*3):
            axs[i].remove()
        plt.tight_layout()
        plt.get_current_fig_manager().window.state('zoomed')
        plt.show()

    def select_file():
        data = pd.read_excel('число въездных поездок в Россию.xlsx')
        info_window = tk.Toplevel(root)
        info_window.title("Информация из файла")
        info_window.geometry("1000x500")
        info_table = tk.Text(info_window, height=30, width=100)
        info_table.insert(tk.END, data.to_string(index=False))
        info_table.pack()

    def max_tourists():
        file = pd.read_excel('число въездных поездок в Россию.xlsx')
        df = pd.DataFrame(file)
        name = df.iloc[1:-1, 0]  # срез для выделения имен стран
        tourists = df.iloc[1:-1, 1:-1]
        max_tourists = 0
        max_tourists_country = ''
        max_tourists_year = ''
        for i in range(tourists.shape[0]):
            for j in range(tourists.shape[1]):
                if pd.to_numeric(tourists.iloc[i, j], errors='coerce') >= max_tourists:
                    max_tourists = pd.to_numeric(tourists.iloc[i, j], errors='coerce')
                    max_tourists_country = name.iloc[i]  # использование .iloc[i] для получения имени страны
                    max_tourists_year = str(tourists.columns[j])
        result_str = f'Больше всего туристов ({max_tourists}) приезжало из {max_tourists_country} в {max_tourists_year} году'
        result_window = tk.Toplevel(root)
        result_window.title("Результат")
        result_window.geometry("500x100")
        result_label = tk.Label(result_window, text=result_str, font=("Arial", 12))
        result_label.pack(pady=20)