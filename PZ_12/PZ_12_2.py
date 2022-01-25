from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('pz_3_1')
root.geometry('530x300')
root.resizable(False, False)

# Функция-обработчик события "закрытие главного окна"
def close():
    root.destroy()
    root.quit()

# Условие задачи
us_label = Label(text='Программа проверяет истинность высказывания', font='Sans-serif 15')
us_label.place(x=20, y=20)
us1_label = Label(text='«Каждое из чисел A, B, C положительное».', font='Sans-serif 10')
us1_label.place(x=20, y=50)

# Первое поле ввода
ft_label = Label(text='Введите первое целое число', font='Sans-serif 9')
ft_label.place(x=20, y=85)
ft_entry = Entry(width=10)
ft_entry.place(x=22, y=105)

# Второе поле ввода
sd_label = Label(text='Введите второе целое число', font='Sans-serif 9')
sd_label.place(x=225, y=85)
sd_entry = Entry(width=10)
sd_entry.place(x=227, y=105)

# Третье поле ввода
td_label = Label(text='Введите третье целое число', font='Sans-serif 9')
td_label.place(x=20, y=135)
td_entry = Entry(width=10)
td_entry.place(x=22, y=155)

# Функция-обработчик события "нажатие на кнопку"
def resh():
    try:
        # Присвоение переменным значений, полученных из полей ввода
        A, B, C = int(ft_entry.get()), int(sd_entry.get()), int(td_entry.get())
        a = (A > 0)
        b = (B > 0)
        c = (C > 0)
        x = (a and b and c)

        p = Label(text=f"Каждое из чисел A, B, C положительное: {x}", font='Sans-serif 15')
        p.place(x=19, y=250)
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный ввод")

# Кнопка "Ответ"
bt = Button(text='Ответ', fg='white', font='Sans 10', bg='#1E90FF', command=resh)
bt.place(x=20, y=200, width=190)

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
