import tkinter as tk
import ALG
import EncryptorUI
import DecryptorUI
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def showresult0(pw, location0):
    def SelectFileToSave():
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        with open(location, "w") as temp:
            ttt = FileShowingBox.get(1.0, tk.END)
            temp.write(ttt)

    def SaveF():
        with open(location0, "w", encoding="utf-8") as temp:
            ttt = FileShowingBox.get(1.0, tk.END)
            temp.write(ttt)

    def hits0():
        x = [str(i) for i in range(26)]
        t2 = pw.DictionaryMethodPossiblity
        h = [t2[((26 - pw.DictionaryMethodKValue) + i - pw.DictionaryMethodKValue) % 26] for i in range(26)]
        plt.bar(x, h)
        plt.show()

    w = tk.Tk()
    w.title("解密結果")

    # Using Text widget instead of Label
    FileShowingBox = tk.Text(w, width=40, height=8, bg="white", wrap=tk.WORD)
    # Adding Scrollbar
    scrollbar = tk.Scrollbar(w, command=FileShowingBox.yview)
    FileShowingBox.config(yscrollcommand=scrollbar.set)

    def show(*e):
        a = pw.Asciiw
        a = ALG.Return_AsciiNumberPuseK(a, 26 - int(value.get()))
        a = ALG.Return_AsciiToPrintableWord(a)
        FileShowingBox.delete(1.0, tk.END)
        FileShowingBox.insert(tk.END, a)

    KValueString = tk.Label(w, text="設置k值", width=25, height=2)
    optionList = list(range(26))
    value = tk.StringVar(w)
    value.set(pw.DictionaryMethodKValue)
    KValue = tk.OptionMenu(w, value, *optionList)
    KValue.config(width=8, height=2)
    value.trace('w', show) 

    FileShowingBox.insert(tk.END, pw.DictionaryMethodOriganArticle)
    
    tk.Button(w, text="k值準確度圖表", padx=10, pady=10, command=hits0).grid(row=4, column=1)
    tk.Label(w, text="k值解密結果 " + str(pw.DictionaryMethodKValue)).grid(row=4, column=0)
    tk.Button(w, text="將明文覆寫於原檔", padx=10, pady=10, command=SaveF).grid(row=5, column=0)
    tk.Button(w, text="選擇儲存於其他檔案", padx=10, pady=10, command=SelectFileToSave).grid(row=5, column=1)

    KValue.grid(row=1, column=1)
    KValueString.grid(row=1, column=0)
    tk.Label(w, text="解密結果預覽", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=0, column=0)
    
    # Adjusting grid layout to include scrollbar
    FileShowingBox.grid(row=3, column=0, columnspan=2)
    scrollbar.grid(row=3, column=2, sticky='ns')

    w.mainloop()

