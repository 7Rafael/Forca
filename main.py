import random
import tkinter
from tkinter import *
from tkinter.messagebox import *
import time
run = True

# main loop
while run:
    maxError = 0
    dif = Tk()
    dif.geometry('200x200')
    dif.title("dificulty")
    def normal():
        global maxError
        maxError = 6
        dif.destroy()
    def tormento():
        global maxError
        print("tormento")
        maxError = 4
        dif.destroy()
    def inferno():
        global maxError
        print("inferno")
        maxError = 2
        dif.destroy()
    def nightmere():
        global maxError
        print("nightmere")
        maxError = 1
        dif.destroy()
    def exitDif():
        dif.quit()
    b1 = Button(dif,text='Normal', command=normal)
    b2 = Button(dif,text='tormento', command=tormento)
    b3 = Button(dif,text='inferno', command=inferno)
    b4 = Button(dif,text='nightmere', background="#000", foreground="#FFF",command=nightmere)
    exit = Button(dif,text='exit',  background="#FF0000", foreground="#FFF",command=exitDif)

    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    exit.pack()

    dif.mainloop()
    def exit():
        app.destroy()

    app = Tk()
    app.title('HANG MAN')
    app.config(bg='#b0ffff')
    app.geometry('905x700')
    count = 0
    win_count = 0
    # hangman images
    h123 = ['h1','Hangman1','Hangman2','Hangman3','Hangman4','Hangman5','Hangman6']
    for hangman in h123:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman,hangman))

    # letters icon
    al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
    for let in al:
        exec('{}=PhotoImage(file="{}.png")'.format(let, let))
    # hangman images
    # letters placement
    button = [['b1', 'a', 0, 595], ['b2', 'b', 70, 595], ['b3', 'c', 140, 595], ['b4', 'd', 210, 595],
              ['b5', 'e', 280, 595], ['b6', 'f', 350, 595], ['b7', 'g', 420, 595], ['b8', 'h', 490, 595],
              ['b9', 'i', 560, 595], ['b10', 'j', 630, 595], ['b11', 'k', 700, 595], ['b12', 'l', 770, 595],
              ['b13', 'm', 840, 595], ['b14', 'n', 0, 645], ['b15', 'o', 70, 645], ['b16', 'p', 140, 645],
              ['b17', 'q', 210, 645], ['b18', 'r', 280, 645], ['b19', 's', 350, 645], ['b20', 't', 420, 645],
              ['b21', 'u', 490, 645], ['b22', 'v', 560, 645], ['b23', 'w', 630, 645], ['b24', 'x', 700, 645],
              ['b25', 'y', 770, 645], ['b26', 'z', 840, 645]]
    for q1 in button:
        exec(
            '{}=Button(app,bd=0,command=lambda:check("{}","{}"),bg="#b0ffff",activebackground="#E7FFFF",font=10,image={})'.format(
                q1[0], q1[1], q1[0], q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0], q1[2], q1[3]))

        # hangman placement
        han = [['c1', 'h1'], ['c2', 'Hangman1'], ['c3', 'Hangman2'], ['c4', 'Hangman3'], ['c5', 'Hangman4'], ['c6', 'Hangman5'], ['c7', 'Hangman6']]
        for p1 in han:
            exec('{}=Label(app,bg="#b0ffff",image={})'.format(p1[0], p1[1]))

        # placement of first hangman image
        c1.place(x=300, y= 150)

    exit = Button(text='exit', command=exit, background="#FF0000",foreground="#FFF")
    exit.place(x=840, y = 10)


    numberCorrect = 0
    numberWrong = 0
    hangmanCount = 0
    posWrongLetters = 30
    ##contagem de letras na palavra
    file = open('forca.txt', 'r')
    content = file.readlines()
    content = [x.strip('\n') for x in content]
    randWord = random.choices(content)
    wordString = str(randWord).strip("[']")
    numberCharacter = len(wordString)
    print(numberCharacter, (wordString))
    initialized = False
    chances = 0

    def check(letter, button):

        global initialized, numbOfLetters, i1, x1,chances
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
        if not initialized:
            while numbOfLetters < numberCharacter and initialized == False:
                underLines = Label(app, text="____", background="#b0ffff", foreground="#000")
                underLines.place(x=x1, y=100, width=20, height=25)
                numbOfLetters += 1
                i1 += 1
                x1 += 25
            initialized = True
        i1 = 0
        x1 = 30
        errors = 0
        for i in range(numberCharacter):
            global numberCorrect, numberWrong, run, posWrongLetters, hangmanCount
            exec('{}.destroy()'.format(button))
            correctLatters = Label(app, text=wordString[i], font=("Arial", 14), background="#b0ffff", foreground="#000")
            if wordString[i] == letter:
                correctLatters.place(x=x1, y=100, width=20, height=25)
                numberCorrect += 1
                if numberCorrect == numberCharacter:
                    tkinter.messagebox.showinfo(title="Ganhou", message="Parabéns, você desvendou a palavra")
                    result = tkinter.messagebox.askquestion(title="Jogar novamente", message="Deseja jogar novamente?")
                    if result == 'yes':
                        run = True
                        app.destroy()
                    else:
                        run = False
                        app.destroy()
            else:
                errors += 1

            x1 += 25
        chances += 1

        if letter not in wordString:
            hangmanCount += 1
            numberErrors =Label(text=numberWrong, font=("Arial", 14), background="#b0ffff", foreground="#000")
            numberErrors.place(x=150, y=150, width=200, height=25)

            lettersUsed = Label(text="Letras utilizadas", font=("Arial", 14), background="#b0ffff", foreground="#000")
            lettersUsed.place(x=10, y=150, width=200, height=25)

            letters = Label(text=letter, font=("Arial", 13), background="#b0ffff", foreground="#000")
            letters.place(x=posWrongLetters , y=200, width=20, height=25)


            exec('c{}.destroy()'.format(hangmanCount))
            exec('c{}.place(x={},y={})'.format(hangmanCount + 1, 300, 150))
            if hangmanCount == 6:
                hangmanCount = 5
            posWrongLetters += 20
            numberWrong += 1


        if numberWrong > maxError-1:
            print("imagem")
            tkinter.messagebox.showerror(title="Perdeu", message="Fim de jogo, você perdeu ")
            result = tkinter.messagebox.askquestion(title="Jogar novamente", message="Deseja jogar novamente?")
            if result =='yes':
                run = True
                app.destroy()
            else:
                run = False
                app.destroy()
    app.mainloop()
