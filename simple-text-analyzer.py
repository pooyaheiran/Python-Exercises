import tkinter as tk

#create window in tkinter
win = tk.Tk()
win.title('simple-text-analyzer')
win.resizable(0,0)
win.configure(bg="#EDF4F2")

#count word in sentence
def word(sentence):
    word_count = len(sentence.split())
    return word_count


#count vowel in a sentence
def vowel(sentence):
    vowel_count = 0
    vowel_list = ["a",'e',"i","o","u","A","E","I","O","U"]
    for i in sentence:
        if i in vowel_list:
            vowel_count += 1
    return vowel_count


#count letters in a sentence
def letter(letters):
    letter_count = 0
    for i in letters:
        letter_count += 1
        if i == ' ':
            letter_count -= 1
    return letter_count  


def show():
    show_word = word(entry.get())
    show_letter = letter(entry.get())
    show_vowel = vowel(entry.get())
    
    lbl.config(text=f"word: {show_word}\n\nletter: {show_letter}\n\nvowel: {show_vowel}")
    lbl.after(100,show)



entry_text = tk.Label(
    
    win,text="enter your text",
    font=("Fira Code",25),background="#EDF4F2",
    foreground="#31473A"

)

entry = tk.Entry(
    
    win,font=("Fira Code",15),
    width=100,background="#EDF4F2",
    foreground="#31473A"
    
)


lbl = tk.Label(
    
    win,text='',
    font=("Fira Code",25),
    foreground="#31473A",
    background="#EDF4F2"

)

entry_text.pack()
entry.pack(side="top")
lbl.pack(pady="50")


show()

win.mainloop()
