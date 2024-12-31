import tkinter as tk
import ALG
import EncryptorUI
import DecryptorUI
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def showresult0(pw, location0) :
    def SelectFileToSave() :
        global temp
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        temp = 0
        temp = open(str(location), "w")
        ttt = FileShowingBox.get()
        for i in ttt :
            temp.write(i)
        temp.close()
    def SaveF() :
        global temp
        temp = 0
        temp = open(str(location0), "w")
        ttt = FileShowingBox.get()
        for i in ttt :
            temp.write(i)
        temp.close()
    def hits0() :
        x = [] 
        for i in range(26) :
            x.append(str(i))
        t2 = pw.DictionaryMethodPossiblity
        print(pw.DictionaryMethodPossiblity)
        h = []
        for i in range(26) :
            h.append(t2[((26 - pw.DictionaryMethodKValue) + i - pw.DictionaryMethodKValue) % 26 ])
        plt.bar(x,h)
        plt.show()
    w = tk.Tk()
    w.title("解密結果")

    FileShowingBox = tk.StringVar(w)

    def show(*e):
        a = pw.Asciiw
        a = ALG.Return_AsciiNumberPuseK(a, 26 - int(value.get()))
        a = ALG.Return_AsciiToPrintableWord(a)
        FileShowingBox.set(a)
    KValueString = tk.Label(w, text = "設置k值" , width = 25, height  = 2)
    optionList = []
    value = tk.StringVar(w)
    value.set(pw.DictionaryMethodKValue)
    for i in range(26) :
        optionList.append(i)
    KValue = tk.OptionMenu(w, value, *optionList)
    KValue.config(width = 8, height  = 2)
    value.trace('w', show) 
    
    FileShowingBox.set(pw.DictionaryMethodOriganArticle)
    content = tk.Label(w, textvariable = FileShowingBox, width = 40, height = 8, bg = "white", justify = "left")
    tk.Button(w, text = "k值準確度圖表", padx = 10, pady = 10, command = hits0).grid(row = 4, column = 1)
    tk.Label(w, text = "k值解密結果 "+ str(pw.DictionaryMethodKValue) ).grid(row = 4, column = 0)
    tk.Button(w, text = "將明文覆寫於原檔", padx = 10, pady = 10, command = SaveF).grid(row = 5, column = 0)
    tk.Button(w, text = "選擇儲存於其他檔案", padx = 10, pady = 10, command = SelectFileToSave).grid(row = 5, column = 1)
    

    KValue.grid(row = 1, column = 1)
    KValueString.grid(row = 1, column = 0)
    tk.Label(w, text = "解密結果預覽", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 0, column = 0)
    content.grid(row = 3, column = 0)

    w.mainloop()


def showresult1(pw, location0) :
    def SelectFileToSave() :
        global temp
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        temp = 0
        temp = open(str(location), "w")
        ttt = FileShowingBox.get()
        for i in ttt :
            temp.write(i)
        temp.close()
    def SaveF() :
        global temp
        temp = 0
        temp = open(str(location0), "w")
        ttt = FileShowingBox.get()
        for i in ttt :
            temp.write(i)
        temp.close()
    def hits0() :
        x = [] 
        for i in range(26) :
            x.append(chr(ord("A") + i))
        
        print(pw.wordFrequency)
        h = pw.wordFrequency
        plt.bar(x,h)
        plt.show()
    w = tk.Tk()
    w.title("解密結果")

    FileShowingBox = tk.StringVar(w)

    def show(*e):
        a = pw.Asciiw
        a = ALG.Return_AsciiNumberPuseK(a, 26 - int(value.get()))
        a = ALG.Return_AsciiToPrintableWord(a)
        FileShowingBox.set(a)
    KValueString = tk.Label(w, text = "設置k值" , width = 25, height  = 2)
    optionList = []
    value = tk.StringVar(w)
    value.set(pw.WordFrewuencyMethodKValue)
    for i in range(26) :
        optionList.append(i)
    KValue = tk.OptionMenu(w, value, *optionList)
    KValue.config(width = 8, height  = 2)
    value.trace('w', show) 
    
    FileShowingBox.set(pw.WordFrewuencyMethodOriganArticle)
    content = tk.Label(w, textvariable = FileShowingBox, width = 40, height = 8, bg = "white", justify = "left")
    tk.Button(w, text = "k值準確度圖表", padx = 10, pady = 10, command = hits0).grid(row = 4, column = 1)
    tk.Label(w, text = "k值解密結果 "+ str(pw.WordFrewuencyMethodKValue) ).grid(row = 4, column = 0)
    tk.Button(w, text = "將明文覆寫於原檔", padx = 10, pady = 10, command = SaveF).grid(row = 5, column = 0)
    tk.Button(w, text = "選擇儲存於其他檔案", padx = 10, pady = 10, command = SelectFileToSave).grid(row = 5, column = 1)
    

    KValue.grid(row = 1, column = 1)
    KValueString.grid(row = 1, column = 0)
    tk.Label(w, text = "解密結果預覽", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 0, column = 0)
    content.grid(row = 3, column = 0)

    w.mainloop()

def showresult2(pw, location0) :
    def SelectFileToSave() :
        global temp
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        temp = 0
        temp = open(str(location), "w")
        ttt = FileShowingBox.get()
        for i in ttt :
            temp.write(i)
        temp.close()
    def SaveF() :
        global temp
        temp = 0
        temp = open(str(location0), "w")
        ttt = FileShowingBox.get()
        for i in ttt :
            temp.write(i)
        temp.close()
    
    w = tk.Tk()
    w.title("解密結果")

    FileShowingBox = tk.StringVar(w)

    
    FileShowingBox.set(pw.M2P)
    content = tk.Label(w, textvariable = FileShowingBox, width = 40, height = 8, bg = "white", justify = "left")
    tk.Button(w, text = "將明文覆寫於原檔", padx = 10, pady = 10, command = SaveF).grid(row = 5, column = 0)
    tk.Button(w, text = "選擇儲存於其他檔案", padx = 10, pady = 10, command = SelectFileToSave).grid(row = 5, column = 1)
    
    tk.Label(w, text = "解密結果預覽", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 0, column = 0)
    content.grid(row = 3, column = 0)

    w.mainloop()


