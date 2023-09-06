bjk = []
fb = []
gs = []
with open("football.txt","r", encoding="utf-8")as file:
    liste = file.readlines()
    print(liste)
    for a in liste:
        a = a.split(",")
        club = a[:-1]
        print(club)
        if club[1] == "fenerbahçe":
            fb.append(club[0]+"\n")
        elif club[1] == "galatasaray":
            gs.append(club[0]+"\n")
        elif club[1] == "beşiktaş":
            bjk.append(club[0]+"\n")

with open("beşiktas.txt","w",encoding="utf-8") as b:
    b.writelines(bjk)
with open("fenerbahce.txt","w",encoding="utf-8")as f:
    f.writelines(fb)
with open("galatasaray.txt","w",encoding="utf-8")as g:
    g.writelines(gs)
        