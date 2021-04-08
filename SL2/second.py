from tkinter import *
from PIL import Image, ImageTk
import time
import codecs
import tkinter as tk

def akcja1():
    global opis, przycisk
    opis=Label(glowneOkno, text="Witaj w drugiej części badania ChessSL. Aby przejść do dalszych instrukcji kliknij Dalej.",font=("Times New Roman",20,),)
    opis.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk= Button( glowneOkno, text = "Dalej",font=("Times New Roman",16,"bold"),background="white",command=akcja2)
    przycisk.place(x=650, y=670)

def akcja2():
    global opis, przycisk
    opis.destroy()
    przycisk.destroy()
    opis=Label(glowneOkno,text = u"Ten etap potrwa ok 60 minut. Będzie się składał z sześciu zadań.",font=("Times New Roman",20,))
    opis.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk = Button( glowneOkno, text ="Dalej ",font=("Times New Roman",16,"bold"),background="white", command=akcja3 )
    przycisk.place(x=650, y=670)

def akcja3():
    global opis, przycisk
    opis.destroy()
    przycisk.destroy()
    opis=Label(glowneOkno,text = u"Każde z nich będzie polegało na ocenie analizy pozycji szachowej.",font=("Times New Roman",20,))
    opis.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja4 )
    przycisk.place(x=650, y=670)

def akcja4():
    global opis, przycisk
    opis.destroy()
    przycisk.destroy()
    opis=Label(glowneOkno,text = u"Oto sposób prezentacji analiz: ",font=("Times New Roman",20,))
    opis.place(x=170, y=10)
    przycisk = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja5 )
    przycisk.place(x=650, y=670)
    plotno1.create_image(1025,576 ,image = obraz6Tk)
    plotno1.place(x=-338,y=-220)

def akcja5():
    global opis, przycisk
    opis.destroy()
    przycisk.destroy()
    opis=Label(glowneOkno,text = u"Zapoznaj się z poleceniami po prawej stronie. Upewnij się, że wszystkie są dla Ciebie jasne.",font=("Times New Roman",20,))
    opis.place(x=180, y=10)
    przycisk = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja6 )
    przycisk.place(x=650, y=670)
    plotno1.create_image(1025,576 ,image = obraz8Tk)
    plotno1.place(x=-338,y=-220)

def akcja6():
    global opis, przycisk
    opis.destroy()
    przycisk.destroy()
    plotno1.destroy()
    opis=Label(glowneOkno,text = u"Pozycje, których analizy będziesz oceniał rozpoznasz z poprzedniego etapu badania.",font=("Times New Roman",20,))
    opis.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja7 )
    przycisk.place(x=650, y=670)

def akcja7():
    global opis, przycisk
    opis.destroy()
    przycisk.destroy()
    opis=Label(glowneOkno,text = u"Autorami pierwszych pięciu analiz są inni szachiści. W zadaniu szóstym spotkasz się z własnym rozwiązaniem.",font=("Times New Roman",20,))
    opis.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja8 )
    przycisk.place(x=650, y=670)

def akcja8():
    global opis, przycisk
    opis.destroy()
    przycisk.destroy()
    opis=Label(glowneOkno,text = u"Czas na ocenę jednej analizy wynosi 10 min. W ostatniej minucie zegar zmieni kolor na czerwony.\nTo sygnał żeby wprowadzić ostatnie poprawki.",font=("Times New Roman",20,))
    opis.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja9 )
    przycisk.place(x=650, y=670)

def akcja9():
    global opis, przycisk
    opis.destroy()
    przycisk.destroy()
    opis=Label(glowneOkno,text = u"Po upływie czasu automatycznie rozpocznie się kolejne zadanie.",font=("Times New Roman",20,))
    opis.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja10 )
    przycisk.place(x=650, y=670)

def akcja10():
    global opis, przycisk
    opis.destroy()
    przycisk.destroy()
    opis=Label(glowneOkno,text = u"Jeżeli skończysz wcześniej, możesz samodzielnie przejść do następnego zadania klikając ZAPISZ.",font=("Times New Roman",20,))
    opis.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja11 )
    przycisk.place(x=650, y=670)

def akcja11():
    global opis, przycisk
    opis.destroy()
    przycisk.destroy()
    opis=Label(glowneOkno,text = u"Możesz korzystać z realnej szachownicy znajdującej się po Twojej prawej stronie.",font=("Times New Roman",20,))
    opis.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja12 )
    przycisk.place(x=650, y=670)

def akcja12():
    global opis, przycisk
    opis.destroy()
    przycisk.destroy()
    opis=Label(glowneOkno,text = u"Jeżeli masz jakieś pytania, zadaj je teraz prowadzącemu.",font=("Times New Roman",20,))
    opis.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk = Button( glowneOkno, text ="Dalej",font=("Times New Roman",16,"bold"),background="white", command=akcja13 )
    przycisk.place(x=650, y=670)

def akcja13():
    global opis, przycisk
    opis.destroy()
    przycisk.destroy()
    opis=Label(glowneOkno,text = u"Jeżeli wszystkie instrukcje są dla Ciebie jasne i nie masz żadnych pytań, rozpocznij klikając zielony przycisk. \nPowodzenia!",font=("Times New Roman",20,))
    opis.place(relx=0.5, rely=0.5, anchor=CENTER)
    przycisk = Button( glowneOkno, text ="Rozpocznij",font=("Times New Roman",16,"bold"),background="green", command=zadanie1 )
    przycisk.place(x=625, y=670)

