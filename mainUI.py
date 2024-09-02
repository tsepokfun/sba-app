import tkinter as tk
import ALG
import EncryptorUI
import DecryptorUI
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
        def hits0() :
            DecryptorUI.DQer0()
        def hits1() :
            DecryptorUI.info0()
        def hits2() :
            DecryptorUI.DQer1()
        def hits3() :
            DecryptorUI.info1()
        tk.Label(self, text = "解密器", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 0, column = 1)
        tk.Button(self, text = "加密器", padx = 40, pady = 15, command = lambda: master.switch_frame(PageOne)).grid(row = 0, column = 0)
        tk.Button(self, text = "字典法解密", padx = 30, pady = 10, command = hits0).grid(row = 2, column = 1)
        tk.Button(self, text = "原理->", padx = 10, pady = 10, command = hits1).grid(row = 2, column = 0)
        tk.Button(self, text = "單字頻數法解密", padx = 15, pady = 10, command = hits2).grid(row = 3, column = 1)
        tk.Button(self, text = "原理->", padx = 10, pady = 10, command = hits3).grid(row = 3, column = 0)

        tk.Label(self, text = " ", padx = 40, pady = 15).grid(row = 1)



class PageOne(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        def hits0() :
            EncryptorUI.EQer0()
        def hits1() :
            EncryptorUI.info0()
        tk.Label(self, text = "加密器", padx = 40, pady = 15,  font = ('Times New Roman', 15, 'bold')).grid(row = 0, column = 0)
        tk.Button(self, text  = "解密器", padx = 40, pady = 15, command = lambda: master.switch_frame(StartPage)).grid(row = 0, column = 1)
        tk.Label(self, text = " ", padx = 40, pady = 15).grid(row = 1)
        tk.Button(self, text = "位移方法加密", padx = 30, pady = 10, command = hits0).grid(row = 2, column = 0)
        tk.Button(self, text = "<-原理", padx = 10, pady = 10, command = hits1).grid(row = 2, column = 1)
if __name__ == "__main__":
    app = App()
    app.mainloop()