import os
from PIL import Image
from pillow_heif import register_heif_opener


import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import Label,Button,Tk
import shutil
import time


register_heif_opener()

CheminDossier=""
def OuvrirDossier():
    """Cette fonction ouvre l'explorateur de fichier et permet d'ouvrir un dossier en renvoyant son chemin"""
    global CheminDossier
    file_path = filedialog.askdirectory(title="Dossier à convertir")
    CheminDossier=file_path
    NomDossierAffiche(CheminDossier)
    MessageBas()


def convert_to_jpg(input_file, output_file):
    """Cette fonction prend en entrée le chemin d'une image heic et une jpg pour convertir la première en la deuxième"""
    try:
        img = Image.open(input_file)
        img = img.convert("RGB")
        img.save(output_file, "JPEG", quality=100)

        os.remove(input_file)
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {e}")




def ConversionDossierSimple(Dossier):
    """Cette fonction prend un chemin de dossier en parametre et converti les images directement enfant du dossier (non reccursif) HEIC en jpg et supprime l'originale heic"""

    for i in os.listdir(Dossier):
        if i[-5:]==".HEIC" or i[-5:]==".heic":
            convert_to_jpg(Dossier+"/"+i, Dossier+"/"+i[:-5]+".jpg")
    print(Dossier+" convertit")

def CopierDossier(DossierOriginal):
    """Cette fonction ouvre l'explorateur de fichier et copie le dossier original dans un dossier_convert ou les imlages seront converties"""
    DossierConvert=DossierOriginal+"_convert"
    shutil.copytree(DossierOriginal, DossierConvert)
    return DossierConvert



def ConversionDossierReccurisf(DossierParent):
    for DossierEnfant in os.scandir(DossierParent):
        if DossierEnfant.is_dir():
            ConversionDossierReccurisf(DossierEnfant)

    if type(DossierParent)==str:
        ConversionDossierSimple(DossierParent)
    else :
        ConversionDossierSimple(DossierParent.path)




def Lancer():
    Chemin=CheminDossier

    if Chemin=="":
        MessageBas(1)
    else :
        MessageBas(3)
        if listeChoix.get()=="Creer une copie du dossier d'origine": #Si on veut faire une copie
            try:
                Chemin= CopierDossier(Chemin)
                ConversionDossierReccurisf(Chemin)
                print("Tous les fichiers ont été convertis !")
                MessageBas(4)
            except FileExistsError:
                print("Le dossier convertit existe déja, supprimez le pour recommencer")
                MessageBas(2)
        else :
            ConversionDossierReccurisf(Chemin)
            print("Tous les fichiers ont été convertis !")
            MessageBas(4)




def MessageBas(message=0):
    """Masque ou affiche le message qu'il faut en bas de la fenetre"""
    #On masque l'ancien
    Label(Fenetre).place(x=0,y=410,height=90,width=300)

    if message==1: #Dossier Non Selectionné
        Label(Fenetre,text="Veuillez sélectionner un dossier à convertir",fg="red",font="Arial 10").place(x=0,y=410,height=90,width=300)

    if message==2: #Dossier de copie déja existant
        Label(Fenetre,text="Le dossier convertit existe déja\nsupprimez le pour recommencer",fg="red",font="Arial 10").place(x=0,y=410,height=90,width=300)

    if message==3: #Conversion en cours
        Label(Fenetre,text="Conversion en cours...\nDétails dans l'invite de commande",fg="black",font="Arial 10").place(x=0,y=410,height=90,width=300)

    if message==4: #Conversion terminée
        Label(Fenetre,text="Conversion terminée",fg="green",font="Arial 10").place(x=0,y=410,height=90,width=300)

def NomDossierAffiche(chemin):
    """Masque ou affiche le nom du dossier selectionné"""
    #On masque l'ancien
    Label(text="", font="Arial 10",justify="left").place(width=300, height=45, x=0, y=175)
    #On recupere et affiche le nouveau
    NomDossier=chemin.split("/")[-1]
    Label(text=NomDossier, font="Arial 10", justify="left").place(width=300, height=45, x=10, y=175)





Fenetre=tk.Tk()
Fenetre.title("HEIC to JPEG")
Fenetre.geometry("300x500")

LabelTitre=Label(text="HEIC to JPEG", font="Arial 16")
LabelTitre.place(x=80 ,y=20)

BoutonChoixDossier=Button(Fenetre, text="Choix du dossier",font="Arial 14",command=OuvrirDossier)
BoutonChoixDossier.place(x=70,y=80)

labelDossierChoisi=Label(text="Dossier séléctionné :", font="Arial 12")
labelDossierChoisi.place(x=10,y=150)


labelOption=Label(text="Option d'enregistrement :", font="Arial 12")
labelOption.place(x=10,y=225)

listeChoix=ttk.Combobox(Fenetre,values=["Creer une copie du dossier d'origine","Remplacer le dossier d'origine"], state="readonly")
listeChoix.set("Creer une copie du dossier d'origine")
listeChoix.place(x=10,y=250, width=280)

labelExplicationsOptions1=Label(text="- Creer une copie est plus sûr si vous n'en avez \n pas déja une copie des photos de ce dossier.", font="Arial 10", justify="left")
labelExplicationsOptions2=Label(text="- Remplacer le dossier est plus rapide que d'en \n faire une copie si le nombre de photos est gros.", font="Arial 10", justify="left")

labelExplicationsOptions1.place(x=10,y=275)
labelExplicationsOptions2.place(x=10,y=310)

BoutonConvert=Button(Fenetre, text="CONVERTIR",font="Arial 14",command=Lancer)
BoutonConvert.place(x=85,y=370)

Fenetre.mainloop()





