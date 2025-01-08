import tkinter as tk
import ALG
import EncryptorUI
import DecryptorUI
from tkinter import filedialog
import displayOriganalTextUI
import chardet

def DQer0():
    temp = []
    location = ""
    
    def uploadFile():
        nonlocal temp, location
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        temp = []
        try:
            # Detect the file encoding
            with open(location, 'rb') as file:
                raw_data = file.read()
                result = chardet.detect(raw_data)
                encoding = result['encoding']
            
            # Read the file with the detected encoding
            with open(location, "r", encoding=encoding) as file:
                temp = file.readlines()
        except UnicodeDecodeError:
            with open(location, "r", encoding="latin-1") as file:
                temp = file.readlines()
        
        temp0 = [i.upper() for i in temp]
        temp = temp0
        ttt = "".join(temp)
        # Updating Text widget content
        FileShowingBox.delete(1.0, tk.END)
        FileShowingBox.insert(tk.END, ttt)

    def hits():
        nonlocal temp, location
        if location != "":
            a = ALG.pre_proess_word(temp)
            displayOriganalTextUI.showresult0(a, location)
        else:
            t0 = tk.Tk()
            t0.title("注意")
            tk.Label(t0, text="請上載密文檔案", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=1, column=0)
            t0.mainloop()

    w = tk.Tk()
    w.title("「位移加密法」字典法解密器")

    # Using Text widget instead of Label
    FileShowingBox = tk.Text(w, width=40, height=8, bg="white", wrap=tk.WORD)
    # Adding Scrollbar
    scrollbar = tk.Scrollbar(w, command=FileShowingBox.yview)
    FileShowingBox.config(yscrollcommand=scrollbar.set)

    bOfChooseFile = tk.Button(w, text="密文檔案上載", width=15, height=2, command=uploadFile)
    BOfProcess = tk.Button(w, text="解密", command=hits)

    tk.Label(w, text="密文預覽", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=1, column=0)
    # Adjusting grid layout to include scrollbar
    FileShowingBox.grid(row=2, column=0, columnspan=2)
    scrollbar.grid(row=2, column=2, sticky='ns')
    bOfChooseFile.grid(row=3, column=0, ipadx=3, ipady=3, padx=10, pady=20)
    BOfProcess.grid(row=3, column=1)

    w.mainloop()

def DQer1():
    temp = []
    location = ""
    
    def uploadFile():
        nonlocal temp, location
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        temp = []
        try:
            # Detect the file encoding
            with open(location, 'rb') as file:
                raw_data = file.read()
                result = chardet.detect(raw_data)
                encoding = result['encoding']
            
            # Read the file with the detected encoding
            with open(location, "r", encoding=encoding) as file:
                temp = file.readlines()
        except UnicodeDecodeError:
            with open(location, "r", encoding="latin-1") as file:
                temp = file.readlines()
        
        temp0 = [i.upper() for i in temp]
        temp = temp0
        ttt = "".join(temp)
        FileShowingBox.delete(1.0, tk.END)
        FileShowingBox.insert(tk.END, ttt)

    def hits():
        nonlocal temp, location
        if location != "":
            a = ALG.pre_proess_word(temp)
            displayOriganalTextUI.showresult1(a, location)
        else:
            t0 = tk.Tk()
            t0.title("注意")
            tk.Label(t0, text="請上載密文檔案", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=1, column=0)
            t0.mainloop()

    w = tk.Tk()
    w.title("「位移加密法」單字頻數法解密器")

    FileShowingBox = tk.Text(w, width=40, height=8, bg="white", wrap=tk.WORD)
    scrollbar = tk.Scrollbar(w, command=FileShowingBox.yview)
    FileShowingBox.config(yscrollcommand=scrollbar.set)

    bOfChooseFile = tk.Button(w, text="上載密文檔案", width=15, height=2, command=uploadFile)
    BOfProcess = tk.Button(w, text="解密", command=hits)

    tk.Label(w, text="密文預覽", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=1, column=0)
    FileShowingBox.grid(row=2, column=0, columnspan=2)
    scrollbar.grid(row=2, column=2, sticky='ns')
    bOfChooseFile.grid(row=3, column=0, ipadx=3, ipady=3, padx=10, pady=20)
    BOfProcess.grid(row=3, column=1)

    w.mainloop()

def DQer2():
    temp = []
    location = ""
    
    def uploadFile():
        nonlocal temp, location
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),)) 
        temp = []
        try:
            # Detect the file encoding
            with open(location, 'rb') as file:
                raw_data = file.read()
                result = chardet.detect(raw_data)
                encoding = result['encoding']
            
            # Read the file with the detected encoding
            with open(location, "r", encoding=encoding) as file:
                temp = file.readlines()
        except UnicodeDecodeError:
            with open(location, "r", encoding="latin-1") as file:
                temp = file.readlines()
        
        temp0 = [i.upper() for i in temp]
        temp = temp0
        ttt = "".join(temp)
        # Updating Text widget content
        FileShowingBox.delete(1.0, tk.END)
        FileShowingBox.insert(tk.END, ttt)

    def hits():
        nonlocal temp, location
        if location != "":
            a = ALG.pre_proess_word(temp)
            displayOriganalTextUI.showresult2(a, location)
        else:
            t0 = tk.Tk()
            t0.title("注意")
            tk.Label(t0, text="請上載密文檔案", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=1, column=0)
            t0.mainloop()

    w = tk.Tk()
    w.title("「位移加密法」序列編號法解密器")

    # Using Text widget instead of Label
    FileShowingBox = tk.Text(w, width=40, height=8, bg="white", wrap=tk.WORD)
    # Adding Scrollbar
    scrollbar = tk.Scrollbar(w, command=FileShowingBox.yview)
    FileShowingBox.config(yscrollcommand=scrollbar.set)

    bOfChooseFile = tk.Button(w, text="上載密文檔案", width=15, height=2, command=uploadFile)
    BOfProcess = tk.Button(w, text="解密", command=hits)

    tk.Label(w, text="密文預覽", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=1, column=0)
    # Adjusting grid layout to include scrollbar
    FileShowingBox.grid(row=2, column=0, columnspan=2)
    scrollbar.grid(row=2, column=2, sticky='ns')
    bOfChooseFile.grid(row=3, column=0, ipadx=3, ipady=3, padx=10, pady=20)
    BOfProcess.grid(row=3, column=1)

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