def zadanie1():
    global opis, przycisk, poleTekstowe1, poleTekstowe2, poleTekstowe3, poleTekstowe4, poleTekstowe5, poleTekstowe6, poleTekstowe7, opisP1, opisP2, opisP3, opisP4, opisP5, opisP6, opisP7,licznik_zadan, czasStart, plotno, R1, R2, sb_2, sb_3, sb_4, sb_5, sb_6, sb_7, opisR
    opis.destroy() # usunięcie instrukcji
    przycisk.destroy()# usunięcie przycisku 'dalej'

    licznik_zadan+=1
    czasStart= time.time()
    UpdateCzas10()
    opis = Label(glowneOkno, text="Ocena analizy nr 1",font=("Times New Roman",20,))
    opis.place(x=15,y=5)
	#okno 1. wyświetlające ocenę gracza.
    opisP1=Label(glowneOkno, text =u"Ocena gracza:",font=("Times New Roman",13))
    opisP1.place(x=10, y=60)
    poleTekstowe1= tk.Text (glowneOkno, width=25,height=1)
    poleTekstowe1.place(x=120, y=62)
	# wyświetlenie w oknie 1 oceny zapisanej w pliku
    plik_tekstowy1 = codecs.open(u"1okno1_ocena.txt","rb")
    tekst_ocena=(plik_tekstowy1.read ())
    plik_tekstowy1.close()
    poleTekstowe1.insert(tk.END,tekst_ocena)
    def zapiszR(): # zapisanie do pliku tekstowego odpowiedzi z radiobutton
        wyborR = "Ocna pozycji: " + str(var.get())
        ocenar = codecs.open("ocenar.txt","a")
        ocenar.write(wyborR + "  ")
        ocenar.close()

    var = IntVar() # określenie typu wartości radiobutton
    opisR=Label(glowneOkno, text=u"Czy zgadzasz się z oceną gracza?",font=("Times New Roman",13))
    opisR.place(x=890, y=15)
    R1 = Radiobutton(glowneOkno, text=u"Tak", variable=var, value=1,command=zapiszR)
    R1.place(x=1140,y=15)
    R2 = Radiobutton(glowneOkno, text=u"Nie", variable=var, value=2,command=zapiszR)
    R2.place(x=1220,y=15)

    opisP2=Label(glowneOkno, text =u"Elementy wskazane przez gracza jako istotne w pozycji:",font=("Times New Roman",13))
    opisP2.place(x=10, y=135)
    sb_2 = tk.Scrollbar(glowneOkno) # zamieszczenie scrollbutton
    poleTekstowe2=tk.Text(glowneOkno, width=55,height=11,yscrollcommand = sb_2.set) # wymiary okna i podpięccie funcji scroll
    sb_2.place(in_ = poleTekstowe2, relx = 1, rely = 0, relheight = 1.)# ustawienie miejsca scrollbutton zrelatywizowane względem okna
    poleTekstowe2.place(x=10, y=160)
    sb_2.config(command = poleTekstowe2.yview)# podłączenie tekstu z poleTekstowe2 do scrollbuttona
	#wyświetlnie w oknie 2 Elementów zapisanych w pliku
    plik_tekstowy2 = open ("1okno2_elementy.txt","rb")
    tekst_ocena=(plik_tekstowy2.read ())
    plik_tekstowy2.close()
    poleTekstowe2.insert(tk.END,tekst_ocena)

    opisP3=Label(glowneOkno, text =u"Posunięcia rozważane przez zawodnika:", justify=(LEFT), font=("Times New Roman",13))
    opisP3.place(x=10, y=380)
    sb_3=tk.Scrollbar(glowneOkno)
    poleTekstowe3= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_3.set )
    sb_3.place(in_ = poleTekstowe3, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe3.place(x=10, y=405)
    sb_3.config(command = poleTekstowe3.yview)
    #wyświetlnie w oknie 3 ruchów kanydatów zapisanych w pliku
    plik_tekstowy3 = open ("1okno3_kandydaty.txt","rb")
    tekst_ocena=(plik_tekstowy3.read ())
    plik_tekstowy3.close()
    poleTekstowe3.insert(tk.END,tekst_ocena)

    opisP4=Label(glowneOkno, text =u"Wybrany przez gracza ruch wraz z planem gry i wariantem:", justify=(LEFT), font=("Times New Roman",13))
    opisP4.place(x=10, y=580)
    sb_4=tk.Scrollbar(glowneOkno)
    poleTekstowe4= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_4.set)
    sb_4.place(in_ = poleTekstowe4, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe4.place(x=10, y=605)
    sb_4.config(command = poleTekstowe4.yview)
    #wyświetlnie w oknie 4 wariantu zapisanego w pliku
    plik_tekstowy4 = open ("1okno4_wariant.txt","rb")
    tekst_ocena=(plik_tekstowy4.read ())
    plik_tekstowy4.close()
    poleTekstowe4.insert(tk.END,tekst_ocena)

    okna_567_doZ5()

    plotno.create_image(301,301 ,image = obraz2Tk) # stworzenie pozycji z zadaniem na określonym płótnie
    przycisk = Button(glowneOkno, text =u"ZAPISZ",font=("Times New Roman",16,"bold"),background="white", command=zapiszOdp)
    przycisk.place(x=630,y=670)

def zadanie2():
    global opis, przycisk, poleTekstowe1, poleTekstowe2, poleTekstowe3, poleTekstowe4, poleTekstowe5, poleTekstowe6, poleTekstowe7, opisP1, opisP2, opisP3, opisP4, opisP5, opisP6, opisP7,licznik_zadan, czasStart, plotno, R1, R2, sb_2, sb_3, sb_4, sb_5, sb_6, sb_7, opisR

    licznik_zadan+=1
    czasStart= time.time()
    UpdateCzas10()
    opis = Label(glowneOkno, text="Ocena analizy nr 2",font=("Times New Roman",20,))
    opis.place(x=15,y=5)
	#okno 1. wyświetlające ocenę gracza.
    opisP1=Label(glowneOkno, text =u"Ocena gracza:",font=("Times New Roman",13))
    opisP1.place(x=10, y=60)
    poleTekstowe1= tk.Text (glowneOkno, width=25,height=1)
    poleTekstowe1.place(x=120, y=62)
	# wyświetlenie w oknie 1 oceny zapisanej w pliku
    plik_tekstowy1 = codecs.open("2okno1_ocena.txt","rb")
    tekst_ocena=(plik_tekstowy1.read ())
    plik_tekstowy1.close()
    poleTekstowe1.insert(tk.END,tekst_ocena)
    def zapiszR(): # zapisanie do pliku tekstowego odpowiedzi z radiobutton
        wyborR = "Ocna pozycji: " + str(var.get())
        ocenar = codecs.open("ocenar.txt","a")
        ocenar.write(wyborR + "  ")
        ocenar.close()

    var = IntVar() # określenie typu wartości radiobutton
    opisR=Label(glowneOkno, text=u"Czy zgadzasz się z oceną gracza?",font=("Times New Roman",13))
    opisR.place(x=890, y=15)
    R1 = Radiobutton(glowneOkno, text=u"Tak", variable=var, value=1,command=zapiszR)
    R1.place(x=1140,y=15)
    R2 = Radiobutton(glowneOkno, text=u"Nie", variable=var, value=2,command=zapiszR)
    R2.place(x=1220,y=15)

    opisP2=Label(glowneOkno, text =u"Elementy wskazane przez gracza jako istotne w pozycji:",font=("Times New Roman",13))
    opisP2.place(x=10, y=135)
    sb_2 = tk.Scrollbar(glowneOkno) # zamieszczenie scrollbutton
    poleTekstowe2=tk.Text(glowneOkno, width=55,height=11,yscrollcommand = sb_2.set) # wymiary okna i podpięccie funcji scroll
    sb_2.place(in_ = poleTekstowe2, relx = 1, rely = 0, relheight = 1.)# ustawienie miejsca scrollbutton zrelatywizowane względem okna
    poleTekstowe2.place(x=10, y=160)
    sb_2.config(command = poleTekstowe2.yview)# podłączenie tekstu z poleTekstowe2 do scrollbuttona
	#wyświetlnie w oknie 2 Elementów zapisanych w pliku
    plik_tekstowy2 = open ("2okno2_elementy.txt","rb")
    tekst_ocena=(plik_tekstowy2.read ())
    plik_tekstowy2.close()
    poleTekstowe2.insert(tk.END,tekst_ocena)

    opisP3=Label(glowneOkno, text =u"Posunięcia rozważane przez zawodnika:", justify=(LEFT), font=("Times New Roman",13))
    opisP3.place(x=10, y=380)
    sb_3=tk.Scrollbar(glowneOkno)
    poleTekstowe3= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_3.set )
    sb_3.place(in_ = poleTekstowe3, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe3.place(x=10, y=405)
    sb_3.config(command = poleTekstowe3.yview)
    #wyświetlnie w oknie 3 ruchów kanydatów zapisanych w pliku
    plik_tekstowy3 = open ("2okno3_kandydaty.txt","rb")
    tekst_ocena=(plik_tekstowy3.read ())
    plik_tekstowy3.close()
    poleTekstowe3.insert(tk.END,tekst_ocena)

    opisP4=Label(glowneOkno, text =u"Wybrany przez gracza ruch wraz z planem gry i wariantem:", justify=(LEFT), font=("Times New Roman",13))
    opisP4.place(x=10, y=580)
    sb_4=tk.Scrollbar(glowneOkno)
    poleTekstowe4= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_4.set)
    sb_4.place(in_ = poleTekstowe4, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe4.place(x=10, y=605)
    sb_4.config(command = poleTekstowe4.yview)
    #wyświetlnie w oknie 4 wariantu zapisanego w pliku
    plik_tekstowy4 = open ("2okno4_wariant.txt","rb")
    tekst_ocena=(plik_tekstowy4.read ())
    plik_tekstowy4.close()
    poleTekstowe4.insert(tk.END,tekst_ocena)

    okna_567_doZ5()

    plotno.create_image(301,301 ,image = obraz3Tk) # stworzenie pozycji z zadaniem na określonym płótnie
    przycisk = Button(glowneOkno, text =u"ZAPISZ",font=("Times New Roman",16,"bold"),background="white", command=zapiszOdp)
    przycisk.place(x=630,y=670)

def zadanie3():
    global opis, przycisk, poleTekstowe1, poleTekstowe2, poleTekstowe3, poleTekstowe4, poleTekstowe5, poleTekstowe6, poleTekstowe7, opisP1, opisP2, opisP3, opisP4, opisP5, opisP6, opisP7,licznik_zadan, czasStart, plotno, R1, R2, sb_2, sb_3, sb_4, sb_5, sb_6, sb_7, opisR

    licznik_zadan+=1
    czasStart= time.time()
    UpdateCzas10()
    opis = Label(glowneOkno, text="Ocena analizy nr 3",font=("Times New Roman",20,))
    opis.place(x=15,y=5)
	#okno 1. wyświetlające ocenę gracza.
    opisP1=Label(glowneOkno, text =u"Ocena gracza:",font=("Times New Roman",13))
    opisP1.place(x=10, y=60)
    poleTekstowe1= tk.Text (glowneOkno, width=25,height=1)
    poleTekstowe1.place(x=120, y=62)
	# wyświetlenie w oknie 1 oceny zapisanej w pliku
    plik_tekstowy1 = codecs.open("3okno1_ocena.txt","rb")
    tekst_ocena=(plik_tekstowy1.read ())
    plik_tekstowy1.close()
    poleTekstowe1.insert(tk.END,tekst_ocena)
    def zapiszR(): # zapisanie do pliku tekstowego odpowiedzi z radiobutton
        wyborR = "Ocna pozycji: " + str(var.get())
        ocenar = codecs.open("ocenar.txt","a")
        ocenar.write(wyborR + "  ")
        ocenar.close()

    var = IntVar() # określenie typu wartości radiobutton
    opisR=Label(glowneOkno, text=u"Czy zgadzasz się z oceną gracza?",font=("Times New Roman",13))
    opisR.place(x=890, y=15)
    R1 = Radiobutton(glowneOkno, text=u"Tak", variable=var, value=1,command=zapiszR)
    R1.place(x=1140,y=15)
    R2 = Radiobutton(glowneOkno, text=u"Nie", variable=var, value=2,command=zapiszR)
    R2.place(x=1220,y=15)

    opisP2=Label(glowneOkno, text =u"Elementy wskazane przez gracza jako istotne w pozycji:",font=("Times New Roman",13))
    opisP2.place(x=10, y=135)
    sb_2 = tk.Scrollbar(glowneOkno) # zamieszczenie scrollbutton
    poleTekstowe2=tk.Text(glowneOkno, width=55,height=11,yscrollcommand = sb_2.set) # wymiary okna i podpięccie funcji scroll
    sb_2.place(in_ = poleTekstowe2, relx = 1, rely = 0, relheight = 1.)# ustawienie miejsca scrollbutton zrelatywizowane względem okna
    poleTekstowe2.place(x=10, y=160)
    sb_2.config(command = poleTekstowe2.yview)# podłączenie tekstu z poleTekstowe2 do scrollbuttona
	#wyświetlnie w oknie 2 Elementów zapisanych w pliku
    plik_tekstowy2 = open ("3okno2_elementy.txt","rb")
    tekst_ocena=(plik_tekstowy2.read ())
    plik_tekstowy2.close()
    poleTekstowe2.insert(tk.END,tekst_ocena)

    opisP3=Label(glowneOkno, text =u"Posunięcia rozważane przez zawodnika:", justify=(LEFT), font=("Times New Roman",13))
    opisP3.place(x=10, y=380)
    sb_3=tk.Scrollbar(glowneOkno)
    poleTekstowe3= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_3.set )
    sb_3.place(in_ = poleTekstowe3, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe3.place(x=10, y=405)
    sb_3.config(command = poleTekstowe3.yview)
    #wyświetlnie w oknie 3 ruchów kanydatów zapisanych w pliku
    plik_tekstowy3 = open ("3okno3_kandydaty.txt","rb")
    tekst_ocena=(plik_tekstowy3.read ())
    plik_tekstowy3.close()
    poleTekstowe3.insert(tk.END,tekst_ocena)

    opisP4=Label(glowneOkno, text =u"Wybrany przez gracza ruch wraz z planem gry i wariantem:", justify=(LEFT), font=("Times New Roman",13))
    opisP4.place(x=10, y=580)
    sb_4=tk.Scrollbar(glowneOkno)
    poleTekstowe4= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_4.set)
    sb_4.place(in_ = poleTekstowe4, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe4.place(x=10, y=605)
    sb_4.config(command = poleTekstowe4.yview)
    #wyświetlnie w oknie 4 wariantu zapisanego w pliku
    plik_tekstowy4 = open ("3okno4_wariant.txt","rb")
    tekst_ocena=(plik_tekstowy4.read ())
    plik_tekstowy4.close()
    poleTekstowe4.insert(tk.END,tekst_ocena)

    okna_567_doZ5()

    plotno.create_image(301,301 ,image = obrazTk) # stworzenie pozycji z zadaniem na określonym płótnie
    przycisk = Button(glowneOkno, text =u"ZAPISZ",font=("Times New Roman",16,"bold"),background="white", command=zapiszOdp)
    przycisk.place(x=630,y=670)

def zadanie4():
    global opis, przycisk, poleTekstowe1, poleTekstowe2, poleTekstowe3, poleTekstowe4, poleTekstowe5, poleTekstowe6, poleTekstowe7, opisP1, opisP2, opisP3, opisP4, opisP5, opisP6, opisP7,licznik_zadan, czasStart, plotno, R1, R2, sb_2, sb_3, sb_4, sb_5, sb_6, sb_7, opisR

    licznik_zadan+=1
    czasStart= time.time()
    UpdateCzas10()
    opis = Label(glowneOkno, text="Ocena analizy nr 4",font=("Times New Roman",20,))
    opis.place(x=15,y=5)
	#okno 1. wyświetlające ocenę gracza.
    opisP1=Label(glowneOkno, text =u"Ocena gracza:",font=("Times New Roman",13))
    opisP1.place(x=10, y=60)
    poleTekstowe1= tk.Text (glowneOkno, width=25,height=1)
    poleTekstowe1.place(x=120, y=62)
	# wyświetlenie w oknie 1 oceny zapisanej w pliku
    plik_tekstowy1 = codecs.open("4okno1_ocena.txt","rb")
    tekst_ocena=(plik_tekstowy1.read ())
    plik_tekstowy1.close()
    poleTekstowe1.insert(tk.END,tekst_ocena)
    def zapiszR(): # zapisanie do pliku tekstowego odpowiedzi z radiobutton
        wyborR = "Ocna pozycji: " + str(var.get())
        ocenar = codecs.open("ocenar.txt","a")
        ocenar.write(wyborR + "  ")
        ocenar.close()

    var = IntVar() # określenie typu wartości radiobutton
    opisR=Label(glowneOkno, text=u"Czy zgadzasz się z oceną gracza?",font=("Times New Roman",13))
    opisR.place(x=890, y=15)
    R1 = Radiobutton(glowneOkno, text=u"Tak", variable=var, value=1,command=zapiszR)
    R1.place(x=1140,y=15)
    R2 = Radiobutton(glowneOkno, text=u"Nie", variable=var, value=2,command=zapiszR)
    R2.place(x=1220,y=15)

    opisP2=Label(glowneOkno, text =u"Elementy wskazane przez gracza jako istotne w pozycji:",font=("Times New Roman",13))
    opisP2.place(x=10, y=135)
    sb_2 = tk.Scrollbar(glowneOkno) # zamieszczenie scrollbutton
    poleTekstowe2=tk.Text(glowneOkno, width=55,height=11,yscrollcommand = sb_2.set) # wymiary okna i podpięccie funcji scroll
    sb_2.place(in_ = poleTekstowe2, relx = 1, rely = 0, relheight = 1.)# ustawienie miejsca scrollbutton zrelatywizowane względem okna
    poleTekstowe2.place(x=10, y=160)
    sb_2.config(command = poleTekstowe2.yview)# podłączenie tekstu z poleTekstowe2 do scrollbuttona
	#wyświetlnie w oknie 2 Elementów zapisanych w pliku
    plik_tekstowy2 = open ("4okno2_elementy.txt","rb")
    tekst_ocena=(plik_tekstowy2.read ())
    plik_tekstowy2.close()
    poleTekstowe2.insert(tk.END,tekst_ocena)

    opisP3=Label(glowneOkno, text =u"Posunięcia rozważane przez zawodnika:", justify=(LEFT), font=("Times New Roman",13))
    opisP3.place(x=10, y=380)
    sb_3=tk.Scrollbar(glowneOkno)
    poleTekstowe3= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_3.set )
    sb_3.place(in_ = poleTekstowe3, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe3.place(x=10, y=405)
    sb_3.config(command = poleTekstowe3.yview)
    #wyświetlnie w oknie 3 ruchów kanydatów zapisanych w pliku
    plik_tekstowy3 = open ("4okno3_kandydaty.txt","rb")
    tekst_ocena=(plik_tekstowy3.read ())
    plik_tekstowy3.close()
    poleTekstowe3.insert(tk.END,tekst_ocena)

    opisP4=Label(glowneOkno, text =u"Wybrany przez gracza ruch wraz z planem gry i wariantem:", justify=(LEFT), font=("Times New Roman",13))
    opisP4.place(x=10, y=580)
    sb_4=tk.Scrollbar(glowneOkno)
    poleTekstowe4= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_4.set)
    sb_4.place(in_ = poleTekstowe4, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe4.place(x=10, y=605)
    sb_4.config(command = poleTekstowe4.yview)
    #wyświetlnie w oknie 4 wariantu zapisanego w pliku
    plik_tekstowy4 = open ("4okno4_wariant.txt","rb")
    tekst_ocena=(plik_tekstowy4.read ())
    plik_tekstowy4.close()
    poleTekstowe4.insert(tk.END,tekst_ocena)

    okna_567_doZ5()

    plotno.create_image(301,301 ,image = obraz3Tk) # stworzenie pozycji z zadaniem na określonym płótnie
    przycisk = Button(glowneOkno, text =u"ZAPISZ",font=("Times New Roman",16,"bold"),background="white", command=zapiszOdp)
    przycisk.place(x=630,y=670)

def zadanie5():
    global opis, przycisk, poleTekstowe1, poleTekstowe2, poleTekstowe3, poleTekstowe4, poleTekstowe5, poleTekstowe6, poleTekstowe7, opisP1, opisP2, opisP3, opisP4, opisP5, opisP6, opisP7,licznik_zadan, czasStart, plotno, R1, R2, sb_2, sb_3, sb_4, sb_5, sb_6, sb_7, opisR

    licznik_zadan+=1
    czasStart= time.time()
    UpdateCzas10()
    opis = Label(glowneOkno, text="Ocena analizy nr 5",font=("Times New Roman",20,))
    opis.place(x=15,y=5)
	#okno 1. wyświetlające ocenę gracza.
    opisP1=Label(glowneOkno, text =u"Ocena gracza:",font=("Times New Roman",13))
    opisP1.place(x=10, y=60)
    poleTekstowe1= tk.Text (glowneOkno, width=25,height=1)
    poleTekstowe1.place(x=120, y=62)
	# wyświetlenie w oknie 1 oceny zapisanej w pliku
    plik_tekstowy1 = codecs.open("5okno1_ocena.txt","rb")
    tekst_ocena=(plik_tekstowy1.read ())
    plik_tekstowy1.close()
    poleTekstowe1.insert(tk.END,tekst_ocena)
    def zapiszR(): # zapisanie do pliku tekstowego odpowiedzi z radiobutton
        wyborR = "Ocna pozycji: " + str(var.get())
        ocenar = codecs.open("ocenar.txt","a")
        ocenar.write(wyborR + "  ")
        ocenar.close()

    var = IntVar() # określenie typu wartości radiobutton
    opisR=Label(glowneOkno, text=u"Czy zgadzasz się z oceną gracza?",font=("Times New Roman",13))
    opisR.place(x=890, y=15)
    R1 = Radiobutton(glowneOkno, text=u"Tak", variable=var, value=1,command=zapiszR)
    R1.place(x=1140,y=15)
    R2 = Radiobutton(glowneOkno, text=u"Nie", variable=var, value=2,command=zapiszR)
    R2.place(x=1220,y=15)

    opisP2=Label(glowneOkno, text =u"Elementy wskazane przez gracza jako istotne w pozycji:",font=("Times New Roman",13))
    opisP2.place(x=10, y=135)
    sb_2 = tk.Scrollbar(glowneOkno) # zamieszczenie scrollbutton
    poleTekstowe2=tk.Text(glowneOkno, width=55,height=11,yscrollcommand = sb_2.set) # wymiary okna i podpięccie funcji scroll
    sb_2.place(in_ = poleTekstowe2, relx = 1, rely = 0, relheight = 1.)# ustawienie miejsca scrollbutton zrelatywizowane względem okna
    poleTekstowe2.place(x=10, y=160)
    sb_2.config(command = poleTekstowe2.yview)# podłączenie tekstu z poleTekstowe2 do scrollbuttona
	#wyświetlnie w oknie 2 Elementów zapisanych w pliku
    plik_tekstowy2 = open ("5okno2_elementy.txt","rb")
    tekst_ocena=(plik_tekstowy2.read ())
    plik_tekstowy2.close()
    poleTekstowe2.insert(tk.END,tekst_ocena)

    opisP3=Label(glowneOkno, text =u"Posunięcia rozważane przez zawodnika:", justify=(LEFT), font=("Times New Roman",13))
    opisP3.place(x=10, y=380)
    sb_3=tk.Scrollbar(glowneOkno)
    poleTekstowe3= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_3.set )
    sb_3.place(in_ = poleTekstowe3, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe3.place(x=10, y=405)
    sb_3.config(command = poleTekstowe3.yview)
    #wyświetlnie w oknie 3 ruchów kanydatów zapisanych w pliku
    plik_tekstowy3 = open ("5okno3_kandydaty.txt","rb")
    tekst_ocena=(plik_tekstowy3.read ())
    plik_tekstowy3.close()
    poleTekstowe3.insert(tk.END,tekst_ocena)

    opisP4=Label(glowneOkno, text =u"Wybrany przez gracza ruch wraz z planem gry i wariantem:", justify=(LEFT), font=("Times New Roman",13))
    opisP4.place(x=10, y=580)
    sb_4=tk.Scrollbar(glowneOkno)
    poleTekstowe4= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_4.set)
    sb_4.place(in_ = poleTekstowe4, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe4.place(x=10, y=605)
    sb_4.config(command = poleTekstowe4.yview)
    #wyświetlnie w oknie 4 wariantu zapisanego w pliku
    plik_tekstowy4 = open ("5okno4_wariant.txt","rb")
    tekst_ocena=(plik_tekstowy4.read ())
    plik_tekstowy4.close()
    poleTekstowe4.insert(tk.END,tekst_ocena)

    okna_567_doZ5()

    plotno.create_image(301,301 ,image = obraz2Tk) # stworzenie pozycji z zadaniem na określonym płótnie
    przycisk = Button(glowneOkno, text =u"ZAPISZ",font=("Times New Roman",16,"bold"),background="white", command=zapiszOdp)
    przycisk.place(x=630,y=670)
def zadanie6():
    global opis, przycisk, poleTekstoweD, poleTekstowe1, poleTekstowe2, poleTekstowe3, poleTekstowe4, poleTekstowe5, poleTekstowe6, poleTekstowe7, opisD, opisP1, opisP2, opisP3, opisP4, opisP5, opisP6, opisP7,licznik_zadan, czasStart, plotno, R1, R2, sb_2, sb_3, sb_4, sb_5, sb_6, sb_7, opisR

    licznik_zadan+=1
    czasStart= time.time()
    UpdateCzas10()
    opis = Label(glowneOkno, text="Ocena Twojej analizy",font=("Times New Roman",20,))
    opis.place(x=15,y=5)
	#okno 1. wyświetlające ocenę gracza.
    opisP1=Label(glowneOkno, text =u"Twoja ocena:",font=("Times New Roman",13))
    opisP1.place(x=10, y=60)
    poleTekstowe1= tk.Text (glowneOkno, width=25,height=1)
    poleTekstowe1.place(x=120, y=62)
	# wyświetlenie w oknie 1 oceny zapisanej w pliku
    plik_tekstowy1 = codecs.open("6okno1_ocena.txt","rb")
    tekst_ocena=(plik_tekstowy1.read ())
    plik_tekstowy1.close()
    poleTekstowe1.insert(tk.END,tekst_ocena)
    def zapiszR(): # zapisanie do pliku tekstowego odpowiedzi z radiobutton
        wyborR = "Ocna pozycji: " + str(var.get())
        ocenar = codecs.open("ocenar.txt","a")
        ocenar.write(wyborR + "  ")
        ocenar.close()

    var = IntVar() # określenie typu wartości radiobutton
    opisR=Label(glowneOkno, text=u"Czy zgadzasz się ze swoją oceną?",font=("Times New Roman",13))
    opisR.place(x=890, y=15)
    R1 = Radiobutton(glowneOkno, text=u"Tak", variable=var, value=1,command=zapiszR)
    R1.place(x=1140,y=15)
    R2 = Radiobutton(glowneOkno, text=u"Nie", variable=var, value=2,command=zapiszR)
    R2.place(x=1220,y=15)

    opisP2=Label(glowneOkno, text =u"Elementy wskazane przez Ciebie jako istotne w pozycji:",font=("Times New Roman",13))
    opisP2.place(x=10, y=135)
    sb_2 = tk.Scrollbar(glowneOkno) # zamieszczenie scrollbutton
    poleTekstowe2=tk.Text(glowneOkno, width=55,height=11,yscrollcommand = sb_2.set) # wymiary okna i podpięccie funcji scroll
    sb_2.place(in_ = poleTekstowe2, relx = 1, rely = 0, relheight = 1.)# ustawienie miejsca scrollbutton zrelatywizowane względem okna
    poleTekstowe2.place(x=10, y=160)
    sb_2.config(command = poleTekstowe2.yview)# podłączenie tekstu z poleTekstowe2 do scrollbuttona
	#wyświetlnie w oknie 2 Elementów zapisanych w pliku
    plik_tekstowy2 = open ("6okno2_elementy.txt","rb")
    tekst_ocena=(plik_tekstowy2.read ())
    plik_tekstowy2.close()
    poleTekstowe2.insert(tk.END,tekst_ocena)

    opisP3=Label(glowneOkno, text =u"Posunięcia, które rozważałeś:", justify=(LEFT), font=("Times New Roman",13))
    opisP3.place(x=10, y=380)
    sb_3=tk.Scrollbar(glowneOkno)
    poleTekstowe3= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_3.set )
    sb_3.place(in_ = poleTekstowe3, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe3.place(x=10, y=405)
    sb_3.config(command = poleTekstowe3.yview)
    #wyświetlnie w oknie 3 ruchów kanydatów zapisanych w pliku
    plik_tekstowy3 = open ("6okno3_kandydaty.txt","rb")
    tekst_ocena=(plik_tekstowy3.read ())
    plik_tekstowy3.close()
    poleTekstowe3.insert(tk.END,tekst_ocena)

    opisP4=Label(glowneOkno, text =u"Wybrany przez Ciebie ruch wraz z planem gry i wariantem:", justify=(LEFT), font=("Times New Roman",13))
    opisP4.place(x=10, y=580)
    sb_4=tk.Scrollbar(glowneOkno)
    poleTekstowe4= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_4.set)
    sb_4.place(in_ = poleTekstowe4, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe4.place(x=10, y=605)
    sb_4.config(command = poleTekstowe4.yview)
    #wyświetlnie w oknie 4 wariantu zapisanego w pliku
    plik_tekstowy4 = open ("6okno4_wariant.txt","rb")
    tekst_ocena=(plik_tekstowy4.read ())
    plik_tekstowy4.close()
    poleTekstowe4.insert(tk.END,tekst_ocena)

    opisD= Label(glowneOkno, text= u"Jeśli się nie zgadzasz, zapisz swoją ocenę:",justify=(LEFT), font=("Times New Roman",13))
    opisD.place(x=890,y=50)
    poleTekstoweD=Text(glowneOkno,width=25, height=1)
    poleTekstoweD.place(x=890,y=77)

    opisP5=Label(glowneOkno, text =u"Odnieś się do każdego elementu, który wcześniej wskazałeś.\nCzy jest poprawny? Czy jest istotny w tej sytuacji?\nJeżeli pominąłeś jakiś istotny element, wypisz go:", justify=(LEFT), font=("Times New Roman",13))
    opisP5.place(x=890, y=105)
    sb_5=tk.Scrollbar(glowneOkno)
    poleTekstowe5=Text(glowneOkno, width=55,height=11,yscrollcommand = sb_5.set)
    sb_5.place(in_ = poleTekstowe5, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe5.place(x=890, y=170)
    sb_5.config(command = poleTekstowe5.yview)

    opisP6=Label(glowneOkno, text =u"Czy pominąłeś jakiś ważny ruch, który należałoby rozważyć\nw tej pozycji? Jeśli uważasz, że tak, wypisz go:", justify=(LEFT), font=("Times New Roman",13))
    opisP6.place(x=890, y=360)
    sb_6=tk.Scrollbar(glowneOkno)
    poleTekstowe6= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_6.set)
    sb_6.place(in_ = poleTekstowe6, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe6.place(x=890, y=405)
    sb_6.config(command = poleTekstowe6.yview)

    opisP7=Label(glowneOkno, text =u"Czy wybrałeś najlepsze posunięcie? Jeśli nie, zaproponuj lepsze. \nCzy dalej uważasz, że jest to najlepszy plan/kontynuacja?", justify=(LEFT), font=("Times New Roman",13))
    opisP7.place(x=890, y=560)
    sb_7=tk.Scrollbar(glowneOkno)
    poleTekstowe7= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_7.set)
    poleTekstowe7.place(x=890, y=605)
    sb_7.place(in_ = poleTekstowe7, relx = 1, rely = 0, relheight = 1.)
    sb_7.config(command = poleTekstowe7.yview)

    plotno.create_image(301,301 ,image = obrazTk) # stworzenie pozycji z zadaniem na określonym płótnie
    przycisk = Button(glowneOkno, text =u"ZAPISZ",font=("Times New Roman",16,"bold"),background="white", command=zapiszOdp)
    przycisk.place(x=630,y=670)

def okna_567_doZ5(): #funkcja z oknami, które się powtarzają w każdym zadaniu 1-5
    global poleTekstowe5, poleTekstowe6, poleTekstowe7, poleTekstoweD, opisP5, opisP6, opisP7, opisD, sb_5, sb_6, sb_7

    opisD= Label(glowneOkno, text= u"Jeśli się nie zgadzasz, zapisz swoją ocenę:",justify=(LEFT), font=("Times New Roman",13))
    opisD.place(x=890,y=50)
    poleTekstoweD=Text(glowneOkno,width=25, height=1)
    poleTekstoweD.place(x=890,y=77)

    opisP5=Label(glowneOkno, text =u"Odnieś się do każdego elementu wskazanego przez gracza.\nCzy jest poprawny? Czy jest istotny w tej sytuacji?\nJeżeli gracz pominął istotny element w tej pozycji, wypisz go:", justify=(LEFT), font=("Times New Roman",13))
    opisP5.place(x=890, y=105)
    sb_5=tk.Scrollbar(glowneOkno)
    poleTekstowe5=Text(glowneOkno, width=55,height=11,yscrollcommand = sb_5.set)
    sb_5.place(in_ = poleTekstowe5, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe5.place(x=890, y=170)
    sb_5.config(command = poleTekstowe5.yview)

    opisP6=Label(glowneOkno, text =u"Czy gracz pominął jakiś ważny ruch, który należałoby rozważyć\nw tej pozycji? Jeśli uważasz, że tak, wypisz go:", justify=(LEFT), font=("Times New Roman",13))
    opisP6.place(x=890, y=360)
    sb_6=tk.Scrollbar(glowneOkno)
    poleTekstowe6= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_6.set)
    sb_6.place(in_ = poleTekstowe6, relx = 1, rely = 0, relheight = 1.)
    poleTekstowe6.place(x=890, y=405)
    sb_6.config(command = poleTekstowe6.yview)

    opisP7=Label(glowneOkno, text =u"Czy gracz wybrał najlepsze posunięcie? Jeśli nie, zaproponuj lepsze. \nCzy zgadasz się, że jest to poprawny plan/kontynuacja?", justify=(LEFT), font=("Times New Roman",13))
    opisP7.place(x=890, y=560)
    sb_7=tk.Scrollbar(glowneOkno)
    poleTekstowe7= Text(glowneOkno, width=55,height=9,yscrollcommand = sb_7.set)
    poleTekstowe7.place(x=890, y=605)
    sb_7.place(in_ = poleTekstowe7, relx = 1, rely = 0, relheight = 1.)
    sb_7.config(command = poleTekstowe7.yview)


def UpdateCzas10():
    global zegar10, czasStart, czasStop
    czasSekunda= 600- round(time.time() - czasStart,0)
    if czasStop==False:
        if czasSekunda >= 600:
            min=10
            sec= int(czasSekunda - 600)
            if sec<10:
                sec='0' + str(sec)
            CzasWyswietlany=str(min)+':'+ str(sec)
            zegar10.destroy()
            zegar10=Label(glowneOkno)
            zegar10.place(x=620,y=10)
            zegar10.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateCzas10)
        elif czasSekunda>= 540:
            min=9
            sec=int(czasSekunda-540)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar10.destroy()
            zegar10=Label(glowneOkno)
            zegar10.place(x=623,y=10)
            zegar10.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateCzas10)
        elif czasSekunda>= 480:
            min=8
            sec=int(czasSekunda-480)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar10.destroy()
            zegar10=Label(glowneOkno)
            zegar10.place(x=623,y=10)
            zegar10.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateCzas10)
        elif czasSekunda>= 420:
            min=7
            sec=int(czasSekunda-420)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar10.destroy()
            zegar10=Label(glowneOkno)
            zegar10.place(x=623,y=10)
            zegar10.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateCzas10)
        elif czasSekunda>= 360:
            min=6
            sec=int(czasSekunda-360)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar10.destroy()
            zegar10=Label(glowneOkno)
            zegar10.place(x=623,y=10)
            zegar10.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateCzas10)
        elif czasSekunda>= 300:
            min=5
            sec=int(czasSekunda-300)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar10.destroy()
            zegar10=Label(glowneOkno)
            zegar10.place(x=623,y=10)
            zegar10.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateCzas10)
        elif czasSekunda>= 240:
            min=4
            sec=int(czasSekunda-240)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar10.destroy()
            zegar10=Label(glowneOkno)
            zegar10.place(x=623,y=10)
            zegar10.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateCzas10)
        elif czasSekunda>= 180:
            min=3
            sec=int(czasSekunda-180)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar10.destroy()
            zegar10=Label(glowneOkno)
            zegar10.place(x=623,y=10)
            zegar10.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateCzas10)
        elif czasSekunda>= 120:
            min=2
            sec=int(czasSekunda-120)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar10.destroy()
            zegar10=Label(glowneOkno)
            zegar10.place(x=623,y=10)
            zegar10.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateCzas10)
        elif czasSekunda>= 60:
            min=1
            sec=int(czasSekunda-60)
            if sec<10:
               sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar10.destroy()
            zegar10=Label(glowneOkno)
            zegar10.place(x=623,y=10)
            zegar10.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateCzas10)
        elif czasSekunda>0:
            min=0
            sec=int(czasSekunda)
            if sec<10:
                sec='0' + str(sec)
            CzasWyswietlany='0'+str(min)+':'+ str(sec)
            zegar10.destroy()
            zegar10=Label(glowneOkno, fg='red')
            zegar10.place(x=623,y=10)
            zegar10.configure(text=CzasWyswietlany,font=("Times New Roman",35,"bold"))
            glowneOkno.after(1000, UpdateCzas10)
        else:
            zapiszOdp()