def showresult1(pw, location0):
    def SelectFileToSave():
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        with open(location, "w") as temp:
            ttt = FileShowingBox.get(1.0, tk.END)
            temp.write(ttt)

    def SaveF():
        with open(location0, "w", encoding="utf-8") as temp:
            ttt = FileShowingBox.get(1.0, tk.END)
            temp.write(ttt)

    def hits0():
        x = [chr(ord("A") + i) for i in range(26)]
        h = pw.wordFrequency
        plt.bar(x, h)
        plt.show()

    w = tk.Tk()
    w.title("解密結果")

    # Using Text widget instead of Label
    FileShowingBox = tk.Text(w, width=40, height=8, bg="white", wrap=tk.WORD)
    # Adding Scrollbar
    scrollbar = tk.Scrollbar(w, command=FileShowingBox.yview)
    FileShowingBox.config(yscrollcommand=scrollbar.set)

    def show(*e):
        a = pw.Asciiw
        a = ALG.Return_AsciiNumberPuseK(a, 26 - int(value.get()))
        a = ALG.Return_AsciiToPrintableWord(a)
        FileShowingBox.delete(1.0, tk.END)
        FileShowingBox.insert(tk.END, a)

    KValueString = tk.Label(w, text="設置k值", width=25, height=2)
    optionList = list(range(26))
    value = tk.StringVar(w)
    value.set(pw.WordFrewuencyMethodKValue)
    KValue = tk.OptionMenu(w, value, *optionList)
    KValue.config(width=8, height=2)
    value.trace('w', show) 

    FileShowingBox.insert(tk.END, pw.WordFrewuencyMethodOriganArticle)
    
    tk.Button(w, text="k值準確度圖表", padx=10, pady=10, command=hits0).grid(row=4, column=1)
    tk.Label(w, text="k值解密結果 " + str(pw.WordFrewuencyMethodKValue)).grid(row=4, column=0)
    tk.Button(w, text="將明文覆寫於原檔", padx=10, pady=10, command=SaveF).grid(row=5, column=0)
    tk.Button(w, text="選擇儲存於其他檔案", padx=10, pady=10, command=SelectFileToSave).grid(row=5, column=1)

    KValue.grid(row=1, column=1)
    KValueString.grid(row=1, column=0)
    tk.Label(w, text="解密結果預覽", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=0, column=0)
    
    # Adjusting grid layout to include scrollbar
    FileShowingBox.grid(row=3, column=0, columnspan=2)
    scrollbar.grid(row=3, column=2, sticky='ns')

def showresult2(pw, location0):
    def SelectFileToSave():
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        with open(location, "w") as temp:
            ttt = FileShowingBox.get(1.0, tk.END)
            temp.write(ttt)

    def SaveF():
        with open(location0, "w", encoding="utf-8") as temp:
            ttt = FileShowingBox.get(1.0, tk.END)
            temp.write(ttt)

    w = tk.Tk()
    w.title("解密結果")

    # Using Text widget instead of Label
    FileShowingBox = tk.Text(w, width=40, height=8, bg="white", wrap=tk.WORD)
    # Adding Scrollbar
    scrollbar = tk.Scrollbar(w, command=FileShowingBox.yview)
    FileShowingBox.config(yscrollcommand=scrollbar.set)

    FileShowingBox.insert(tk.END, pw.M2P)
    
    tk.Button(w, text="將明文覆寫於原檔", padx=10, pady=10, command=SaveF).grid(row=5, column=0)
    tk.Button(w, text="選擇儲存於其他檔案", padx=10, pady=10, command=SelectFileToSave).grid(row=5, column=1)
    
    tk.Label(w, text="解密結果預覽", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=0, column=0)
    
    # Adjusting grid layout to include scrollbar
    FileShowingBox.grid(row=3, column=0, columnspan=2)
    scrollbar.grid(row=3, column=2, sticky='ns')

    w.mainloop()

def showresult3(pw, location0):
    def SelectFileToSave():
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),))
        with open(location, "w") as temp:
            ttt = FileShowingBox.get(1.0, tk.END)
            temp.write(ttt)

    def SaveF():
        with open(location0, "w", encoding="utf-8") as temp:
            ttt = FileShowingBox.get(1.0, tk.END)
            temp.write(ttt)

    w = tk.Tk()
    w.title("解密結果")

    FileShowingBox = tk.Text(w, width=40, height=8, bg="white", wrap=tk.WORD)
    scrollbar = tk.Scrollbar(w, command=FileShowingBox.yview)
    FileShowingBox.config(yscrollcommand=scrollbar.set)

    FileShowingBox.insert(tk.END, pw.word2vscMethodOriganArticle)

    tk.Button(w, text="將明文覆寫於原檔", padx=10, pady=10, command=SaveF).grid(row=5, column=0)
    tk.Button(w, text="選擇儲存於其他檔案", padx=10, pady=10, command=SelectFileToSave).grid(row=5, column=1)

    tk.Label(w, text="解密結果預覽", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=0, column=0)

    FileShowingBox.grid(row=3, column=0, columnspan=2)
    scrollbar.grid(row=3, column=2, sticky='ns')

    w.mainloop()