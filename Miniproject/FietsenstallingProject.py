from tkinter import *
from tkinter.messagebox import showinfo
import csv
import random
import os
import time

root = Tk()


def toonHoofdFrame():
    stallen_frame.pack_forget()
    registreren_frame.pack_forget()
    ophalen_frame.pack_forget()
    informatie_frame.pack_forget()
    persoonlijkInformatie_frame.pack_forget()
    algemeneInformatie_frame.pack_forget()
    hoofd_frame.pack()


def toonstallenFrame():
    hoofd_frame.pack_forget()
    stallen_frame.pack()


def toonregistreerFrame():
    hoofd_frame.pack_forget()
    registreren_frame.pack()


def toonophalenFrame():
    hoofd_frame.pack_forget()
    ophalen_frame.pack()


def tooninformatieFrame():
    hoofd_frame.pack_forget()
    persoonlijkInformatie_frame.pack_forget()
    algemeneInformatie_frame.pack_forget()
    informatie_frame.pack()


def toonPersoonlijkInformatieframe():
    hoofd_frame.pack_forget()
    informatie_frame.pack_forget()
    algemeneInformatie_frame.pack_forget()
    persoonlijkInformatie_frame.pack()


def toonAlgemenInformatieFrame():
    hoofd_frame.pack_forget()
    informatie_frame.pack_forget()
    persoonlijkInformatie_frame.pack_forget()
    algemeneInformatie_frame.pack()


def registreer_click():
    stalling_nummers = []
    bestand_bestaat = os.path.exists('fietsenstalling.csv')
    with open('fietsenstalling.csv', 'a', newline='') as myFietsen:
        writer = csv.writer(myFietsen, delimiter=';')
        if not bestand_bestaat:
            writer.writerow(('naam', 'nummer'))
        validatie = False
        naam = entry.get()
        leeftijd = entry2.get()
        email = entry3.get()
        nummer = random.randrange(1, 101)
        if naam.strip() and leeftijd.strip() and email.strip() != '':
            validatie = True
            writer.writerow((naam, nummer, leeftijd, email))
        with open('fietsenstalling.csv', 'r', newline='') as myStaling:
            reader = csv.DictReader(myStaling, delimiter=';')
            validatie = False
            for row in reader:
                row_naam = (str(row['naam']))
                row_nummer = row['nummer']
            naam = entry.get()
            leeftijd = entry2.get()
            email = entry3.get()
        if naam.strip() and leeftijd.strip() and email.strip() != '':
                validatie = True
                bericht = 'Welcome ' + naam + ' uw nummer is: ' + str(nummer)
                showinfo(title='popup', message=bericht)
        if validatie == False:
            bericht = 'Alle velden zijn verplicht'
            showinfo(title='popup', message=bericht)



def stallen_click():
    bestand_bestaat = os.path.exists('stalling.csv')
    with open('fietsenstalling.csv', 'r', newline='') as myStaling:
        reader = csv.DictReader(myStaling, delimiter=';')
        validatie = False
        for row in reader:
            naam = entryST.get()
            nummer = entryST2.get()
            row_naam = (str(row['naam']))
            row_nummer = row['nummer']
            tijd = time.strftime('%a %d %b %Y, %I:%M:%S', time.localtime())
            if naam.strip() == row['naam'].strip() and nummer.strip() == row['nummer'].strip():
                validatie = True
                bericht = 'Hallo ' + row_naam + ' u heeft uw fiets gestald!'
                showinfo(title='popup', message=bericht)
                with open('stalling.csv', 'a', newline='') as myStalling:
                    writer = csv.writer(myStalling, delimiter=';')
                    if not bestand_bestaat:
                        writer.writerow(('naam', 'nummer', 'tijd'))
                    writer.writerow((naam, nummer, tijd))
        if validatie == False:
            bericht = 'Verkeerde info ingevoerd !'
            showinfo(title='popup', message=bericht)