def zapiszOdp():
    global czasStop, licznik_zadan, poleTekstoweD, poleTekstowe1, poleTekstowe2, poleTekstowe3, poleTekstowe4, poleTekstowe5, poleTekstowe6, poleTekstowe7, opisD, opisP1, opisP2, opisP3, opisP4, opisP5, opisP6, opisP7, plotno, R1, R2, sb_2, sb_3, sb_4, sb_5, sb_6, sb_7, opisR, zegar10, OdpD, OdpElementy, OdpKandydaty, OdpWariant
    czasStop=True
    if licznik_zadan ==1:
#pobranie odpowiedzi
        pobierzOdp()
        plik_tekstowy = codecs.open("Odp1.txt", "a", "utf-8")
        plik_tekstowy.write(u"ocenaD:" + OdpD + u"#### Ocena elementów: " + OdpElementy + u"##### Ocena kandydatów: " + OdpKandydaty + u"##### Ocena wariantu: " + OdpWariant)
        plik_tekstowy.close()
#wprowadzenie rozdzielenia w zapisie odp z radiobutton
        ocenar = codecs.open("ocenar.txt","a")
        ocenar.write(u' ###zadanie2### ')
        ocenar.close()
#wyczyszczenie okna przed kolejnym zadaniem
        kasuj()
        czasStop=False
        zadanie2()
    elif licznik_zadan ==2:
