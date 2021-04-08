#-*- coding: utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk
import time
import codecs

def akcja1():
    global opis1, przycisk1
    opis1=Label(glowneOkno, text="Witaj w pierwszej części badania ChessSL. Aby przejść do dalszych instrukcji kliknij Dalej.",font=("Times New Roman",20,),)
    opis1.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk1= Button( glowneOkno, text = "Dalej",font=("Times New Roman",16,"bold"),background="white",command=akcja2)
    przycisk1.place(x=630, y=650)

def akcja2():
    global opis1, przycisk1
    opis1.destroy()
    przycisk1.destroy()
    opis1=Label(glowneOkno,text = u"Ten etap potrwa ok 60 minut. Będzie się składał z trzech zadań.",font=("Times New Roman",20,))
    opis1.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk1 = Button( glowneOkno, text ="Dalej ",font=("Times New Roman",16,"bold"),background="white", command=akcja3 )
    przycisk1.place(x=630, y=650)


def akcja3():
    global opis1, przycisk1
    opis1.destroy()
    przycisk1.destroy()
    opis1=Label(glowneOkno,text = u"Każde z nich to inna pozycja szachowa. Rozwinęły się one naturalnie w grze turniejowej.\nNie są to kombinacje typu: wygrana w n posunięciach.",font=("Times New Roman",20,))
    opis1.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk1 = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja4 )
    przycisk1.place(x=630, y=650)

def akcja4():
    global opis1, przycisk1
    opis1.destroy()
    przycisk1.destroy()
    opis1=Label(glowneOkno,text = u"Twoje zadanie będzie polegało na przeprowadzeniu analizy każdej z tych pozycji.",font=("Times New Roman",20,))
    opis1.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk1 = Button(glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja5 )
    przycisk1.place(x=630, y=650)

def akcja5():
    global opis1, przycisk1
    opis1.destroy()
    przycisk1.destroy()
    opis1=Label(glowneOkno,text = u"Czas przeznaczony na jedną pozycję to 15 min. Zegar wyświetli się w prawym \n górnym rogu w chwili rozpoczęcia zadania.",font=("Times New Roman",20,))
    opis1.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk1 = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja6 )
    przycisk1.place(x=630, y=650)

def akcja6():
    global opis1, przycisk1
    opis1.destroy()
    przycisk1.destroy()
    opis1=Label(glowneOkno,text = u"Nie możesz skrócić czasu przeznaczonego na analizę. Poświęć każdej pozycji 15 minut.",font=("Times New Roman",20,))
    opis1.place(relx=0.5, rely=0.5, anchor=CENTER)

    przycisk1 = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja7 )
    przycisk1.place(x=630, y=650)
	
def akcja7():
    global opis1, przycisk1
    opis1.destroy()
    przycisk1.destroy()
    opis1=Label(glowneOkno,text = u"Możesz korzystać z realnej szachownicy, znajdującej się po Twojej prawej stronie.",font=("Times New Roman",20,))
    opis1.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk1 = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja8 )
    przycisk1.place(x=630, y=650)

def akcja8():
    global opis1, przycisk1
    opis1.destroy()
    przycisk1.destroy()
    plotno1.create_image(451,613 ,image = obraz4Tk)
    plotno1.place(x=665,y=-225)
    opis1=Label(glowneOkno,text =u"Po upływie czasu przeznaczonego na analizę,\nwyświetli się takie okno dialogowe z pytaniami. ",font=("Times New Roman",20,))
    opis1.place(x=250,y=340)
    przycisk1 = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja9 )
    przycisk1.place(x=630, y=650)
	
def akcja9():
    global opis1, przycisk1
    opis1.destroy()
    przycisk1.destroy()
    opis1=Label(glowneOkno,text = u"Zapoznaj się teraz z każdym pytaniem.\nUpewnij się, że wszystkie polecenia są dla Ciebie jasne.\n Wątpliwości zgłoś prowadzącemu. ",font=("Times New Roman",20,))
    opis1.place(x=240, y=340)
    przycisk1 = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja10 )
    przycisk1.place(x=630, y=650)

def akcja10():
    global opis1, przycisk1
    opis1.destroy()
    plotno1.destroy()
    przycisk1.destroy()
    opis1=Label(glowneOkno,text = u"Czas na wpisanie odpowiedzi wynosi 7 min. \nPo jego upływie automatycznie rozpocznie się kolejne zadanie. ",font=("Times New Roman",20,))
    opis1.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk1 = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja11 )
    przycisk1.place(x=630, y=650)

