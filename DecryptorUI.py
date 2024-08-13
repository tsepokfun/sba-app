import tkinter as tk
import ALG
from tkinter import filedialog



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
    a = ALG.pre_proess_word(temp)
    print(a)
    ttt = ""
    for i in a.DictionaryMethodOriganArticle :
        ttt += i
    FileShowingBox.set(ttt)

w = tk.Tk()
w.title("「位移加密法」解密器")

FileShowingBox = tk.StringVar()



bOfChooseFile = tk.Button(w, text = "上載密文檔案" , width = 15, height  = 2, command = uploadFile)

content = tk.Label(w, textvariable = FileShowingBox, width = 40, height = 8, bg = "white", justify = "left")

BOfProcess = tk.Button(w, text = "解密", command = hits)

BOfProcess.grid(row = 3, column = 1)
content.grid(row = 2, column = 0)
bOfChooseFile.grid(row = 3 , column = 0, ipadx = '3', ipady = '3', padx = '10', pady = '20')

w.mainloop()


