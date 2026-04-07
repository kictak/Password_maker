import tkinter as tk
from tkinter import ANCHOR, CENTER, Button, ttk
import time
from types import CellType
import password_play as pp

## Присвоение root - Tk + навзание + размер окна приложения + запрет на изменение окна
root = tk.Tk()
root.title("RedPass")
root.geometry("400x200+760+440")
root.resizable(False, False)
size = 8
good_password = "Тут чего-то не хватает...??"


## Выбор длинны пароля
def change(new_value):
    size = int(float(new_value))
    pass_size["text"] = size
    print(size)


## Отображение выбраного размера пароля
pass_size = ttk.Label()
pass_size.pack(anchor="nw")
pass_size.place(x=270, y=100, width=19, height=20)

## Настройка стиля виджетов
style = ttk.Style()
style.theme_use("clam")
# настрока стимле ползунка - scale
style.configure(
    "TScale",  #  отвечает за стиль всех ползунков для изменеиния
    #  конреткного виджета мне надо писать "My.TScale"
    #  и указывать в парметрах style="My.TScale"
    background="white",
    troughcolor="gray",
    sliderlength=10,
)
# настройка стиля текстового окна
style.configure("My.Textstyle", background="gray")


## Текстовая вставка выберите размер пароля
info_pass_size = tk.Label(text="Выберите длину пароля")
info_pass_size.place(x=100, y=80, width=210, height=20)

## Ползунок выбора размера пароля
scale = ttk.Scale(orient="horizontal", length=200, from_=8, to=50, command=change)
scale.pack(anchor="nw")
scale.place(x=120, y=100, width=150, height=20)


# pp.generate_password(int(scale.get()))
ready_password = tk.Label(text=good_password)
ready_password.place(x=0, y=20, width=400, height=20)
ready_password.configure(background="white")


## Вывод пароля
def gen_pass():
    size = int(scale.get())
    ready_password["text"] = pp.generate_password(size)
    print(good_password)


## Иконка приложения
root.iconbitmap(r"./icon.ico")


## Кнопка запроса генерации пароля
open_button = ttk.Button(text="Сгенерировать пароль", command=gen_pass)
open_button.place(x=120, y=130, width=155, height=35)


root.mainloop()
