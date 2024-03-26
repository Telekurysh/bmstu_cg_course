import matplotlib.pyplot as plt

# Замените 'ваш_файл.txt' на имя вашего файла с данными
file_path = 'time2.txt'

# Чтение данных из файла
with open(file_path, 'r') as file:
    lines = file.readlines()

# Разделение строк на значения x и y (предполагаем, что значения разделены пробелом)
x_values = [float(line.split()[0]) for line in lines]
y_values = [float(line.split()[1]) for line in lines]

# Построение графика
plt.plot(x_values, y_values, label='Зависимость времени генерации от количества значимых точек')

plt.grid(True)

# Настройки графика (название, подписи осей и т.д.)
plt.title('Зависимость времени генерации от количества значимых точек')
plt.xlabel('Количество значимых точек')
plt.ylabel('Время работы, тики')
plt.legend()  # Добавление легенды

# Отображение графика
plt.show()