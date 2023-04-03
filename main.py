import random
from tkinter import *
import string


app=Tk()

x = 30
i = 0
numeroAcertos = 0
numeroErros = 0
##contagem de letras na palavra
numbOfLetters = 0

file = open('forca.txt', 'r')
content = file.readlines()
content = [x.strip('\n') for x in content]
randWord = random.choices(content)
wordString = str(randWord).strip("[']")
numberCharacter = len(wordString)

letter = Entry(app)
letter.place(x=10, y=80, width=20, height=20)
letra = ''
def getData():
    print(letter.get())
    letra = letter.get()
    print(letra)

Button(app, text="Input", command=getData).place(x=10, y=270, width=100, height=20)

print(numberCharacter, (wordString))

if letra not in wordString:
    print("n tem")
    numeroErros += 1
    #errou
else:
    numeroAcertos = wordString.count(letra)
    print(numeroAcertos)

while numbOfLetters < numberCharacter:

    app.title("Forca")
    app.geometry("1000x600")
    app.configure(background="#000000")
    txt = Label(app, text=numeroErros, background="#000", foreground="#FFF")
    txt.place(x=10, y=10, width=20, height=20, )

    correctLatters = Label(app, text=wordString[i], font=("Arial", 14), background="#000", foreground="#FFF")
    correctLatters.place(x=x, y=100, width=20, height=15)
    underLines = Label(app, text="____", background="#000", foreground="#FFF")
    underLines.place(x=x, y=100, width=20, height=15)

    if wordString[i] == letter:
        # acertou
        correctLatters.lift()
    numbOfLetters += 1
    i += 1
    x += 30


app.mainloop()
#======================================================================= 
"""
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Calculate the Square Root')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type your Number:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def get_square_root():
    x1 = entry1.get()

    label3 = tk.Label(root, text='The Square Root of ' + x1 + ' is:', font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    label4 = tk.Label(root, text=float(x1) ** 0.5, font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)

button1 = tk.Button(text='Get the Square Root', command=get_square_root, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()

"""