#pobranie odpowiedzi
        pobierzOdp()
        plik_tekstowy = codecs.open("Odp2.txt", "a", "utf-8")
        plik_tekstowy.write(u"ocenaD:"+ OdpD + u"Ocena elementów: " + OdpElementy + u"##### Ocena kandydatów: " + OdpKandydaty + u"##### Ocena wariantu: " + OdpWariant)
        plik_tekstowy.close()
#wprowadzenie rozdzielenia w zapisie odp z radiobutton
        ocenar = codecs.open("ocenar.txt","a")
        ocenar.write(u' ###zadanie3### ')
        ocenar.close()
#wyczyszczenie okna przed kolejnym zadaniem
        kasuj()
        czasStop=False
        zadanie3()
    elif licznik_zadan ==3:
#pobranie odpowiedzi
        pobierzOdp()
        plik_tekstowy = codecs.open("Odp3.txt", "a", "utf-8")
        plik_tekstowy.write(u"ocenaD:" + OdpD + u"Ocena elementów: " + OdpElementy + u"##### Ocena kandydatów: " + OdpKandydaty + u"##### Ocena wariantu: " + OdpWariant)
        plik_tekstowy.close()
#wprowadzenie rozdzielenia w zapisie odp z radiobutton
        ocenar = codecs.open("ocenar.txt","a")
        ocenar.write(u' ###zadanie4### ')
        ocenar.close()
