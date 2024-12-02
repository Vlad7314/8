import tkinter as tk
from tkinter import messagebox
import math

def perform_operation(operation):
    """
    Выполняет операцию над двумя числами и отображает результат.

    Параметры:
    operation (str): Операция, которую нужно выполнить ('Addition', 'Subtraction', 'Multiplication', 'Division', 'SquareRoot', 'Power').
    """
    try:
        if operation in ['Addition', 'Subtraction', 'Multiplication', 'Division']:
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

        elif operation == 'SquareRoot':
            num1 = float(entry_num1.get())
            result = math.sqrt(num1)
            messagebox.showinfo("Результат", f"Квадратный корень: {result}")

        elif operation == 'Power':
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            result = math.pow(num1, num2)
            messagebox.showinfo("Результат", f"{num1} в степени {num2} = {result}")
    
    except ValueError:
        messagebox.showwarning("Ошибка", "Введите нормально числа")
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
window.title("Калькулятор")
window.configure(bg="#f3f4f6")

# Установка размеров окна
window.geometry("400x500")  # Ширина x Высота
window.resizable(True, True)  # Сделать окно изменяемым

# Надписи и поля ввода
label_num1 = tk.Label(window, text="Введите первое число:", bg="#f3f4f6", font=("Helvetica", 12))
label_num1.pack(pady=(20, 10))

entry_num1 = tk.Entry(window, font=("Helvetica", 12), borderwidth=2, relief="groove")
entry_num1.pack(pady=5)

label_num2 = tk.Label(window, text="Введите второе число:", bg="#f3f4f6", font=("Helvetica", 12))
label_num2.pack(pady=(20, 10))

entry_num2 = tk.Entry(window, font=("Helvetica", 12), borderwidth=2, relief="groove")
entry_num2.pack(pady=5)

# Кнопки операций с иконками
button_add = tk.Button(window, text=" Сложение", command=lambda: perform_operation("Addition"), bg="#4CAF50", fg="white", font=("Helvetica", 12), width=20)
button_add.pack(pady=5)

button_subtract = tk.Button(window, text=" Вычитание", command=lambda: perform_operation("Subtraction"), bg="#F44336", fg="white", font=("Helvetica", 12), width=20)
button_subtract.pack(pady=5)

button_multiply = tk.Button(window, text=" Умножение", command=lambda: perform_operation("Multiplication"), bg="#2196F3", fg="white", font=("Helvetica", 12), width=20)
button_multiply.pack(pady=5)

button_divide = tk.Button(window, text=" Деление", command=lambda: perform_operation("Division"), bg="#FF9800", fg="white", font=("Helvetica", 12), width=20)
button_divide.pack(pady=5)

button_sqrt = tk.Button(window, text=" Квадратный корень", command=lambda: perform_operation("SquareRoot"), bg="#9C27B0", fg="white", font=("Helvetica", 12), width=20)
button_sqrt.pack(pady=5)

button_power = tk.Button(window, text=" Возведение в степень", command=lambda: perform_operation("Power"), bg="#3F51B5", fg="white", font=("Helvetica", 12), width=20)
button_power.pack(pady=5)

button_clear = tk.Button(window, text=" Очистить", command=clear_entries, bg="#f44336", fg="white", font=("Helvetica", 12), width=20)
button_clear.pack(pady=5)

window.mainloop()
