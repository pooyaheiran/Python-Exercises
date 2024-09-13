import tkinter as tk

#create window in tkinter
win = tk.Tk()
win.title('word counter')
win.resizable(0,0)
win.configure(bg="black")

#count word in sentence
def word(sentence):
    word = 1
    for i in sentence:
        if i == ' ':
            word += 1
    return word 


#count vowel in sentence
def vowel(sentence):
    vowel_count = 0
    vowel_list = ["a",'e',"i","o","u","A","E","I","O","U"]
    for i in sentence:
        if i in vowel_list:
            vowel_count += 1
    return vowel_count


#count letters in sentence
def letter(letters):
    letter_count = 0
    for i in letters:
        letter_count += 1
        if i == ' ':
            letter_count -= 1
    return letter_count  

#function to show 
def show():
    show_word = word(entry.get())
    show_vowel = vowel(entry.get())
    show_letter = letter(entry.get())
    lbl.config(text=f"word: {show_word} \n\nletter: {show_letter}\n\nvowel: {show_vowel}")
    lbl.after(100,show)


entry = tk.Entry(win,font=("Fira Code",15),width=100,background="black",foreground="#008000")
lbl = tk.Label(win,text='',font=("",15,"bold"),foreground="green",background="black")

entry.pack(side="top")
lbl.pack(side="left")

show()
win.mainloop()


