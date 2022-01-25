from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.title('Create an account')
root.geometry('440x500')
root.resizable(False, False)
root['bg'] = 'white'

# Функция-обработчик события "закрытие главного окна"
def close():
    root.destroy()
    root.quit()


main_label = Label(text='Create an account', font='Sans-serif 15', bg='white')
main_label.place(x=20, y=20)
pls_label = Label(text='Please complete all fields', font='Sans-serif 10', bg='white')
pls_label.place(x=20, y=50)

#"Имя"
fn_label = Label(text='First Name', font='Sans-serif 9', bg='white')
fn_label.place(x=20, y=85)
fn_entry = Entry(highlightthickness=1)
fn_entry.place(x=22, y=105, width=190)
# красная звёздочка
fn_star = Label(text='*', font='Georgia 10', fg='red', bg='white')
fn_star.place(x=83, y=90, height=10)

#"Фамилия"
ln_label = Label(text='Last Name', font='Sans-serif 9', bg='white')
ln_label.place(x=225, y=85)
ln_entry = Entry(highlightthickness=1)
ln_entry.place(x=227, y=105, width=190)
# красная звёздочка
fn_star = Label(text='*', font='Georgia 10', fg='red', bg='white')
fn_star.place(x=288, y=90, height=10)

#"Должность"
job_label = Label(text='Job Title', font='Sans-serif 9', bg='white')
job_label.place(x=20, y=135)
job_entry = Entry(highlightthickness=1)
job_entry.place(x=22, y=155, width=190)
# красная звёздочка
job_star = Label(text='*', font='Georgia 10', fg='red', bg='white')
job_star.place(x=70, y=133)

#"Эл. почта"
email_label = Label(text='Email', font='Sans-serif 9', bg='white')
email_label.place(x=225, y=135)
email_entry = Entry(highlightthickness=1)
email_entry.place(x=227, y=155, width=190)
# красная звёздочка
email_star = Label(text='*', font='Georgia 10', fg='red', bg='white')
email_star.place(x=260, y=133)

#"Пароль"
pass_label = Label(text='Password', font='Sans-serif 9', bg='white')
pass_label.place(x=20, y=185)
pass_entry = Entry(highlightthickness=1)
pass_entry.place(x=22, y=205, width=190)
# красная звёздочка
pass_star = Label(text='*', font='Georgia 10', fg='red', bg='white')
pass_star.place(x=79, y=183)

#"Повторите пароль"
re_label = Label(text='Re-enter Password', font='Sans-serif 9', bg='white')
re_label.place(x=225, y=185)
re_entry = Entry(highlightthickness=1)
re_entry.place(x=227, y=205, width=190)
# красная звёздочка
re_star = Label(text='*', font='Georgia 10', fg='red', bg='white')
re_star.place(x=337, y=183)

#"Телефон"
phone_label = Label(text='Phone', font='Sans-serif 9', bg='white')
phone_label.place(x=20, y=235)
phone_entry = Entry(highlightthickness=1)
phone_entry.place(x=22, y=255, width=190)
# красная звёздочка
phone_star = Label(text='*', font='Georgia 10', fg='red', bg='white')
phone_star.place(x=58, y=233)

#"Компания"
company_label = Label(text='Company', font='Sans-serif 9', bg='white')
company_label.place(x=225, y=235)
company_entry = Entry(highlightthickness=1)
company_entry.place(x=227, y=255, width=190)
# красная звёздочка
company_star = Label(text='*', font='Georgia 10', fg='red', bg='white')
company_star.place(x=282, y=233)

#"Работник"
empl_label = Label(text='Employees', font='Sans-serif 9', bg='white')
empl_label.place(x=20, y=295)
# Выпадающий список с должностями??
empl_combobox = Combobox(values=('...', '...', '...'))
empl_combobox.place(x=22, y=315, width=190)
# красная звёздочка
empl_star = Label(text='*', font='Georgia 10', fg='red', bg='white')
empl_star.place(x=85, y=293)

#"Страна"
country_label = Label(text='Country', font='Sans-serif 9', bg='white')
country_label.place(x=225, y=295)
# Выпадающий список со странами
country_combobox = Combobox(values=('Russia', 'USA', 'Belarus'))
country_combobox.place(x=227, y=315, width=190)
# красная звёздочка
country_star = Label(text='*', font='Georgia 10', fg='red', bg='white')
country_star.place(x=271, y=293)

# Кнопка "Галочка"
receiving_check = Checkbutton(bg='white')
receiving_check.place(x=19, y=355)
receiving_label = Label(text='I give consent to receiving text messages (carrier charges may apply)',
                        font='Sans-serif 8',
                        bg='white',
                        fg='#696969')
receiving_label.place(x=42, y=358)

# Кнопка "Галочка"
terms_check = Checkbutton(bg='white')
terms_check.place(x=19, y=385)
terms_label = Label(text='I accept the Terms of Use',
                    font='Sans-serif 8',
                    bg='white',
                    fg='#696969')
terms_label.place(x=42, y=388)

# Кнопка "Регистрация"
button = Button(text='Sign up',
                fg='white',
                font='Sans 10',
                bg='#1E90FF')
button.place(x=19, y=440, width=190)

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