def info2() :
    w = tk.Tk()
    w.title("序列編號加密原理")
    tk.Label(w, text = "序列編號加密法\n\n為每一個英文字母給予編號，代表在此位的K\n\n目前編碼規律：順序排列（1-26）loop\n\n解密速度：\n足夠數據量下尋找crib\n找到規律下O(n)\n否則無法破解NaN\n\n對單字頻率採樣免疫", padx = 40, pady = 15, font = ('Times New Roman', 15, 'bold')).grid(row = 2)
    w.mainloop()


def info3():
    w = tk.Tk()
    w.title("word2vec")
    tk.Label(w, text="word2vec\n\n使用預訓練的word2vec模型\n\n解密速度：o(sixe(M)*N)\n取決於所選模型的大小\n\n對單字頻率採樣免疫", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=2)
    w.mainloop()


def DQer3():
    temp = []
    location = ""
    key_word = ""

    def SelectFileToSave():
        nonlocal temp, location
        location = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("text", "*.txt"),))
        if location:
            try:
                # Detect encoding of the content
                encoding = chardet.detect(FileShowingBox.get(1.0, tk.END).encode())['encoding'] or 'utf-8'
            except:
                encoding = 'utf-8'  # Default to utf-8 if detection fails

            with open(location, "w", encoding=encoding) as temp_file:
                ttt = FileShowingBox.get(1.0, tk.END)
                temp_file.write(ttt)

    def SaveF():
        nonlocal temp, location
        if location:
            try:
                # Use the same encoding as when the file was opened
                with open(location, 'rb') as f:
                    original_encoding = chardet.detect(f.read())['encoding']
            except:
                original_encoding = 'utf-8' # Default to utf-8 if detection fails
            
            with open(location, "w", encoding=original_encoding) as temp_file:
                ttt = FileShowingBox.get(1.0, tk.END)
                temp_file.write(ttt)
        else:
            tk.messagebox.showinfo("Info", "Original file not loaded or saved.")

    def uploadFile():
        nonlocal temp, location
        location = filedialog.askopenfilename(filetypes=(("text", "*.txt"),))
        temp = []
        try:
            with open(location, 'rb') as file:
                raw_data = file.read()
                result = chardet.detect(raw_data)
                encoding = result['encoding']

            with open(location, "r", encoding=encoding) as file:
                temp = file.readlines()
        except UnicodeDecodeError:
            with open(location, "r", encoding="latin-1") as file:
                temp = file.readlines()

        temp0 = [i.upper() for i in temp]
        temp = temp0
        ttt = "".join(temp)
        FileShowingBox.delete(1.0, tk.END)
        FileShowingBox.insert(tk.END, ttt)

    def hits():
      nonlocal temp, location, key_word
      key_word = KeyEntry.get().upper()
      if location != "" and key_word != "":
          if ALG.wv is not None:
              a = temp
              T = ''
              for i in a :
                  T += i
              a = T 
              print(a)
              a = a.split('\n')
              a = ALG.word2vsc_decrypt(a, key_word)
              FileShowingBox.delete(1.0, tk.END)
              FileShowingBox.insert(tk.END, a)
          else:
              error_message = "Word2Vec model not loaded. Cannot perform decryption."
              tk.messagebox.showerror("Error", error_message)
      else:
          t0 = tk.Tk()
          t0.title("注意")
          tk.Label(t0, text="請上載密文檔案", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=1, column=0)
          t0.mainloop()

    w = tk.Tk()
    w.title("「word2vec」解密器")

    FileShowingBox = tk.Text(w, width=40, height=8, bg="white", wrap=tk.WORD)
    scrollbar = tk.Scrollbar(w, command=FileShowingBox.yview)
    FileShowingBox.config(yscrollcommand=scrollbar.set)

    bOfChooseFile = tk.Button(w, text="上載密文檔案", width=15, height=2, command=uploadFile)
    BOfProcess = tk.Button(w, text="解密", command=hits)

    KeyLabel = tk.Label(w, text="Key:", width=5, height=2)
    KeyEntry = tk.Entry(w, width=20)  # Entry for key

    tk.Label(w, text="密文預覽", padx=40, pady=15, font=('Times New Roman', 15, 'bold')).grid(row=1, column=0)
    FileShowingBox.grid(row=2, column=0, columnspan=2)
    scrollbar.grid(row=2, column=2, sticky='ns')
    bOfChooseFile.grid(row=3, column=0, ipadx=3, ipady=3, padx=10, pady=20)
    BOfProcess.grid(row=3, column=1)
    KeyLabel.grid(row=4, column=0)
    KeyEntry.grid(row=4, column=1)
    
    tk.Button(w, text="將明文覆寫於原檔", padx=10, pady=10, command=SaveF).grid(row=5, column=0)
    tk.Button(w, text="選擇儲存於其他檔案", padx=10, pady=10, command=SelectFileToSave).grid(row=5, column=1)

    w.mainloop()