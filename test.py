


import ALG


temp = ["COMPUTER SCIENCE AND DATA SICENCE", "SCHOOL OF CS"]
key_word = "TRY"
a = temp
a = ALG.Return_WordToAscii(a)
a = ALG.Return_CombinWordToVocab(a)[0]
a = ALG.Return_AsciiToPrintableWord(a)
a = ALG.word2vsc_encrypt(a, key_word)

print(a)
a = a.split('\n')
a = ALG.word2vsc_decrypt(a, key_word)
print(a)
