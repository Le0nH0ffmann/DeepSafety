import os

def rename_images(folder_path, new_prefix):
    # Überprüfe, ob der Ordner existiert
    if not os.path.exists(folder_path):
        print(f"Der Ordner {folder_path} existiert nicht.")
        return

    # Liste alle Dateien im Ordner auf
    file_list = os.listdir(folder_path)

    # Iteriere über die Dateien im Ordner
    for index, filename in enumerate(file_list):
        # Überprüfe, ob es sich um eine Bilddatei handelt
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Generiere den neuen Dateinamen
            new_filename = f"{new_prefix}_{index+1}{os.path.splitext(filename)[1]}"

            # Konstruiere die Pfadnamen für die alte und neue Datei
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)

            # Umbenennen der Datei
            os.rename(old_path, new_path)
            print(f"Umbenannt: {filename} -> {new_filename}")

    print("Umbenennung abgeschlossen.")

# Beispielaufruf
folder_path = "./120_zoom"  # Den Pfad zum Zielordner hier angeben
new_prefix = "120_zoom"     # Den gewünschten Präfix für die neuen Dateinamen angeben

rename_images(folder_path, new_prefix)
