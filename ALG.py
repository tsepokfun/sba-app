
#ditionary create
temp = open("wiki-100k.txt")
t = temp.readline()
rank = 0
dictionary = {t[:len(t) - 1].upper(): rank}
a = len(t[:len(t) - 1])
while t != "" :
    dictionary[t[:len(t) - 1].upper()] = rank
    t = temp.readline()
    rank += 1
    if a < len(t[:len(t) - 1]) :
        a = len(t[:len(t) - 1])
        b = t
print(a, b)
#ditionary created

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
        pboK.append(vid/v)
    k = pboK.index(max(pboK))
    return Return_AsciiToPrintableWord(Return_AsciiNumberPuseK(nul, k)), k, pboK

def Return_KWordFrewuencyMethod (nul) : # as the name :) #in w type #not null
    cpl = Return_wordFrequency(nul)
    k = cpl.index(max(cpl)) - 4
    if k - 4 > 0 :
        return k
    else :
        return 26 + k



class pre_proess_word :
    def __init__(self, w) :
        self.w = w
        self.Asciiw = Return_WordToAscii(self.w)
        self.Vocabw = Return_CombinWordToVocab(self.Asciiw)
        self.wordFrequency = Return_wordFrequency(self.Asciiw)
        print(self.Asciiw)
        t = Return_OriganalArticleDictionaryMethod(self.Asciiw) 
        self.DictionaryMethodOriganArticle = t[0]
        self.DictionaryMethodKValue = 26 - t[1]
        self.DictionaryMethodPossiblity = t[2]
        self.WordFrewuencyMethodKValue = Return_KWordFrewuencyMethod(self.Asciiw)
        self.WordFrewuencyMethodOriganArticle = Return_AsciiToPrintableWord(Return_AsciiNumberPuseK(self.Asciiw, self.WordFrewuencyMethodKValue))

a = pre_proess_word(["JGNNQ YQTNF"])
print(a.DictionaryMethodOriganArticle)

"""
#!comment: This is a list of the top 100,000 most frequently-used English words
#!comment: according to Wiktionary.
#!comment:
#!comment: It was compiled in August 2005 and coalesced into a handy list for
#!comment: use in John the Ripper.
#!comment:
#!comment:
#!comment: Pull date: Sun Jan 15 22:03:54 2012 GMT
#!comment:
#!comment: Sources:
#!comment:
#!comment: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists#Top_English_words_lists
#!comment: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2005/08/1-10000
#!comment: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2005/08/10001-20000
#!comment: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2005/08/20001-30000
#!comment: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2005/08/30001-40000
#!comment: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2005/08/40001-50000
#!comment: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2005/08/50001-60000
#!comment: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2005/08/60001-70000
#!comment: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2005/08/70001-80000
#!comment: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2005/08/80001-90000
#!comment: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2005/08/90001-100000
#!comment:
#!comment: Compiled by h3xx
#!comment:
#!comment: 1 - 100
"""