def akcja11():
    global opis1, przycisk1
    opis1.destroy()
    przycisk1.destroy()
    opis1=Label(glowneOkno,text = u"Jeżeli skończysz zapisz analizy wcześniej, możesz samodzielnie przejść \ndo następnej pozycji klikając ZAPISZ. ",font=("Times New Roman",20,))
    opis1.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk1 = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja12 )
    przycisk1.place(x=630, y=650)

def akcja12():
    global opis1, przycisk1
    opis1.destroy()
    przycisk1.destroy()
    opis1=Label(glowneOkno,text = u"Jeżeli masz jakieś pytania, zadaj je w tym momencie prowadzącemu badanie. ",font=("Times New Roman",20,))
    opis1.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk1 = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja13 )
    przycisk1.place(x=630, y=650)

def akcja13():
    global opis1, przycisk1
    opis1.destroy()
    przycisk1.destroy()
    opis1=Label(glowneOkno,text = u"Jeżeli wszystkie instrukcje są dla Ciebie jasne i nie masz żadnych pytań, rozpocznij badanie klikając zielony przycisk. \nPowodzenia!",font=("Times New Roman",20,))
    opis1.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk1 = Button( glowneOkno, text ="Rozpocznij",font=("Times New Roman",16,"bold"),background="green", command=zadanie1 )
    przycisk1.place(x=630, y=650)

def zadanie1():
    global opis1, przycisk1, czasStart, zegar15, opis2, licznik
    opis1.destroy()
    przycisk1.destroy()
    licznik += 1 
    czasStart=time.time()
    UpdateZegar15()
    opis2=Label(glowneOkno, text =u"Pozycja numer 1. Białe na posunięciu.",font=("Times New Roman",16))
    opis2.place(x=20,y=10)
    plotno.create_image(430,430 ,image = obrazTk)

def zadanie2():
    global opis2, czasStart, zegar15,licznik, czasStop15
    czasStop15= False
    licznik +=1
    czasStart=time.time()
    UpdateZegar15()
    opis2=Label(glowneOkno, text = u"Pozycja numer 2. Białe na posunięciu.", font= ("Times New Roman", 16))
    opis2.place(x=20,y=10)
    UpdateZegar15()
    plotno.create_image(430,430, image=obraz2Tk)

def zadanie3():
    global opis2, czasStart, zegar15, licznik, czasStop15
    czasStop15=False
    licznik +=1
    czasStart=time.time()
    UpdateZegar15()
    opis2=Label(glowneOkno, text =u"Pozycja numer 3. Białe na posunięciu.", font=("Times New Roman", 16))
    opis2.place(x=20,y=10)
    UpdateZegar15()
    plotno.create_image(430,430, image=obraz3Tk)
	

def UpdateZegar15():
    global zegar15,czasStart, czasStop15
    czasSekunda= 900- round(time.time() - czasStart,0)
    if czasStop15==False:
        if czasSekunda >= 900:
            min=15
            sec= int(czasSekunda - 900)
            if sec<10:
                sec='0' + str(sec)
            CzasWyswietlany=str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)
        elif czasSekunda >= 840:
            min=14
            sec= int(czasSekunda - 840)
            if sec<10:
                sec='0' + str(sec)
            CzasWyswietlany=str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)
        elif czasSekunda >= 780:
            min=13
            sec= int(czasSekunda - 780)
            if sec<10:
                sec='0' + str(sec)
            CzasWyswietlany=str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)		
        elif czasSekunda >= 720:
            min=12
            sec= int(czasSekunda - 720)
            if sec<10:
                sec='0' + str(sec)
            CzasWyswietlany=str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)
        elif czasSekunda >= 660:
            min=11
            sec= int(czasSekunda - 660)
            if sec<10:
                sec='0' + str(sec)
            CzasWyswietlany=str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)
        elif czasSekunda >= 600:
            min=10
            sec= int(czasSekunda - 600)
            if sec<10:
                sec='0' + str(sec)
            CzasWyswietlany=str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)
        elif czasSekunda>= 540:
            min=9
            sec=int(czasSekunda-540)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)
        elif czasSekunda>= 480:
            min=8
            sec=int(czasSekunda-480)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)	
        elif czasSekunda>= 420:
            min=7
            sec=int(czasSekunda-420)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)
        elif czasSekunda>= 360:
            min=6
            sec=int(czasSekunda-360)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)		
        elif czasSekunda>= 300:
            min=5
            sec=int(czasSekunda-300)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15) 
        elif czasSekunda>= 240:
            min=4
            sec=int(czasSekunda-240)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)
        elif czasSekunda>= 180:
            min=3
            sec=int(czasSekunda-180)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)
        elif czasSekunda>= 120:
            min=2
            sec=int(czasSekunda-120)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)
        elif czasSekunda>= 60:
            min=1
            sec=int(czasSekunda-60)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno)
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)
        elif czasSekunda>0:
            min=0
            sec=int(czasSekunda)
            if sec<10:
                sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar15.destroy()
            zegar15=Label(glowneOkno, fg='red')
            zegar15.place(x=1200,y=10)
            zegar15.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateZegar15)
        else:
            pass
            zegar15.destroy()
            Pytania()
			