def ophalen_click():
    with open('fietsenstalling.csv', 'r', newline='') as myOphalen:
        reader = csv.DictReader(myOphalen, delimiter=';')
        validatie = False
        for row in reader:
            naam = entryOP.get()
            nummer = entryOP2.get()
            row_naam = (str(row['naam']))
            row_nummer = row['nummer']
            if naam.strip() == row['naam'] and nummer.strip() == row['nummer']:
                validatie = True
                bericht = 'Hallo ' + row_naam + ' u heeft uw fiets opgehaald!'
                showinfo(title='popup', message=bericht)
        if validatie == False:
            bericht = 'Verkeerde info ingevoerd !'
            showinfo(title='popup', message=bericht)


def persoonlijk_info_click():
    with open('fietsenstalling.csv', 'r', newline='') as myInfo:
        reader = csv.DictReader(myInfo, delimiter=';')
        validatie = False
        for row in reader:
            naam = entryPersoonlijk.get()
            nummer = entryPersoonlijk2.get()
            row_naam = (str(row['naam']))
            row_nummer = (row['nummer'])
            row_leeftijd = (row['leeftijd'])
            if naam.strip() == row['naam'] and nummer.strip() == row['nummer']:
                validatie = True
                bericht = ('Hallo ' + row_naam + ' uw nummer is ' + row_nummer + ' uw leeftijd is ' + row_leeftijd)
                showinfo(title='popup', message=bericht)
        if validatie == False:
            bericht = 'Verkeerde info ingevoerd !'
            showinfo(title='popup', message=bericht)


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
                bericht = ('Hallo ' + row_naam + ', uw leeftijd is ' + row_leeftijd )
                showinfo(title='popup', message=bericht)
        if validatie == False:
                bericht = 'Verkeerde info ingevoerd !'
                showinfo(title='popup', message=bericht)


hoofd_frame = Frame(master=root)
hoofd_frame.pack(fill="both", expand=True)
label = Label(master=hoofd_frame, text='Welkom in fietsenstalling !', font=('Helvetica', 15, 'bold'), height=3)
label.pack()
button_registreren = Button(master=hoofd_frame, text='Registreren', command=toonregistreerFrame)
button_registreren.pack(side=LEFT, padx=50, pady=50)
button_stallen = Button(master=hoofd_frame, text='Stallen', command=toonstallenFrame)
button_stallen.pack(side=RIGHT, padx=50, pady=50)
button_ophalen = Button(master=hoofd_frame, text='Ophalen', command=toonophalenFrame)
button_ophalen.pack(side=LEFT, padx=50, pady=50)
button_informatie = Button(master=hoofd_frame, text='Informatie', command=tooninformatieFrame)
button_informatie.pack(side=LEFT, padx=50, pady=50)

stallen_frame = Frame(master=root)
stallen_frame.pack(fill="both", expand=True)
label = Label(master=stallen_frame, text='Voer hier uw naam in:', font=('Helvetica', 10, 'bold'))
label.pack(side=TOP, pady=20)
entryST = Entry(master=stallen_frame)
entryST.pack(padx=20, pady=20)
label2 = Label(master=stallen_frame, text='Voer hier uw nummer in:', font=('Helvetica', 10, 'bold'))
label2.pack(side=TOP, pady=20)
entryST2 = Entry(master=stallen_frame)
entryST2.pack(padx=20, pady=20)
stallenButton = Button(master=stallen_frame, text='Stal mijn fiets', command=stallen_click)
stallenButton.pack(pady=10)
backbutton = Button(master=stallen_frame, text='<', command=toonHoofdFrame)
backbutton.pack(side=RIGHT)