# wyczyszczenie okna przed kolejnym zadaniem
        kasuj()
        czasStop=False
        zadanie4()
    elif licznik_zadan ==4:
#poranie odpowiedzi
        pobierzOdp()
        plik_tekstowy = codecs.open("Odp4.txt", "a", "utf-8")
        plik_tekstowy.write(u"ocenaD:" + OdpD + u"Ocena elementów: " + OdpElementy + u"##### Ocena kandydatów: " + OdpKandydaty + u"##### Ocena wariantu: " + OdpWariant)
        plik_tekstowy.close()
#wprowadzenie rozdzielenia w zapisie odp z radiobutton
        ocenar = codecs.open("ocenar.txt","a")
        ocenar.write(u' ###zadanie5### ')
        ocenar.close()
# wyczyszczenie okna przed kolejnym zadaniem
        kasuj()
        czasStop=False
        zadanie5()
    elif licznik_zadan ==5:
#pobranie odpowiedzi
        pobierzOdp()
        plik_tekstowy = codecs.open("Odp5.txt", "a", "utf-8")
        plik_tekstowy.write(u"OdpD:" + OdpD + u"Ocena elementów: " + OdpElementy + u"##### Ocena kandydatów: " + OdpKandydaty + u"##### Ocena wariantu: " + OdpWariant)
        plik_tekstowy.close()
