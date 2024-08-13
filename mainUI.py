import tkinter as tk
import ALG
from tkinter import filedialog


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("「位移加密法」加解密器")
        self.geometry("450x300")
        self.current_frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        temp = 0
        def uploadFile () :
            global temp
            location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
            temp = 0
            temp = open(str(location), "r", encoding="utf-8")
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

        FileShowingBox = tk.StringVar()

        KValueString = tk.Label(self, text = "k值" , width = 25, height  = 2)
        optionList = []
        value = tk.StringVar()
        value.set(0)
        for i in range(27) :
            optionList.append(i)
        KValue = tk.OptionMenu(self, value, *optionList) 


        bOfChooseFile = tk.Button(self, text = "上載密文檔案" , width = 15, height  = 2, command = uploadFile)

        content = tk.Label(self, textvariable = FileShowingBox, width = 40, height = 8, bg = "white", justify = "left")

        BOfProcess = tk.Button(self, text = "加密", command = hits)

        KValue.grid(row = 1, column = 1)
        KValueString.grid(row = 1, column = 0)
        BOfProcess.grid(row = 3, column = 1)
        content.grid(row = 2, column = 0)
        bOfChooseFile.grid(row = 3 , column = 0, ipadx = 3, ipady = 3, padx = 10, pady = 20)

        tk.Button(self, text = "解密器", command=lambda: master.switch_frame(PageOne)).grid(row = 0, column = 0)
        tk.Label(self, text = "加密器").grid(row = 0, column = 1)

class PageOne(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
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

        FileShowingBox = tk.StringVar()
        bOfChooseFile = tk.Button(self, text = "上載密文檔案" , width = 15, height  = 2, command = uploadFile)

        content = tk.Label(self, textvariable = FileShowingBox, width = 40, height = 8, bg = "white", justify = "left")

        BOfProcess = tk.Button(self, text = "解密", command = hits)

        BOfProcess.grid(row = 3, column = 1)
        content.grid(row = 2, column = 0)
        bOfChooseFile.grid(row = 3 , column = 0, ipadx = '3', ipady = '3', padx = '10', pady = '20')
        tk.Label(self, text="加密器").grid(row = 0, column = 0)
        tk.Button(self, text="解密器", command=lambda: master.switch_frame(StartPage)).grid(row = 0, column = 1)

if __name__ == "__main__":
    app = App()
    app.mainloop()