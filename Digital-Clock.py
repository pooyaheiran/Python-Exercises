import tkinter as tk
from time import strftime

window = tk.Tk()
window.title('clock')
window.resizable(0,0)


def GetTime():
    get_time = strftime("%H:%M:%S")
    label.config(text=get_time)
    label.after(1000,GetTime)
    

label = tk.Label(window,font=('',40),foreground='#AAFF00',background='black')
label.pack()
GetTime()

tk.mainloop()
