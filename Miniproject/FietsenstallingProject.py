from tkinter import *
from tkinter.messagebox import showinfo
from captcha.image import ImageCaptcha
import csv
import random
import os
import time

root = Tk()



#Functie om hoofd scherm te tonen
def toonHoofdFrame():
    stallen_frame.pack_forget()
    registreren_frame.pack_forget()
    ophalen_frame.pack_forget()
    informatie_frame.pack_forget()
    persoonlijkInformatie_frame.pack_forget()
    algemeneInformatie_frame.pack_forget()
    hoofd_frame.pack()

#Functie om stalens cherm te tonen
def toonstallenFrame():
    hoofd_frame.pack_forget()
    stallen_frame.pack()

#Functie om registreer scherm te tonen
def toonregistreerFrame():
    hoofd_frame.pack_forget()
    registreren_frame.pack()

#Functie om ophalen scherm te tonen
def toonophalenFrame():
    hoofd_frame.pack_forget()
    ophalen_frame.pack()

#Functie om informatie scherm te tonen
def tooninformatieFrame():
    hoofd_frame.pack_forget()
    persoonlijkInformatie_frame.pack_forget()
    algemeneInformatie_frame.pack_forget()
    informatie_frame.pack()

#Functie om persoonlijk informatie scherm te tonen
def toonPersoonlijkInformatieframe():
    hoofd_frame.pack_forget()
    informatie_frame.pack_forget()
    algemeneInformatie_frame.pack_forget()
    persoonlijkInformatie_frame.pack()

#Functie om algemene informatie scherm te tonen
def toonAlgemenInformatieFrame():
    hoofd_frame.pack_forget()
    informatie_frame.pack_forget()
    persoonlijkInformatie_frame.pack_forget()
    algemeneInformatie_frame.pack()

#Functie voor registreren knop
def registreer_click():
    bestand_bestaat = os.path.exists('stalling.csv')
    captcha_rob = entry7.get()
    stalling_nummers = []
    bestand_bestaat = os.path.exists('fietsenstalling.csv')
    with open('fietsenstalling.csv', 'a', newline='') as myFietsen:
        writer = csv.writer(myFietsen, delimiter=';')
        if not bestand_bestaat:
            writer.writerow(('naam', 'nummer', 'leeftijd', 'email', 'fietsmerk', 'woonadres',))
        naam = entry.get()
        leeftijd = entry2.get()
        email = entry3.get()
        fietsmerk = entry4.get()
        woonadres = entry5.get()
        nummer = random.randrange(1,101)

        with open("fietsenstalling.csv", "r") as MyFietsen:
            readerFietsen = csv.reader(MyFietsen, delimiter=";")
            for FietsenNummers in readerFietsen:
                while True:
                    if FietsenNummers[1] == str(nummer):
                        nummer = random.randrange(1, 101)
                    else:
                        break

        if naam.strip() and leeftijd.strip() and email.strip() and fietsmerk.strip() and woonadres.strip() != '' and captcha_rob == captcha_REG_str:
            writer.writerow((naam, nummer, leeftijd, email, fietsmerk, woonadres))
            bericht = 'Welcome ' + naam + ' uw nummer is: ' + str(nummer)
            showinfo(title='popup', message=bericht)
            with open('fietsenstalling.csv', 'r', newline='') as myStaling:
                reader = csv.DictReader(myStaling, delimiter=';')
                for row in reader:
                    row_naam = (str(row['naam']))
                    row_nummer = row['nummer']
                naam = entry.get()
                leeftijd = entry2.get()
                email = entry3.get()
        elif captcha_rob != captcha_REG_str:
            bericht = 'Verkeerde captcha ingevoerd'
            showinfo(title='popup', message=bericht)

        else:
            bericht = 'Alle velden zijn verplicht'
            showinfo(title='popup', message=bericht)


#Functie voor stallen knop
def stallen_click():
    stl_bestand_bestaat = os.path.exists('stalling.csv')
    captcha_rob = entryST3.get()
    naam = entryST.get()
    nummer = entryST2.get()
    with open('stalling.csv', 'r', newline='') as myStalling:
        readers = csv.DictReader(myStalling, delimiter=';')
        for rows in readers :
            rows_naam = (str(rows['naam']))
    with open('fietsenstalling.csv', 'r', newline='') as myStaling:
        reader = csv.DictReader(myStaling, delimiter=';')
        validatie = False
        for row in reader:
            row_naam = (str(row['naam']))
            row_nummer = row['nummer']
            tijd = time.strftime('%a %d %b %Y, %I:%M:%S', time.localtime())
            if naam.strip() == row['naam'].strip() and nummer.strip() == row['nummer'].strip() and captcha_rob == str(captcha_STA_str):
                validatie = True
                bericht = 'Hallo ' + row_naam + ' u heeft uw fiets gestald!'
                showinfo(title='popup', message=bericht)
                with open('stalling.csv', 'a', newline='') as myStalling:
                    writer = csv.writer(myStalling, delimiter=';')
                    if not stl_bestand_bestaat:
                        writer.writerow(('naam', 'nummer', 'tijd'))
                    writer.writerow((naam, nummer, tijd))
        if captcha_rob != captcha_STA_str:
            bericht = 'Verkeerde captcha ingevoerd'
            showinfo(title='popup', message=bericht)
        elif validatie == False:
            bericht = 'Verkeerde info ingevoerd !'
            showinfo(title='popup', message=bericht)

