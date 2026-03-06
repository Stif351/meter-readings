
from tkinter import ttk, SUNKEN, W, font
import tkinter as tk



import main_1
import utill
from ut import MyExtraWindow  # Імпорт класу

def add_check():

    new_win = MyExtraWindow(root)

    new_win.grab_set()


def add_date():
    main_1.add_app(root)


def confirm_exit():
    root.destroy()


# ================================ MAIN WINDOW  =================================================

root = tk.Tk()
root.title("MAIN WINDOW")

window_width = 1000
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.configure(bg="#2c3e40")
root.resizable(False, False)

courier_10 = font.Font(family="Courier", size=10, weight=font.BOLD)
courier_14 = font.Font(family="Courier", size=14, weight=font.BOLD)
courier_18 = font.Font(family="Courier", size=18, weight=font.BOLD)


lf_m= ttk.Frame(root, borderwidth=10, relief=SUNKEN)
lf_m.config(width=750, height=200)

label = tk.Label(lf_m, text="ДОДАВАННЯ ПОКАЗНИКІВ ЛІЧИЛЬНИКІВ У ФАЙЛ І ДРУК КВИТАНЦІЙ", fg="BLUE", font=courier_18)
label.grid(row=0, column=0, columnspan=3, ipadx=6, ipady=6, padx=50, pady=15)

add_dates = tk.Button(lf_m, text="ДОДАТИ ПОКАЗНИКИ", font=courier_10, state='normal', command=add_date)
add_dates.grid(row=3, column=0, ipadx=6, ipady=6, padx=50, pady=30)

merges = tk.Button(lf_m, text="ОБ'ЄДНАТИ КВИТАНЦІЇ", font=courier_10, state='normal', command=add_check)
merges.grid(row=3, column=2, ipadx=6, ipady=6, padx=50, pady=30)

exit_btn = tk.Button(lf_m, text="ЗАВЕРШИТИ", font=courier_10, foreground='red', command=confirm_exit)
exit_btn.grid(row=3, column=1, ipadx=6, ipady=6, padx=50, pady=30)

lf_m.grid(column=3, row=1, ipadx=16, ipady=16, padx=20, pady=20, sticky=W)

root.mainloop()