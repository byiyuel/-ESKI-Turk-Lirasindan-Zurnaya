#For personal use only!

#For cleaning console/Konsolu temizlemek için
import os
import time 
cls = lambda: os.system('cls')

#For input/Girdiyi almak için
print("Choose a language/Bir dil seç! (TR or ENG)")
lang = input().lower()

time.sleep(0.2)
cls()

#For Turkish/Türkçe için
if lang == "tr":
    print("Türk Lirasından Zurnaya Çevirme Aracı \n")
    tl = int(input("Türk Lirası giriniz: \n"))
    print("Sonuç:", 25 / tl)

#For English/İngilizce için
elif lang == "eng":
    print("Turkish Lira to Zurna \n")
    tl = int(input("Enter Turkish Lira: \n"))
    print("Result:", tl / 25)

#End of code