def Pytania():
    global poleTekstowe1, poleTekstowe2, poleTekstowe3, opis1, przycisk1,przycisk2, opis2, przycisk2, zegar7, opisPolaTekstowego1, opisPolaTekstowego2, opisPolaTekstowego3, opisR, R1,R2,R3,R4, czasStart, czasStop7,czasStop15
    czasStop15=True
    czasStop7=False
    czasStart=time.time()
    opis1.destroy()
    opis2.destroy()
    przycisk1.destroy()
    def zap():
        selection = "Ocna pozycji: " + str(var.get())
        ocenar = codecs.open("ocenar.txt","a")
        ocenar.write(selection + "  ")
        ocenar.close()

    var = IntVar()
    opisR=Label(glowneOkno, text=u"\nJak oceniasz pozycję?",font=("Times New Roman",13))
    opisR.place(x=37,y=0)
    R1 = Radiobutton(glowneOkno, text=u"lepsza białych", variable=var, value=1,
                  command=zap)
    R1.place(x=37,y=55)

    R2 = Radiobutton(glowneOkno, text=u"lepsza czarnych", variable=var, value=2,
                  command=zap)
    R2.place(x=167,y=55)

    R3 = Radiobutton(glowneOkno, text=u"równa", variable=var, value=3,
                  command=zap)
    R3.place(x=317, y=55)

    R4 = Radiobutton(glowneOkno, text=u"niejasna", variable=var, value=4,
                  command=zap)
    R4.place(x=427, y=55)

    opisPolaTekstowego1 = Label(glowneOkno, text =u"\nWymień wszystkie istotne elementy pozycji:",font=("Times New Roman",13))
    opisPolaTekstowego1.place(x=37,y=80)
    poleTekstowe1 = Text(glowneOkno, width=60, height=10)
    poleTekstowe1.place(x=37,y=125)
    opisPolaTekstowego2 = Label(glowneOkno, text =u"Wymień wszystkie posunięcia, które razważałeś jako potencjalne:",font=("Times New Roman",13))
    opisPolaTekstowego2.place(x=37, y=300)
    poleTekstowe2 = Text(glowneOkno, width=60, height=8)
    poleTekstowe2.place(x=37,y=325)
    opisPolaTekstowego3 = Label(glowneOkno, text =u"Jaki ruch uważasz za najlepszy?\nZapisz go razem z wariantem i planem gry:", justify=(LEFT),font=("Times New Roman",13))
    opisPolaTekstowego3.place(x=37,y=470 )
    poleTekstowe3 = Text(glowneOkno, width=60, height=8)
    poleTekstowe3.place(x=37,y=515)
    przycisk2 = Button(glowneOkno, text ="ZAPISZ",font=("Times New Roman",16,"bold"),background="white", command = ZapiszOdp)
    przycisk2.place(x=235,y=675)
    updateZegar7()
	
def ZapiszOdp():
    global poleTekstowe1, poleTekstowe2, poleTekstowe3, zegar7, opis1, opis2, opis3, przycisk2, opisPolaTekstowego1, opisPolaTekstowego2, opisPolaTekstowego3, opisR, R1, R2, R3, R4, czasStop7
	
    czasStop7=True
    zawartoscPola1= poleTekstowe1.get('1.0',"end-1c")
    zawartoscPola2= poleTekstowe2.get('1.0','end-1c')
    zawartoscPola3= poleTekstowe3.get('1.0','end-1c')
    plik_tekstowy = codecs.open("Odpowiedzi.txt", "a", "utf-8") # Zapisz odpowiedzi
    plik_tekstowy.write("Elementy: " + zawartoscPola1)
    plik_tekstowy.write(" Kandydaty: " + zawartoscPola2)
    plik_tekstowy.write(" Wariant: " + zawartoscPola3 + " ###next### ")
    plik_tekstowy.close()
    
    ocenar = codecs.open("ocenar.txt","a")
    ocenar.write(" ###next### ")
    ocenar.close()
    
    R1.destroy()
    R2.destroy()
    R3.destroy()
    R4.destroy()
    opisR.destroy()	
    poleTekstowe1.destroy()
    poleTekstowe2.destroy()
    poleTekstowe3.destroy()
    opisPolaTekstowego1.destroy()
    opisPolaTekstowego2.destroy()
    opisPolaTekstowego3.destroy()
    przycisk2.destroy()
    zegar7.destroy()
    if licznik == 1:
	    zadanie2()
    elif licznik == 2:
        zadanie3()
    elif licznik == 3:
        plotno.destroy()
        koniec()
	
	
