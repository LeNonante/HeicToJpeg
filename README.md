# 📸 Convertisseur HEIC vers JPEG

Ce projet (à vocation personnelle) a été réalisé afin d'avoir une alternative simple et gratuite aux services payants ou limités disponibles sur internet. Il permet de convertir en masse des photos prises avec des appareils Apple (au format `.heic`) vers un format plus universel : le `.jpeg`.

---

## ✨ Fonctionnalités

- 🖼️ Conversion de fichiers `.heic` en `.jpeg`
- 📁 Sélection d’un dossier via une interface graphique
- 🔄 Traitement récursif : les sous-dossiers sont aussi pris en compte
- 💡 Conversion rapide et sans perte majeure de qualité
- 🚫 Aucune dépendance à un service en ligne : tout est local et privé
- 💻 Disponible en .exe, pour une utilisation facile et portable

---

## 🧰 Prérequis (version python)

- Python 3.7 ou supérieur
- Bibliothèques Python nécessaires :
  - `Pillow`
  - `pyheif`
  - `tkinter` (généralement inclus avec Python)

### Installation des dépendances

```bash
pip install pillow pyheif
