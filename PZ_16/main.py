import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#3380ff', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="BD/add.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить запись', command=self.open_dialog, bg='#0B54FA', bd=0,
                                         compound=tk.TOP, image=self.add_img, fg="white")
        self.btn_open_dialog.pack(side=tk.LEFT, padx=65)

        self.update_img = tk.PhotoImage(file="BD/update.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#0B54FA',
                                    bd=0, compound=tk.TOP, image=self.update_img, fg="white")
        btn_edit_dialog.pack(side=tk.LEFT, padx=65)

        self.delete_img = tk.PhotoImage(file="BD/delete.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#0B54FA',
                               bd=0, compound=tk.TOP, image=self.delete_img, fg="white")
        btn_delete.pack(side=tk.LEFT, padx=65)

        self.search_img = tk.PhotoImage(file="BD/search.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#0B54FA',
                               bd=0, compound=tk.TOP, image=self.search_img, fg="white")
        btn_search.pack(side=tk.LEFT, padx=65)

        self.refresh_img = tk.PhotoImage(file="BD/refresh.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#0B54FA',
                                bd=0, compound=tk.TOP, image=self.refresh_img, fg="white")
        btn_refresh.pack(side=tk.LEFT, padx=65)

        self.tree = ttk.Treeview(self, columns=('repair_id', 'name', 'plant', 'price', 'date', 'doc', 'spec', 'sell'), height=15, show='headings')

        self.tree.column('repair_id', width=50, anchor=tk.CENTER)
        self.tree.column('name', width=180, anchor=tk.CENTER)
        self.tree.column('plant', width=140, anchor=tk.CENTER)
        self.tree.column('price', width=140, anchor=tk.CENTER)
        self.tree.column('date', width=180, anchor=tk.CENTER)
        self.tree.column('doc', width=140, anchor=tk.CENTER)
        self.tree.column('spec', width=140, anchor=tk.CENTER)
        self.tree.column('sell', width=140, anchor=tk.CENTER)

        self.tree.heading('repair_id', text='ID')
        self.tree.heading('name', text='Марка телевизора')
        self.tree.heading('plant', text='Завод-изготовитель')
        self.tree.heading('price', text='Цена')
        self.tree.heading('date', text='Дата ремонта')
        self.tree.heading('doc', text='Документ')
        self.tree.heading('spec', text='Мастер')
        self.tree.heading('sell', text='Сумма оплаты')

        self.tree.pack()

    def records(self, name, plant, price, date, doc, spec, sell):
        self.db.insert_data(name, plant, price, date, doc, spec, sell)
        self.view_records()

    def update_record(self, name, plant, price, date, doc, spec, sell):
        self.db.cur.execute("""UPDATE repair SET name=?, plant=?, price=?, date=?, doc=?, spec=?, sell=? WHERE repair_id=?""",
                            (name, plant, price, date, doc, spec, sell, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM repair""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM repair WHERE repair_id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, repair_id):
        repair_id = ("%" + repair_id + "%",)
        self.db.cur.execute("""SELECT * FROM repair WHERE name LIKE ?""", repair_id)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    # def search_records(self, score):
    #     score = (score,)
    #     self.db.cur.execute("""SELECT * FROM repair WHERE score>?""", score)
    #     [self.tree.delete(i) for i in self.tree.get_children()]
    #     [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить запись')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_name = tk.Label(self, text='Марка телевизора')
        label_name.place(x=1, y=25)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=115, y=25)

        label_plant = tk.Label(self, text='Завод-изготовитель')
        label_plant.place(x=1, y=50)
        self.entry_plant = ttk.Entry(self)
        self.entry_plant.place(x=115, y=50)

        label_price = tk.Label(self, text='Цена(₽)')
        label_price.place(x=1, y=75)
        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=115, y=75)

        label_date = tk.Label(self, text='Дата ремонта')
        label_date.place(x=1, y=100)
        self.entry_date = ttk.Entry(self)
        self.entry_date.place(x=115, y=100)

        label_doc = tk.Label(self, text='Документ')
        label_doc.place(x=1, y=125)
        self.entry_doc = ttk.Entry(self)
        self.entry_doc.place(x=115, y=125)

        label_spec = tk.Label(self, text='Мастер')
        label_spec.place(x=1, y=150)
        self.entry_spec = ttk.Entry(self)
        self.entry_spec.place(x=115, y=150)

        label_sell = tk.Label(self, text='Сумма оплаты(₽)')
        label_sell.place(x=1, y=175)
        self.entry_sell = ttk.Entry(self)
        self.entry_sell.place(x=115, y=175)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=323, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=245, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_name.get(),
                                                                       self.entry_plant.get(),
                                                                       self.entry_price.get(),
                                                                       self.entry_date.get(),
                                                                       self.entry_doc.get(),
                                                                       self.entry_spec.get(),
                                                                       self.entry_sell.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=309, y=140)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_name.get(),
                                                                          self.entry_plant.get(),
                                                                          self.entry_price.get(),
                                                                          self.entry_date.get(),
                                                                          self.entry_doc.get(),
                                                                          self.entry_spec.get(),
                                                                          self.entry_sell.get()))

        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск по марке телевизора")
        label_search.place(x=45, y=1)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=50, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=125, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=50, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('BD/saper.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS repair (
                repair_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                plant INTEGER NOT NULL,
                price INTEGER NOT NULL,
                date DATE NOT NULL,
                doc INTEGER NOT NULL,
                spec TEXT NOT NULL,
                sell INTEGER NOT NULL
                )""")

    def insert_data(self, name, plant, price, date, doc, spec, sell):
        self.cur.execute("""INSERT INTO repair (name, plant, price, date, doc, spec, sell) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                         (name, plant, price, date, doc, spec, sell))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Телемастерская")
    root.geometry("1114x450+800+200")
    root.configure(bg='#3380ff')
    root.iconphoto(True, tk.PhotoImage(file='BD/telik.png'))
    root.resizable(False, False)
    root.mainloop()