def updateZegar7():
    global zegar7,czasStart, czyCzas15wlaczony, czasStart
    Czassekunda = 419-round(time.time()-czasStart,0)
    if czasStop7==False:
        if Czassekunda>= 360 and czyCzas15wlaczony==False:
            min= 6
            sec=int(Czassekunda-360)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar7.destroy()
            zegar7=Label(glowneOkno, fg='blue')
            zegar7.place(x=1200,y=10)
            zegar7.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, updateZegar7)
        elif Czassekunda>= 300 and czyCzas15wlaczony==False:
            min=5
            sec=int(Czassekunda-300)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar7.destroy()
            zegar7=Label(glowneOkno, fg='blue')
            zegar7.place(x=1200,y=10)
            zegar7.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, updateZegar7)
        elif Czassekunda>= 240 and czyCzas15wlaczony==False:
            min=4
            sec=int(Czassekunda-240)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar7.destroy()
            zegar7=Label(glowneOkno, fg='blue')
            zegar7.place(x=1200,y=10)
            zegar7.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, updateZegar7)
        elif Czassekunda>= 180 and czyCzas15wlaczony==False:
            min=3
            sec=int(Czassekunda-180)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar7.destroy()
            zegar7=Label(glowneOkno, fg='blue')
            zegar7.place(x=1200,y=10)
            zegar7.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, updateZegar7)
        elif Czassekunda>= 120 and czyCzas15wlaczony==False:
            min=2
            sec=int(Czassekunda-120)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar7.destroy()
            zegar7=Label(glowneOkno, fg='blue')
            zegar7.place(x=1200,y=10)
            zegar7.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, updateZegar7)
        elif Czassekunda>= 60 and czyCzas15wlaczony==False:
            min=1
            sec=int(Czassekunda-60)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar7.destroy()
            zegar7=Label(glowneOkno, fg='blue')
            zegar7.place(x=1200,y=10)
            zegar7.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, updateZegar7)
        elif Czassekunda>= 0 and czyCzas15wlaczony==False:
            min=0
            sec=int(Czassekunda)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar7.destroy()
            zegar7=Label(glowneOkno, fg='red')
            zegar7.place(x=1200,y=10)
            zegar7.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, updateZegar7)
        elif int(Czassekunda)<=0 and czyCzas15wlaczony==False:
            CzasWyswietlany='00:00'
            pass
            ZapiszOdp()
            zegar7.destroy()
			
def koniec():
    global opis1
    opis1=Label(glowneOkno, text="Dziękujemy za współpracę. Proszę zgłosić się do prowadzącego badanie.",font=("Times New Roman",20,))
    opis1.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    
glowneOkno = Tk()
glowneOkno.title("ChessSL")
glowneOkno.attributes("-fullscreen", True)
obraz = Image.open("trzecia.jpg")
obraz2 = Image.open("pierwsza.jpg")
obraz3 = Image.open('druga.jpg')
obraz4 = Image.open("okno.jpg")
obrazTk = ImageTk.PhotoImage(obraz)
obraz2Tk= ImageTk.PhotoImage(obraz2)
obraz3Tk = ImageTk.PhotoImage(obraz3)
obraz4Tk= ImageTk.PhotoImage(obraz4)
plotno = Canvas(glowneOkno, width = 1476, height = 789)
plotno.place(x=370,y=-50)
plotno1= Canvas(glowneOkno,width =1476, height =1200 )
zegar15=Label(glowneOkno)
zegar7=Label(glowneOkno)
czasStart=0
czasStop15=False
czasStop7= False
czyCzas15wlaczony=False
licznik=0
akcja1()
glowneOkno.mainloop()