#wprowadzenie rozdzielenia w zapisie odp z radiobutton
        ocenar = codecs.open("ocenar.txt","a")
        ocenar.write(u' ###zadanie6### ')
        ocenar.close()
# wyczyszczenie okna przed kolejnym zadaniem
        kasuj()
        czasStop=False
        zadanie6()
    elif licznik_zadan ==6:
#pobranie odpowiedzi
        pobierzOdp()
        plik_tekstowy = codecs.open("Odp6.txt", "a", "utf-8")
        plik_tekstowy.write(u"OdpD:" + OdpD + u"Ocena elementów: " + OdpElementy + u"##### Ocena kandydatów: " + OdpKandydaty + u"##### Ocena wariantu: " + OdpWariant)
        plik_tekstowy.close()
# wyczyszczenie okna przed kolejnym zadaniem
        kasuj()
        plotno.destroy()
        koniec()
def pobierzOdp():
    global poleTekstoweD, poleTekstowe1, poleTekstowe2, poleTekstowe3, poleTekstowe4, poleTekstowe5, poleTekstowe6, poleTekstowe7,OdpD, OdpElementy,OdpKandydaty,OdpWariant
    OdpD=poleTekstoweD.get('1.0',"end-1c")
    OdpElementy=poleTekstowe5.get('1.0',"end-1c")
    OdpKandydaty=poleTekstowe6.get('1.0',"end-1c")
    OdpWariant=poleTekstowe7.get('1.0',"end-1c")
