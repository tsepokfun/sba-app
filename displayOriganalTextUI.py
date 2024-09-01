import tkinter as tk
import ALG
import EncryptorUI
import DecryptorUI
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def showresult0(pw) :
    def hits0() :
        x = [] 
        for i in range(26) :
            x.append(i + 1)
        h = pw.DictionaryMethodPossiblity.reversed()
        print(pw.DictionaryMethodPossiblity)        
        plt.bar(x,h)
        plt.show()
    w = tk.Tk()
    w.title("解密結果")

    FileShowingBox = tk.StringVar(w)


    def show(*e):
        t0 = value.get()
        a = pw.Asciiw
        a = ALG.Return_AsciiNumberPuseK(a, 26 - int(t0))
        a = ALG.Return_AsciiToPrintableWord(a)
        FileShowingBox.set(a)
    KValueString = tk.Label(w, text = "設置k值" , width = 25, height  = 2)
    optionList = []
    value = tk.StringVar(w)
    value.set(pw.DictionaryMethodKValue)
    for i in range(27) :
        optionList.append(i)
    KValue = tk.OptionMenu(w, value, *optionList)
    KValue.config(width = 8, height  = 2)
    value.trace('w', show) 
    
    FileShowingBox.set(pw.DictionaryMethodOriganArticle)
    content = tk.Label(w, textvariable = FileShowingBox, width = 40, height = 8, bg = "white", justify = "left")
    tk.Button(w, text = "k值準確度圖表", padx = 10, pady = 10, command = hits0).grid(row = 4)


    KValue.grid(row = 1, column = 1)
    KValueString.grid(row = 1, column = 0)
    tk.Label(w, text = "解密結果預覽", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 0, column = 0)
    content.grid(row = 3, column = 0)

    w.mainloop()