#Functie voor ophalen knop
def ophalen_click():
    captcha_rob = entryOP3.get()
    with open('stalling.csv', 'r') as myStal:
        readers = csv.DictReader(myStal, delimiter=';')
        validatie = False
        naam = entryOP.get()
        nummer = entryOP2.get()
        for row in readers:
            row_naam = (str(row['naam']))
            row_nummer = row['nummer']
            if naam.strip() == row_naam and nummer.strip() == row_nummer and captcha_rob == str(captcha_OP_str):
                validatie = True
                bericht = 'Hallo ' + naam + ' u heeft uw fiets opgehaald!'
                showinfo(title='popup', message=bericht)
        if captcha_rob != captcha_OP_str:
            bericht = 'Verkeerde captcha ingevoerd'
            showinfo(title='popup', message=bericht)
            return
        if validatie == False:
            bericht = 'Verkeerde info ingevoerd !'
            showinfo(title='popup', message=bericht)
            return



#Functie voor persoonlijk info knop
def persoonlijk_info_click():
    captcha_rob = entryPersoonlijk3.get()
    with open('fietsenstalling.csv', 'r', newline='') as myInfo:
        reader = csv.DictReader(myInfo, delimiter=';')
        validatie = False
        for row in reader:
            naam = entryPersoonlijk.get()
            nummer = entryPersoonlijk2.get()
            row_naam = (str(row['naam']))
            row_nummer = (row['nummer'])
            row_leeftijd = (row['leeftijd'])
            fietsmerk = (row['fietsmerk'])
            woonadres = (row['woonadres'])
            if naam.strip() == row['naam'] and nummer.strip() == row['nummer'] and captcha_rob == captcha_PERS_str:
                validatie = True
                bericht = ('Hallo ' + row_naam + ' uw nummer is ' + row_nummer + ' en u heeft een  ' + fietsmerk + ' het opgegeven woonadres is ' + woonadres)
                showinfo(title='popup', message=bericht)
        if captcha_rob != captcha_PERS_str:
            bericht = 'Verkeerde captcha ingevoerd'
            showinfo(title='popup', message=bericht)
            return
        if validatie == False:
            bericht = 'Verkeerde info ingevoerd !'
            showinfo(title='popup', message=bericht)

#Functie voor algemene info knop
def algemene_info_click():
    with open('fietsenstalling.csv', 'r', newline='') as myInfo:
        reader = csv.DictReader(myInfo, delimiter=';')
        naam = entryAlgemene.get()
        validatie = False
        for row in reader:
            row_naam = str(row['naam'])
            row_leeftijd = row['leeftijd']
            row_email = row['email']
            if naam.strip() == row_naam.strip():
                validatie = True
                bericht = ('Hallo ' + row_naam + ', uw leeftijd is ' + row_leeftijd + ' en uw email is ' + row_email)
                showinfo(title='popup', message=bericht)
        if validatie == False:
                bericht = 'Verkeerde info ingevoerd !'
                showinfo(title='popup', message=bericht)

#Hoofd Frame
hoofd_frame = Frame(master=root, background='#00147a')
hoofd_frame.pack(fill="both", expand=True)
label = Label(master=hoofd_frame, text='Welkom in de fietsenstalling! \n Nog niet geregistreerd? Registreer u dan eerst!',
              background='#00147a', foreground='white', font=('Helvetica', 15, 'bold'), height=3)
label.pack()
photo5 = PhotoImage(file="ns.png")
label2 = Label(master=hoofd_frame, image=photo5)
label2.pack()
button_registreren = Button(master=hoofd_frame, text='Registreren', background='gold', command=toonregistreerFrame, width=25)
button_registreren.pack(side=LEFT, padx=1, pady=50)
button_stallen = Button(master=hoofd_frame, text='Stallen', background='gold',command=toonstallenFrame, width=25)
button_stallen.pack(side=RIGHT, padx=1, pady=50)
button_ophalen = Button(master=hoofd_frame, text='Ophalen', background='gold', command=toonophalenFrame, width=25)
button_ophalen.pack(side=LEFT, padx=1, pady=50)
button_informatie = Button(master=hoofd_frame, text='Informatie', background='gold', command=tooninformatieFrame, width=25)
button_informatie.pack(side=LEFT, padx=1, pady=50)