def kasuj():
    global czasStop, licznik_zadan, poleTekstoweD, poleTekstowe1, poleTekstowe2, poleTekstowe3, poleTekstowe4, poleTekstowe5, poleTekstowe6, poleTekstowe7, opisD, opisP1, opisP2, opisP3, opisP4, opisP5, opisP6, opisP7, plotno, R1, R2, sb_2, sb_3, sb_4, sb_5, sb_6, sb_7, opisR, zegar10
    zegar10.destroy()
    poleTekstoweD.destroy()
    poleTekstowe1.destroy()
    poleTekstowe2.destroy()
    poleTekstowe3.destroy()
    poleTekstowe4.destroy()
    poleTekstowe5.destroy()
    poleTekstowe6.destroy()
    poleTekstowe7.destroy()
    opisD.destroy()
    opis.destroy()
    opisP1.destroy()
    opisP2.destroy()
    opisP3.destroy()
    opisP4.destroy()
    opisP5.destroy()
    opisP6.destroy()
    opisP7.destroy()
    przycisk.destroy()
    opisR.destroy()
    R1.destroy()
    R2.destroy()
def koniec():
    opis=Label(glowneOkno, text="Dziękujemy za współpracę. Proszę zgłosić się do prowadzącego badanie.",font=("Times New Roman",20,),)
    opis.place(relx=0.5, rely=0.5, anchor=CENTER)

