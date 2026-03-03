
from tkinter import ttk
import tkinter as tk
from tkinter import font


import main_1
import utill


def add_date():
    # about_win = tk.Toplevel(root)
    # about_win.title("Внесення показників")
    # about_win.geometry("900x600")
    # about_win.configure(bg="#2c3e50")  # Власний колір фону

    # btn = tk.Button(about_win, text="ENTER")
    # btn.grid(row=3, column=0, ipadx=6, ipady=6, padx=50, pady=30)
    main_1.add_app(root)
    # about_win.grab_set()



def add_check():
    # about_win = tk.Toplevel(root)
    # about_win.title("Об'єднання квітанцій")
    # about_win.geometry("900x600")
    # about_win.configure(bg="#2c3e40")  # Власний колір фону
    #
    # about_win.grab_set()

    utill.print_check(root)

def confirm_exit():
    root.destroy()


# ================================ MAIN WINDOW  =================================================

root = tk.Tk()
root.title("MAIN WINDOW")
root.geometry("900x400")
root.resizable(False, False)

courier_10 = font.Font(family="Courier", size=10, weight=font.BOLD)
courier_14 = font.Font(family="Courier", size=14, weight=font.BOLD)
courier_18 = font.Font(family="Courier", size=18, weight=font.BOLD)
width_frame = 800
height_frame = 600

label = tk.Label(root, text="ДОДАВАННЯ ПОКАЗНИКІВ ЛІЧИЛЬНИКІВ У ФАЙЛ І ДРУК КВІТАНЦІЇ", fg="BLUE", font=courier_18)
label.grid(row=0, column=0, columnspan=3, ipadx=6, ipady=6, padx=5, pady=15)

add_dates = tk.Button(root, text="ДОДАТИ ПОКАЗНИКИ", font=courier_10, state='normal', command=add_date)
add_dates.grid(row=3, column=0, ipadx=6, ipady=6, padx=50, pady=30)

merges = tk.Button(root, text="ОБ'ЄДНАТИ КВІТАНЦІЇ", font=courier_10, state='normal', command=add_check)
merges.grid(row=3, column=1, ipadx=6, ipady=6, padx=50, pady=30)

exit_btn = tk.Button(root, text="ЗАВЕРШИТИ", font=courier_10, foreground='red', command=confirm_exit)
exit_btn.grid(row=4, column=0, ipadx=6, ipady=6, padx=50, pady=1)

root.mainloop()