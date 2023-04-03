import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

# main loop
while run:
    app = Tk()
    app.geometry('905x700')
    app.title('HANG MAN')
    app.config(bg='#E7FFFF')
    count = 0
    win_count = 0

    # letters icon
    al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
    for let in al:
        exec('{}=PhotoImage(file="{}.png")'.format(let, let))

    # hangman images

    # letters placement
    button = [['b1', 'a', 10, 595], ['b2', 'b', 70, 595], ['b3', 'c', 140, 595], ['b4', 'd', 210, 595],
              ['b5', 'e', 280, 595], ['b6', 'f', 350, 595], ['b7', 'g', 420, 595], ['b8', 'h', 490, 595],
              ['b9', 'i', 560, 595], ['b10', 'j', 630, 595], ['b11', 'k', 700, 595], ['b12', 'l', 770, 595],
              ['b13', 'm', 840, 595], ['b14', 'n', 0, 645], ['b15', 'o', 70, 645], ['b16', 'p', 140, 645],
              ['b17', 'q', 210, 645], ['b18', 'r', 280, 645], ['b19', 's', 350, 645], ['b20', 't', 420, 645],
              ['b21', 'u', 490, 645], ['b22', 'v', 560, 645], ['b23', 'w', 630, 645], ['b24', 'x', 700, 645],
              ['b25', 'y', 770, 645], ['b26', 'z', 840, 645]]

    for q1 in button:
        exec(
            '{}=Button(app,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(
                q1[0], q1[1], q1[0], q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0], q1[2], q1[3]))

    numeroAcertos = 0
    numeroErros = 0
    ##contagem de letras na palavra


    file = open('forca.txt', 'r')
    content = file.readlines()
    content = [x.strip('\n') for x in content]
    randWord = random.choices(content)
    wordString = str(randWord).strip("[']")
    numberCharacter = len(wordString)

    print(numberCharacter, (wordString))

    def check(letter,button):
        i=0
        global numbOfLetters,i1,x1
        print(letter)
        if letter in wordString:
            indices = []
            start_index = 0
            while True:
                try:
                    index = wordString.index(letter, start_index)
                    indices.append(index)
                    start_index = index + 1
                except ValueError:
                    break
            print(indices)
        x1 = 30
        i1 = 0
        numbOfLetters = 0
        while numbOfLetters < numberCharacter:
            correctLatters = Label(app, text=wordString[i1], font=("Arial", 14), background="#E7FFFF",foreground="#000")
            correctLatters.place(x=x1, y=100, width=20, height=15)

            underLines = Label(app, text="____", background="#E7FFFF", foreground="#000")
            underLines.place(x=x1, y=100, width=20, height=15)
            if wordString[i1] == letter:
                # acertou
                correctLatters.lift()
            numbOfLetters += 1
            i1 += 1
            x1 += 25


    app.mainloop()
