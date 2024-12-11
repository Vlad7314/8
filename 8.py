import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = '5f3c2746c90c6047f3b76f0b171b7f52'

def get_weather():
    """
    Получает текущую погоду в Ульяновске и отображает ее в сообщении.
    """
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q=Ulyanovsk,RU&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city = data['name']
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            messagebox.showinfo("Погода в Ульяновске", f"Город: {city}\nТемпература: {temperature}°C Описание: {weather_description}")
        else:
            raise Exception("Не удалось получить данные о погоде.")
    except Exception as e:
        messagebox.showwarning("Ошибка", str(e))

def perform_operation(operation):
    """
    Выполняет операцию над двумя числами и отображает результат.
    
    Параметры:
    operation (str): Операция, которую нужно выполнить ('Addition', 'Subtraction', 'Multiplication', 'Division').
    """
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == 'Addition':
            result = num1 + num2
        elif operation == 'Subtraction':
            result = num1 - num2
        elif operation == 'Multiplication':
            result = num1 * num2
        elif operation == 'Division':
            if num2 != 0:
                result = num1 / num2
            else:
                raise ZeroDivisionError

        messagebox.showinfo("Результат", f"Результат: {result}")
    except ValueError:
        messagebox.showwarning("Ошибка", "Введите корректные числа")
    except ZeroDivisionError:
        messagebox.showwarning("Ошибка", "Делить на 0 нельзя")

def clear_entries():
    """
    Очищает поля ввода, удаляя введенные пользователем данные.
    """
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)

# Создаем главное окно
window = tk.Tk()
window.title("Калькулятор Погоды")
window.configure(bg="#eaeaea")

# Установка размеров окна
window.geometry("500x500")  # Ширина x Высота
window.resizable(False, False)  # Запретить изменение размера

# Надписи и поля ввода
label_num1 = tk.Label(window, text="Введите первое число:", bg="#eaeaea", font=("Arial", 14))
label_num1.pack(pady=(20, 10))

entry_num1 = tk.Entry(window, font=("Arial", 14), borderwidth=3, relief="flat")
entry_num1.pack(pady=5)

label_num2 = tk.Label(window, text="Введите второе число:", bg="#eaeaea", font=("Arial", 14))
label_num2.pack(pady=(20, 10))

entry_num2 = tk.Entry(window, font=("Arial", 14), borderwidth=3, relief="flat")
entry_num2.pack(pady=5)

# Кнопки операций с иконками
button_weather = tk.Button(window, text="🌤 Получить погоду", command=get_weather, bg="#4CAF50", fg="white", font=("Arial", 12), width=25, height=2)
button_weather.pack(pady=15)

button_add = tk.Button(window, text="➕ Сложение", command=lambda: perform_operation("Addition"), bg="#2196F3", fg="white", font=("Arial", 12), width=20, height=2)
button_add.pack(pady=5)

button_subtract = tk.Button(window, text="➖ Вычитание", command=lambda: perform_operation("Subtraction"), bg="#F44336", fg="white", font=("Arial", 12), width=20, height=2)
button_subtract.pack(pady=5)

button_multiply = tk.Button(window, text="✖ Умножение", command=lambda: perform_operation("Multiplication"), bg="#FFA500", fg="white", font=("Arial", 12), width=20, height=2)
button_multiply.pack(pady=5)

button_divide = tk.Button(window, text="➗ Деление", command=lambda: perform_operation("Division"), bg="#FF9800", fg="white", font=("Arial", 12), width=20, height=2)
button_divide.pack(pady=5)

# Кнопка очистки
button_clear = tk.Button(window, text="🗑 Очистить", command=clear_entries, bg="#9E9E9E", fg="white", font=("Arial", 12), width=20, height=2)
button_clear.pack(pady=15)

window.mainloop()
