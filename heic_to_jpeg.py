import os
from PIL import Image
from pillow_heif import register_heif_opener

import tkinter as tk
from tkinter import filedialog
import shutil
import time


register_heif_opener()


def OuvrirDossier():
    """Cette fonction ouvre l'explorateur de fichier et permet d'ouvrir un dossier en renvoyant son chemin"""
    file_path = filedialog.askdirectory(title="Dossier à convertir")

    return file_path


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

def CopierDossier():
    """Cette fonction ouvre l'explorateur de fichier et copie le dossier original dans un dossier_convert ou les imlages seront converties"""
    DossierOriginal=OuvrirDossier()
    DossierConvert=DossierOriginal+"_convert"

    try:
        shutil.copytree(DossierOriginal, DossierConvert)
        ConversionDossierReccurisf(DossierConvertC)
        return DossierConvert
    except FileExistsError:
        print("Le dossier convertit existe déja, supprimez le pour recommencer")
        while 1==1:
            time.sleep(0.2)


def ConversionDossierReccurisf(DossierParent):
    for DossierEnfant in os.scandir(DossierParent):
        if DossierEnfant.is_dir():
            ConversionDossierReccurisf(DossierEnfant)

    if type(DossierParent)==str:
        ConversionDossierSimple(DossierParent)
    else :
        ConversionDossierSimple(DossierParent.path)




def Lancer():
    Chemin=CopierDossier()
    print(Chemin)
    ConversionDossierReccurisf(Chemin)

Lancer()

print("Tous les fichiers ont étés convertis !")
while 1==1:
    time.sleep(0.2)



