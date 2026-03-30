import tkinter as tk
from tkinter import ANCHOR, CENTER, Button, ttk
import time
from types import CellType


root = tk.Tk()
root.title("RedPass")
root.geometry("400x200+760+440")
root.resizable(False, False)

# кнопка запроса генерации пароля
open_button = ttk.Button(text="Сгенерировать пароль")
open_button.place(x=120, y=130, width=155, height=35)

# вывод сегенрированного пароля


## Выбор длинны пароля
def change(new_val):
    pass_size["text"] = int(scale.get())


pass_size = ttk.Label()
pass_size.pack(anchor="nw")
pass_size.place(x=270, y=100, width=19, height=20)
##

## Настройка стиля для Scale
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TScale",
    background="white",
    troughcolor="gray",
    sliderlength=10,
)
##
## Текстовая вставка выберите размер пароля
info_pass_size = tk.Label(text="Выберите длину пароля")
info_pass_size.place(x=100, y=80, width=210, height=20)
##
## Ползунок выбора размера пароля
scale = ttk.Scale(orient="horizontal", length=200, from_=8, to=50, command=change)
scale.pack(anchor="nw")
scale.place(x=120, y=100, width=150, height=20)
##

## Иконка приложения
root.iconbitmap(r"./icon.ico")
##

root.mainloop()
print()
