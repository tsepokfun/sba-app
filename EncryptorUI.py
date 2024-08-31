import tkinter as tk
import ALG
from tkinter import filedialog


def EQer0() :
    temp = 0
    def uploadFile () :
        global temp
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        temp = 0
        temp = open(str(location), "r")
        temp = temp.readlines()
        ttt = ""
        for i in temp :
            ttt += i
        FileShowingBox.set(ttt)


    def hits() :
        global temp 
        a = temp
        a = ALG.Return_WordToAscii(a)
        print(a)
        a = ALG.Return_AsciiNumberPuseK(a, int(value.get()))
        print(a)
        a = ALG.Return_AsciiToPrintableWord(a)
        print(a)
        FileShowingBox.set(a)

    w = tk.Tk()
    w.title("「位移加密法」加密器")

    FileShowingBox = tk.StringVar()

    KValueString = tk.Label(w, text = "k值" , width = 25, height  = 2)
    optionList = []
    value = tk.StringVar()
    value.set(0)
    for i in range(27) :
        optionList.append(i)
    KValue = tk.OptionMenu(w, value, *optionList) 


    bOfChooseFile = tk.Button(w, text = "上載密文檔案" , width = 15, height  = 2, command = uploadFile)

    content = tk.Label(w, textvariable = FileShowingBox, width = 40, height = 8, bg = "white", justify = "left")

    BOfProcess = tk.Button(w, text = "加密", command = hits)

    KValue.grid(row = 1, column = 1)
    KValueString.grid(row = 1, column = 0)
    tk.Label(w, text = "密文預覽", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 2, column = 0)

    BOfProcess.grid(row = 4, column = 1)
    content.grid(row = 3, column = 0)
    bOfChooseFile.grid(row = 4 , column = 0, ipadx = '3', ipady = '3', padx = '10', pady = '20')


    w.mainloop()


