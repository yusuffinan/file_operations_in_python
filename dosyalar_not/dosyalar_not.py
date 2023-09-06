kalanlar = []
gecenler = []
def notlar(s):
    
    s = s[:-1]
    liste = s.split(",")
    isim = (liste[0])
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    sonuc = not1 * (0.30) + not2 * (0.30) + not3 * (0.40)
    if sonuc >= 90:
        harf = "aa"
        gecenler.append(isim + harf + str(sonuc) + "\n")
    elif sonuc >= 80:
        harf = "ba"
        gecenler.append(isim + harf + str(sonuc) + "\n")
    elif sonuc >= 65:
        harf = "cb"
        gecenler.append(isim + harf + str(sonuc) + "\n")
    else:
        harf ="FF"
        
        kalanlar.append(isim + harf + str(sonuc) + "\n")
    return isim +  "-----------" + harf + "\n"  

with open("dosya.txt","r", encoding="utf-8") as file:
    ekle =[]
    for i in file:
        ekle.append(notlar(i)) 
    with open("metin.txt", "w", encoding="utf-8") as c:
        c.writelines(ekle)
with open("kalanlar.txt","w", encoding="utf-8") as file2:
    file2.writelines(kalanlar)
with open("gecenler.txt","w", encoding="utf-8") as file3:
    file3.writelines(gecenler)