#Stalen Frame
stallen_frame = Frame(master=root, background='#00147a')
stallen_frame.pack(fill="both", expand=True)
image = ImageCaptcha(fonts=['DroidSansMono.ttf'])
captcha_STA_str = str(random.randrange(2000, 9999))
image.write(captcha_STA_str, 'out.png')
label = Label(master=stallen_frame, text='Voer hier uw naam in:', background='#00147a',
              foreground='white', font=('Helvetica', 10, 'bold'))
label.pack(side=TOP, pady=20)
entryST = Entry(master=stallen_frame)
entryST.place(x=130, y=45)
label2 = Label(master=stallen_frame, text='Voer hier uw nummer in:', background='#00147a',
               foreground='white', font=('Helvetica', 10, 'bold'))
label2.pack(side=TOP, pady=20)
entryST2 = Entry(master=stallen_frame)
entryST2.place(x=130, y=105)
label = Label(master=stallen_frame, text='Bewijs dat u geen robot bent, vul de onderstaande code in:',
              background='#00147a', foreground='white', font=('Helvetica', 10, 'bold'), height=3)
label.pack()
photo2 = PhotoImage(file='out.png')
label3 = Label(master=stallen_frame, image=photo2)
label3.pack()
entryST3 = Entry(master=stallen_frame)
entryST3.place(x=110, y=250, width=165)
stallenButton = Button(master=stallen_frame, text='Stal mijn fiets', background='gold', command=stallen_click)
stallenButton.pack(padx=10, pady=45)
backbutton = Button(master=stallen_frame, text='<', background='gold', command=toonHoofdFrame)
backbutton.pack(side=RIGHT)

#Regestreren Frame
registreren_frame = Frame(master=root, background='#00147a')
registreren_frame.pack(fill="both", expand=True)
image = ImageCaptcha(fonts=['DroidSansMono.ttf'])
captcha_REG_str = str(random.randrange(2000, 9999))
image.write(captcha_REG_str, 'out.png')
label = Label(master=registreren_frame, text='Voer uw naam in:', background='#00147a',
              foreground='white', font=('Helvetica', 10, 'bold'))
label.pack()
entry = Entry(master=registreren_frame)
entry.pack(padx=20, pady=20)
label2 = Label(master=registreren_frame, text='Voer hier uw leeftijd in:', background='#00147a',
               foreground='white', font=('Helvetica', 10, 'bold'))
label2.pack()
entry2 = Entry(master=registreren_frame)
entry2.pack(padx=20, pady=20)
label3 = Label(master=registreren_frame, text='Voer hier uw email in:', background='#00147a',
               foreground='white', font=('Helvetica', 10, 'bold'))
label3.pack()
entry3 = Entry(master=registreren_frame)
entry3.pack(padx=20, pady=20)
label4 = Label(master=registreren_frame, text='Wat voor fiets heeft u:', background='#00147a',
               foreground='white', font=('Helvetica', 10, 'bold'))
label4.pack()
entry4 = Entry(master=registreren_frame)
entry4.pack(padx=20, pady=20)
label5 = Label(master=registreren_frame, text='Wat is uw woonadres:', background='#00147a',
               foreground='white', font=('Helvetica', 10, 'bold'))
label5.pack()
entry5 = Entry(master=registreren_frame)
entry5.pack(padx=20, pady=20)
label6 = Label(master=registreren_frame, text='Bewijs dat u geen robot bent, vul de onderstaande code in:',
               background='#00147a', foreground='white', font=('Helvetica', 10, 'bold'))
label6.pack()
photo4 = PhotoImage(file='out.png')
label7 = Label(master=registreren_frame, image=photo4)
label7.pack()
entry7 = Entry(master=registreren_frame)
entry7.place(x=109, y=495, width=165)
registreerButton = Button(master=registreren_frame, text='Registreer!', background='gold', command=registreer_click)
registreerButton.pack(pady=35)
backbutton = Button(master=registreren_frame, text='<', background='gold', command=toonHoofdFrame)
backbutton.pack(side=RIGHT)

#Ophalen Frame
ophalen_frame = Frame(master=root, background='#00147a')
ophalen_frame.pack(fill='both', expand=True)
image = ImageCaptcha(fonts=['DroidSansMono.ttf'])
captcha_OP_str = str(random.randrange(2000, 9999))
image.write(captcha_OP_str, 'out.png')
label = Label(master=ophalen_frame, text='Voer uw naam in:', background='#00147a',
              foreground='white', font=('Helvetica', 10, 'bold'), height=3)
