import tkinter as tk
import ALG
import EncryptorUI
import DecryptorUI
from tkinter import filedialog
import displayOriganalTextUI


def DQer0() :
    temp = 0
    location = ""
    def uploadFile() :
        global temp
        global location
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
        global location
        if location != "" :
            a = ALG.pre_proess_word(temp)
            displayOriganalTextUI.showresult0(a, location)
        else :
            t0 = tk.Tk()
            t0.title("注意")
            tk.Label(t0, text = "請上載密文檔案", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 1, column = 0)
            t0.mainloop()



    w = tk.Tk()
    w.title("「位移加密法」字典法解密器")

    FileShowingBox = tk.StringVar(w)



    bOfChooseFile = tk.Button(w, text = "密文檔案上載" , width = 15, height  = 2, command = uploadFile)

    content = tk.Label(w, textvariable = FileShowingBox, width = 40, height = 8, bg = "white", justify = "left")

    BOfProcess = tk.Button(w, text = "解密", command = hits)
    tk.Label(w, text = "密文預覽", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 1, column = 0)
    BOfProcess.grid(row = 3, column = 1)
    content.grid(row = 2, column = 0)
    bOfChooseFile.grid(row = 3 , column = 0, ipadx = '3', ipady = '3', padx = '10', pady = '20')

    w.mainloop()

def DQer1() :
    temp = 0
    location = ""
    def uploadFile () :
        global temp
        global location
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
        global location
        if location != "" :
            a = ALG.pre_proess_word(temp)
            displayOriganalTextUI.showresult1(a, location)
        else :
            t0 = tk.Tk()
            t0.title("注意")
            tk.Label(t0, text = "請上載密文檔案", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 1, column = 0)
            t0.mainloop()

    w = tk.Tk()
    w.title("「位移加密法」單字頻數法解密器")

    FileShowingBox = tk.StringVar(w)



    bOfChooseFile = tk.Button(w, text = "上載密文檔案" , width = 15, height  = 2, command = uploadFile)

    content = tk.Label(w, textvariable = FileShowingBox, width = 40, height = 8, bg = "white", justify = "left")

    BOfProcess = tk.Button(w, text = "解密", command = hits)
    tk.Label(w, text = "密文預覽", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 1, column = 0)
    BOfProcess.grid(row = 3, column = 1)
    content.grid(row = 2, column = 0)
    bOfChooseFile.grid(row = 3 , column = 0, ipadx = '3', ipady = '3', padx = '10', pady = '20')

    w.mainloop()


def info0() :
    w = tk.Tk()
    w.title("字典方法解密器原理")
    tk.Label(w, text = "透過匹配己有生字，得出位移值\n字典來源：維基百科，單字使用頻調查\n哈希表儲存，解密速度：O(n)\n\n*數據量足夠時，可透過區間採樣法，下降解密速度至：O(n/k)（k = 區間採樣率)", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 2)
    w.mainloop()

def info1() :
    w = tk.Tk()
    w.title("單字頻數解密器原理")
    tk.Label(w, text = "透過統計單字頻數，得出位移值\n解密速度：O(n)\n\n*數據量足夠時，可透過區間採樣法，下降解密速度至：O(n/k)（k = 區間採樣率）", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 2)
    
    w.mainloop()