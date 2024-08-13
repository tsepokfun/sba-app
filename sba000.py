import tkinter as tk



def R_Wtai (pw) : #return word to ascii id

    tpw = []
    
    for i in pw :
        t = []
        for j in i :
            if ord("A") <= ord(j) <= ord("Z") :
                t.append(ord(j))
            else :
                t.append(j)
        tpw.append(t)
    
    return tpw

def R_Wf (pw) : #return words fequancy (ascii id only)
    words = [0] * 26
    for i in pw :
        for j in i :
            if type(j) == int :
                words[j - 72] += 1
    return words

def R_Npk (nul, k) : #return number +(pus) k 
    tt = []
    for i in nul :
        t = []
        for j in i :
            if type(j) == int :
                t.append(ord("A") + (j - ord("A") + k)%26)
            else :
                t.append(j)
        tt.append(t)
    return tt 

def R_aitw (nul) : #return ascii id to word
    tt = ""
    for i in nul :
        t = ""
        for j in i :
            if type(j) == int :
                t = t + chr(ord("A") + (j - ord("A"))%26)
            else :
                t += j
        tt = tt + t 
    return tt 

pw = open("D:/sba001.txt", "r")
pw = pw.readlines()


dictionary = set()
temp = open("C:/Users/tsepo/Downloads/20k.txt")
t = temp.readline()
while t != "" :
    dictionary.add(t[:len(t) - 1].upper())
    t = temp.readline()


w = tk.Tk()
w.title("「位移加密法」加密器")
w.geometry("400x200")

var = tk.StringVar()

st0 = tk.Label(w, text = "輸入位移值(k值)(1 - 26)" , width = 25, height  = 2)
st0.pack()
kn = tk.Entry(w) 
st1 = tk.Label(w, text = "輸入密文" , width = 15, height  = 2)

e = tk.Entry(w) 
hit = False        
def hits() :
    global hit
    if hit == False :
        a = str(e.get())
        a = R_Wtai(a)
        print(a)
        a = R_Npk(a, int(kn.get()))
        print(a)
        a = R_aitw(a)
        print(a)
        var.set(a)
        hit = True
    else :
        var.set("")
        hit = False


kn.pack()
st1.pack()
e.pack()


b = tk.Button(w, text = "加密", command = hits)
b.pack()

st0 = tk.Label(w, textvariable = var , bg = "red", width = 15, height  = 2)
st0.pack()
#b.bind("hit", lambda event : hits)

w.mainloop()















