import tkinter as tk
import ALG
from tkinter import filedialog


def EQer0() :

    temp = 0
    location = ""
    def SelectFileToSave() :
        global temp        
        global location
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        temp = 0
        temp = open(str(location), "w")
        ttt = FileShowingBox.get()
        for i in ttt :
            temp.write(i)
        temp.close()
    def SaveF() :
        global temp        
        global location
        temp = 0
        temp = open(str(location), "w")
        ttt = FileShowingBox.get()
        for i in ttt :
            temp.write(i)
        temp.close()
    def uploadFile () :
        global temp
        global location
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        temp = 0
        temp = open(str(location), "r")
        temp = temp.readlines()
        temp0 = []
        for i in temp :
            temp0.append(i.upper())
        temp = temp0
        ttt = ""
        for i in temp :
            ttt += i
        FileShowingBox.set(ttt)


    def hits() :
        global temp
        global location
        if location != "" :
            a = temp
            a = ALG.Return_WordToAscii(a)
            print(a)
            a = ALG.Return_AsciiNumberPuseK(a, int(value.get()))
            print(a)
            a = ALG.Return_AsciiToPrintableWord(a)
            print(a)
            FileShowingBox.set(a)
        else :
            t0 = tk.Tk()
            t0.title("注意")
            tk.Label(t0, text = "請上載密文檔案", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 1, column = 0)
            t0.mainloop()


    w = tk.Tk()
    w.title("「位移加密法」加密器")

    FileShowingBox = tk.StringVar(w)

    def show(*e):
        global temp
        a = temp
        a = ALG.Return_WordToAscii(a)
        a = ALG.Return_AsciiNumberPuseK(a,int(value.get()))
        a = ALG.Return_AsciiToPrintableWord(a)
        FileShowingBox.set(a)
    KValueString = tk.Label(w, text = "k值" , width = 25, height  = 2)
    optionList = []
    value = tk.StringVar(w)
    value.set(0)
    for i in range(26) :
        optionList.append(i)
    KValue = tk.OptionMenu(w, value, *optionList)
    KValue.config(width = 8, height  = 2)
    value.trace('w', show) 

    bOfChooseFile = tk.Button(w, text = "上載密文檔案" , width = 15, height  = 2, command = uploadFile)

    content = tk.Label(w, textvariable = FileShowingBox, width = 40, height = 8, bg = "white", justify = "left")

    BOfProcess = tk.Button(w, text = "加密", command = hits)

    KValue.grid(row = 1, column = 1)
    KValueString.grid(row = 1, column = 0)
    tk.Label(w, text = "密文預覽", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 0, column = 0)

    #BOfProcess.grid(row = 4, column = 1)
    content.grid(row = 3, column = 0)
    bOfChooseFile.grid(row = 4 , column = 0, ipadx = '3', ipady = '3', padx = '10', pady = '20')
    tk.Button(w, text = "將密文覆寫於原檔", padx = 10, pady = 10, command = SaveF).grid(row = 5, column = 0)
    tk.Button(w, text = "選擇儲存於其他檔案", padx = 10, pady = 10, command = SelectFileToSave).grid(row = 5, column = 1)
    

    w.mainloop()


def EQer1() :

    temp = 0
    location = ""
    def SelectFileToSave() :
        global temp        
        global location
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        temp = 0
        temp = open(str(location), "w")
        ttt = FileShowingBox.get()
        for i in ttt :
            temp.write(i)
        temp.close()
    def SaveF() :
        global temp        
        global location
        temp = 0
        temp = open(str(location), "w")
        ttt = FileShowingBox.get()
        for i in ttt :
            temp.write(i)
        temp.close()
    def uploadFile () :
        global temp
        global location
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        temp = 0
        temp = open(str(location), "r")
        temp = temp.readlines()
        temp0 = []
        for i in temp :
            temp0.append(i.upper())
        temp = temp0
        ttt = ""
        for i in temp :
            ttt += i
        FileShowingBox.set(ttt)


    def hits() :
        global temp
        global location
        if location != "" :
            a = temp
            t = ALG.pre_proess_word(a)
            print(t.M2O)
            FileShowingBox.set(t.M2O)
        else :
            t0 = tk.Tk()
            t0.title("注意")
            tk.Label(t0, text = "請上載密文檔案", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 1, column = 0)
            t0.mainloop()


    w = tk.Tk()
    w.title("「序列編號加密法」加密器")

    FileShowingBox = tk.StringVar(w)


    bOfChooseFile = tk.Button(w, text = "上載密文檔案" , width = 15, height  = 2, command = uploadFile)

    content = tk.Label(w, textvariable = FileShowingBox, width = 40, height = 8, bg = "white", justify = "left")

    BOfProcess = tk.Button(w, text = "加密", command = hits)

    tk.Label(w, text = "密文預覽", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 0, column = 0)

    BOfProcess.grid(row = 4, column = 1)
    content.grid(row = 3, column = 0)
    bOfChooseFile.grid(row = 4 , column = 0, ipadx = '3', ipady = '3', padx = '10', pady = '20')
    tk.Button(w, text = "將密文覆寫於原檔", padx = 10, pady = 10, command = SaveF).grid(row = 5, column = 0)
    tk.Button(w, text = "選擇儲存於其他檔案", padx = 10, pady = 10, command = SelectFileToSave).grid(row = 5, column = 1)
    

    w.mainloop()



def info0() :
    w = tk.Tk()
    w.title("位移方法加密原理")
    tk.Label(w, text = "把每一個字元變為編碼，均位移K位及取模26，再退回成文本\n\n編碼：\nA-Z (1-26)\n\n位移方法：\n（編碼 + K) mod 26", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 2)
    w.mainloop()


def info1() :
    w = tk.Tk()
    w.title("序列編號加密原理")
    tk.Label(w, text = "序列編號加密法\n\n為每一個英文字母給予編號，代表在此位的K\n\n目前編碼規律：順序排列（1-26）loop\n\n解密速度：\n足夠數據量下尋找crib\n找到規律下O(n)\n否則無法破解NaN\n\n對單字頻率採樣免疫", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 2)
    w.mainloop()