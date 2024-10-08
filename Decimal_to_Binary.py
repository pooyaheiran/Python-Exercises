import tkinter as tk 
from tkinter import ttk

#button def
def convert():  
    GetNum = entry_int.get()
    BinaryList = []
    while(GetNum > 0):
        BinaryList.append(GetNum % 2)
        GetNum = GetNum // 2

    output_string.set(BinaryList[::-1])

#window
window = tk.Tk()
window.title('decimal to binary')
window.geometry('350x120') 

#input label
input_label = ttk.Label(master=window,text = 'enter decimal number ',font =('Calibri 14'),foreground='#023047')
input_label.pack()

#input
inputFrame = ttk.Frame(master=window,width=5)
entry_int = tk.IntVar()
entry = ttk.Entry(master=inputFrame,width=10,textvariable=entry_int)
button = ttk.Button(text= '>',master=inputFrame,command = convert,width=2)
button.pack(side='right',padx=8)
entry.pack(side='right')
inputFrame.pack(pady= 5)

#output label
output_string = tk.StringVar()
output_label = ttk.Label(
     master=window,
     textvariable = output_string,
     text='Binary: ',
     font=('Calibri 14'),
     foreground='#023047'
)

output_label.pack(pady= 5)

#for run 
window.mainloop()