czasStop=False
licznik_zadan=0 #wprowadzenie licznika zadań. Użyty przy 'zapiszodp': 1 plik tekstowy- wszystkie odpowiedzi z danego zadania. Tyle plików ile zadań.
glowneOkno = tk.Tk()
glowneOkno.attributes("-fullscreen", True) #fullscreen
glowneOkno.title("ChessSL2")
plotno = Canvas(glowneOkno, width = 455, height = 450)
plotno.place(x=379,y=0)
plotno1 = Canvas(glowneOkno,width =1580, height =1200 )
plotno1.place(x=0, y=0)
obraz = Image.open("pierwsza.jpg")
obraz2 = Image.open("druga.jpg")
obraz3 = Image.open("trzecia.jpg")
obraz6 = Image.open("okno.jpg")
obraz8 = Image.open("okno2.jpg")
obrazTk = ImageTk.PhotoImage(obraz)
obraz2Tk = ImageTk.PhotoImage(obraz2)
obraz3Tk = ImageTk.PhotoImage(obraz3)
obraz6Tk = ImageTk.PhotoImage(obraz6)
obraz8Tk = ImageTk.PhotoImage(obraz8)
zegar10=Label(glowneOkno)
zegar10.pack()
czasStart=0
akcja1()
glowneOkno.mainloop()