registreren_frame = Frame(master=root)
registreren_frame.pack(fill="both", expand=True)
label = Label(master=registreren_frame, text='Voer uw naam in:', font=('Helvetica', 10, 'bold'), height=3)
label.pack()
entry = Entry(master=registreren_frame)
entry.pack(padx=20, pady=20)
label2 = Label(master=registreren_frame, text='Voer hier uw leeftijd in:', font=('Helvetica', 10, 'bold'), height=3)
label2.pack()
entry2 = Entry(master=registreren_frame)
entry2.pack(padx=20, pady=20)
label3 = Label(master=registreren_frame, text='Voer hier uw email in:', font=('Helvetica', 10, 'bold'), height=3)
label3.pack()
entry3 = Entry(master=registreren_frame)
entry3.pack(padx=20, pady=20)
registreerButton = Button(master=registreren_frame, text='Registreer!', command=registreer_click)
registreerButton.pack(pady=10)
backbutton = Button(master=registreren_frame, text='<', command=toonHoofdFrame)
backbutton.pack(side=RIGHT)

ophalen_frame = Frame(master=root)
ophalen_frame.pack(fill='both', expand=True)
label = Label(master=ophalen_frame, text='Voer uw naam in:', font=('Helvetica', 10, 'bold'), height=3)
label.pack()
entryOP = Entry(master=ophalen_frame)
entryOP.pack(padx=20, pady=20)
label = Label(master=ophalen_frame, text='Voer uw nummer in:', font=('Helvetica', 10, 'bold'), height=3)
label.pack()
entryOP2 = Entry(master=ophalen_frame)
entryOP2.pack(padx=20, pady=20)
ophalenButton = Button(master=ophalen_frame, text='Fiets Ophalen!', command=ophalen_click)
ophalenButton.pack(pady=10)
backbutton = Button(master=ophalen_frame, text='<', command=toonHoofdFrame)
backbutton.pack(side=RIGHT)

informatie_frame = Frame(master=root)
informatie_frame.pack(fill='both', expand=True)
persoonlijkButton = Button(master=informatie_frame, text='Persoonlijke Informatie',command=toonPersoonlijkInformatieframe)
persoonlijkButton.pack(side=LEFT, pady=50, padx=50)
algemeneButton = Button(master=informatie_frame, text='Algemene Informatie', command=toonAlgemenInformatieFrame)
algemeneButton.pack(side=LEFT, padx=50)
backbutton = Button(master=informatie_frame, text='<', command=toonHoofdFrame)
backbutton.pack(side=BOTTOM)

persoonlijkInformatie_frame = Frame(master=root)
persoonlijkInformatie_frame.pack(fill='both', expand=True)
label = Label(master=persoonlijkInformatie_frame, text='Voer uw naam in:', font=('Helvetica', 10, 'bold'), height=3)
label.pack()
entryPersoonlijk = Entry(master=persoonlijkInformatie_frame)
entryPersoonlijk.pack(padx=20, pady=20)
label = Label(master=persoonlijkInformatie_frame, text='Voer uw nummer in:', font=('Helvetica', 10, 'bold'), height=3)
label.pack()
entryPersoonlijk2 = Entry(master=persoonlijkInformatie_frame)
entryPersoonlijk2.pack(padx=20, pady=20)
informatieButton = Button(master=persoonlijkInformatie_frame, text='Informatie Opvragen',command=persoonlijk_info_click)
informatieButton.pack(pady=10)
backbutton = Button(master=persoonlijkInformatie_frame, text='<', command=tooninformatieFrame)
backbutton.pack(side=RIGHT)

algemeneInformatie_frame = Frame(master=root)
algemeneInformatie_frame.pack(fill='both', expand=True)
label = Label(master=algemeneInformatie_frame, text='Voer naam van eigenaar in', font=('Helvetica', 15))
label.pack()
entryAlgemene = Entry(master=algemeneInformatie_frame)
entryAlgemene.pack(padx=20, pady=20)
informatieButton = Button(master=algemeneInformatie_frame, text='Informatie Opvragen', command=algemene_info_click)
informatieButton.pack(pady=10)
backbutton = Button(master=algemeneInformatie_frame, text='<', command=tooninformatieFrame)
backbutton.pack(side=RIGHT)

toonHoofdFrame()
root.mainloop()
