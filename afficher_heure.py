import time
import tkinter
"""def onclick(event):
    global compteur,monLabelle
    compteur +=1
    monLabelle.config(text="compteur" + str(compteur))

mon_boutton = tkinter.Button(maf, text="clique ici !", width=50)
mon_boutton.pack()
mon_boutton.bind('<ButtonRelease-1>',onclick)"""

def regler_alarme(reveil):
    global heure_actuelle
    h1 = reveil[0]
    m1 = reveil[1]
    s1 = reveil[2]
    sonne =(h1,m1,s1)
    if heure_actuelle == sonne:
        print("alarme")
def afficher_heure(tupple):
    global heure_actuelle
    global reveil
    global mode
    time.sleep(1)
    h = tupple[0]
    m = tupple[1]
    s = tupple[2]
    s+=1
    0<h<24
    0<m<60
    0<s<60
    if s > 59 :
         m+=1
         s=0
    if m > 59 :
         h+=1
         m = 0
    heure_actuelle=(h,m,s)
    print(heure_actuelle)
    regler_alarme(reveil)
    afficher_heure(heure_actuelle)   
def afficher_heureanglais(tupple):
    global heure_actuelle
    global reveil
    global mode
    time.sleep(1)
    h = tupple[0]
    m = tupple[1]
    s = tupple[2]
    s+=1
    1<h<24
    0<m<60
    0<s<60
    if s > 59:
         m+=1
         s=0
    elif m > 59:
         h+=1
         m = 0
    elif 0<h<12:
        print(str(h) + "AM")
    elif 12<=h<24:
        print(str(h) +"PM")
    heure_actuelle=(h,m,s)
    print(heure_actuelle)
    regler_alarme(reveil)
    afficher_heureanglais(heure_actuelle)
def rentre_heure():
    global reveil
    global mode
    H = int(input("quelle est l'heure : "))
    M = int(input("nombre de minute : "))
    S = int(input("nombre de secondes : "))
    tuppled=(H,M,S)
    H1 = int(input("quelle est l'heure alarme : "))
    M1 = int(input("nombre de minute alarme : "))
    S1 = int(input("nombre de secondes alarme : "))
    reveil = (H1,M1,S1)
    mode = input("ton choix d'affichage : 1 pour AM/PM 2 pour normale :  ")
    if mode == "1":
        afficher_heureanglais(tuppled)
    elif mode == "2":
        afficher_heure(tuppled)
rentre_heure()
"""maf = tkinter.Tk()
monLabelle = tkinter.Label(maf,rentre_heure)
monLabelle.pack()
maf.mainloop()"""