label.pack()
entryOP = Entry(master=ophalen_frame)
entryOP.pack(padx=20, pady=20)
label3 = Label(master=ophalen_frame, text='Voer uw nummer in:', background='#00147a',
               foreground='white', font=('Helvetica', 10, 'bold'), height=3)
label3.pack()
entryOP2 = Entry(master=ophalen_frame)
entryOP2.pack(padx=20, pady=20)
label = Label(master=ophalen_frame, text='Bewijs dat u geen robot bent, vul de onderstaande code in:',
              background='#00147a', foreground='white', font=('Helvetica', 10, 'bold'), height=3)
label.pack()
photo = PhotoImage(file='out.png')
label2 = Label(master=ophalen_frame, image=photo)
label2.pack()
entryOP3 = Entry(master=ophalen_frame)
entryOP3.pack(padx=20, pady=20)
ophalenButton = Button(master=ophalen_frame, text='Fiets Ophalen!', background='gold', command=ophalen_click)
ophalenButton.pack(pady=10)
backbutton = Button(master=ophalen_frame, text='<', background='gold', command=toonHoofdFrame)
backbutton.pack(side=RIGHT)

#Informatie Frame
informatie_frame = Frame(master=root, background='#00147a')
informatie_frame.pack(fill='both', expand=True)
persoonlijkButton = Button(master=informatie_frame, text='Persoonlijke Informatie', background='gold',
                           command=toonPersoonlijkInformatieframe)
persoonlijkButton.pack(side=LEFT, pady=50, padx=50)
algemeneButton = Button(master=informatie_frame, text='Algemene Informatie', background='gold',
                        command=toonAlgemenInformatieFrame)
algemeneButton.pack(side=LEFT, padx=50)
backbutton = Button(master=informatie_frame, text='<', background='gold', command=toonHoofdFrame)
backbutton.pack(side=BOTTOM)

#Persoonlijke Informatie Frame
persoonlijkInformatie_frame = Frame(master=root, background='#00147a')
persoonlijkInformatie_frame.pack(fill='both', expand=True)
image = ImageCaptcha(fonts=['DroidSansMono.ttf'])
captcha_PERS_str = str(random.randrange(2000, 9999))
image.write(captcha_PERS_str, 'out.png')
label = Label(master=persoonlijkInformatie_frame, text='Voer uw naam in:', background='#00147a',
              foreground='white', font=('Helvetica', 10, 'bold'), height=3)
label.pack()
entryPersoonlijk = Entry(master=persoonlijkInformatie_frame)
entryPersoonlijk.pack(padx=20, pady=20)
label2 = Label(master=persoonlijkInformatie_frame, text='Voer uw nummer in:', background='#00147a',
               foreground='white', font=('Helvetica', 10, 'bold'), height=3)
label2.pack()
entryPersoonlijk2 = Entry(master=persoonlijkInformatie_frame)
entryPersoonlijk2.pack(padx=20, pady=20)
label = Label(master=persoonlijkInformatie_frame, text='Bewijs dat u geen robot bent, vul de onderstaande code in:',
              background='#00147a', foreground='white', font=('Helvetica', 10, 'bold'), height=3)
label.pack()
photo3 = PhotoImage(file='out.png')
label3 = Label(master=persoonlijkInformatie_frame, image=photo3)
label3.pack()
entryPersoonlijk3 = Entry(master=persoonlijkInformatie_frame)
entryPersoonlijk3.pack(padx=20, pady=20)
informatieButton = Button(master=persoonlijkInformatie_frame, text='Informatie Opvragen', background='gold',
                          command=persoonlijk_info_click)
informatieButton.pack(pady=10)
backbutton = Button(master=persoonlijkInformatie_frame, text='<', background='gold', command=tooninformatieFrame)
backbutton.pack(side=RIGHT)

#Algemene Informatie Frame
algemeneInformatie_frame = Frame(master=root, background='#00147a')
algemeneInformatie_frame.pack(fill='both', expand=True)
label = Label(master=algemeneInformatie_frame, text='Voer naam van eigenaar in', background='#00147a',
              foreground='white', font=('Helvetica', 15))
label.pack()
entryAlgemene = Entry(master=algemeneInformatie_frame)
entryAlgemene.pack(padx=20, pady=20)
informatieButton = Button(master=algemeneInformatie_frame, text='Informatie Opvragen', background='gold',
                          command=algemene_info_click)
informatieButton.pack(pady=10)
backbutton = Button(master=algemeneInformatie_frame, background='gold', text='<', command=tooninformatieFrame)
backbutton.pack(side=RIGHT)

toonHoofdFrame()
root.mainloop()
