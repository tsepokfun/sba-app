import tkinter as tk
import ALG
import EncryptorUI
import DecryptorUI
from tkinter import filedialog

#ditionary create
temp = open("data/wiki-100k.txt")
t = temp.readlines()
rank = 0
dictionary = {}
for i in t :
    dictionary[i.rstrip().upper()] = rank
    rank += 1
    
##print("words in dictionary = "+str(len(dictionary)))
#ditionary created
#lot of same word
#no hash collision
"""
for i in t :
    if i[:len(i) - 2].upper() in dictionary :
        print(rank, dictionary.get(i[:len(i) - 2].upper()))
"""
#this can use to check

def Return_WordToAscii (pw) : #return word to ascii id

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

def Return_wordFrequency (pw) : #return words fequancy (ascii number only)
    words = [0] * 26
    for i in pw :
        for j in i :
            if type(j) == int :
                words[j - ord("A")] += 1
    return words

def Return_AsciiNumberPuseK (nul, k) : #return number +(pus) k 
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

def Return_AsciiToPrintableWord (nul) : #return ascii id to word
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

def Return_SeperateVocabToWord (nul) : #[[65, 65], " "] ->[65, 65, ""]
    t = []
    for i in nul :
        if type(i) == list :
            for j in i :
                t.append(j)
        else :
            t.append(i)
    return t

def Return_CombinWordToVocab (nul) : #[65, 65, " "] ->[[65, 65], ""]
    t = []
    for i in nul :
        tt = []
        t0 = []
        for j in i :
            if type(j) == int :
                t0.append(j)
            elif t0 != [] :
                tt.append(t0)
                t0 = []
                tt.append(j)
            else :
                tt.append(j)
        if t0 != [] :
            tt.append(t0)
        t.append(tt)
    return t

def Return_OriganalArticleDictionaryMethod (nul) : # as the name :) #in w type #not null
    pboK = []
    for i in range(26) :
        vid = 0
        v = 0
        cpl = Return_AsciiNumberPuseK(nul, i)
        cpl = Return_CombinWordToVocab(cpl)
        for i in cpl :
            for j in i : 
                if type(j) == list :
                    v += 1
                    t = ""
                    for k in j :
                        t += chr(k)
                    if t in dictionary :
                        vid += 1 
        if v != 0 : 
            pboK.append(vid/v)
        else :
            pboK.append(0)
    k = pboK.index(max(pboK))
    return [Return_AsciiToPrintableWord(Return_AsciiNumberPuseK(nul, k)), k, pboK]

def Return_KWordFrewuencyMethod (nul) : # as the name :) #in w type #not null
    cpl = Return_wordFrequency(nul)
    k = cpl.index(max(cpl)) - 4
    if k - 4 > 0 :
        return k
    else :
        return 26 + k

def Return_M2O (nul) :
    count = 0
    print(nul)
    t = []
    for i in nul :
        tt = []
        for j in i :
            if type(j) == int :
                tt.append(ord("A") + (j - ord("A") + count)%26)
            else :
                tt.append(j)
            count += 1
        t.append(tt)
    print(t)
    return t

def Return_M2P (nul) :
    count = 0
    print(nul)
    t = []
    for i in nul :
        tt = []
        for j in i :
            if type(j) == int :
                tt.append(ord("A") + (j - ord("A") + count)%26)
            else :
                tt.append(j)
            count -= 1
        t.append(tt)
    print(t)
    return t

class pre_proess_word :
    def __init__(self, w) :
        #text proess
        self.w = w
        self.Asciiw = Return_WordToAscii(self.w)
        self.Vocabw = Return_CombinWordToVocab(self.Asciiw)
        #print(self.Asciiw)
        #Method00 dictionary
        t = Return_OriganalArticleDictionaryMethod(self.Asciiw) 
        self.DictionaryMethodOriganArticle = t[0]
        self.DictionaryMethodKValue = (26 - t[1]) % 26
        self.DictionaryMethodPossiblity = t[2]
        #print(self.DictionaryMethodOriganArticle)
        #Method01 fequency
        self.wordFrequency = Return_wordFrequency(self.Asciiw)
        self.WordFrewuencyMethodKValue = Return_KWordFrewuencyMethod(self.Asciiw)
        self.WordFrewuencyMethodOriganArticle = Return_AsciiToPrintableWord(Return_AsciiNumberPuseK(self.Asciiw, self.WordFrewuencyMethodKValue))
        #print(self.WordFrewuencyMethodOriganArticle)
        #Method0 sequence
        self.M2O = Return_AsciiToPrintableWord(Return_M2O(self.Asciiw))
        self.M2P = Return_AsciiToPrintableWord(Return_M2P(self.Asciiw))
        print(self.M2O, self.M2P)
        

        

a = pre_proess_word(["TRY THIS", "HI"])
#print(a.DictionaryMethodPossiblity)

"""
Sources:
http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists#Top_English_words_lists
"""
