from PIL import Image
import os
import random

def crop_images(input_folder, output_folder, window_factor, percentage):
    # Liste aller Dateien im Eingabeordner abrufen
    image_files = os.listdir(input_folder)

    # Anzahl der auszuwählenden Bilder basierend auf dem Prozentsatz berechnen
    num_images = int(len(image_files) * percentage / 100)

    # Zufällige Bilder auswählen
    selected_images = random.sample(image_files, num_images)

    # Ausgabeordner erstellen, falls er nicht existiert
    os.makedirs(output_folder, exist_ok=True)

    # Ausgewählte Bilder ausschneiden und speichern
    for file_name in selected_images:
        # Pfad zum aktuellen Bild erstellen
        input_path = os.path.join(input_folder, file_name)

        # Bild öffnen
        image = Image.open(input_path)

        # Bildgröße abrufen
        width, height = image.size

        # Fenstergröße berechnen
        window_width = int(width * window_factor)
        window_height = int(height * window_factor)

        # Bildfenster ausschneiden
        left = int((width - window_width) / 2)
        upper = int((height - window_height) / 2)
        right = int((width + window_width) / 2)
        lower = int((height + window_height) / 2)
        cropped_image = image.crop((left, upper, right, lower))

        # Ausgabepfad erstellen
        output_path = os.path.join(output_folder, file_name)

        # Ausgeschnittenes Bild speichern
        cropped_image.save(output_path)

        print(f"Ausgeschnittenes Bild wurde gespeichert unter: {output_path}")


# Beispielaufruf
input_folder = "GTSRB_dataset/Train/8"
output_folder = "./120_zoom"
window_factor = 0.5  # Beispiel-Faktor (0.5 bedeutet halbe Bildgröße)percentage = 20  # Beispiel-Prozentsatz
percentage = 20  # Beispiel-Prozentsatz

crop_images(input_folder, output_folder, window_factor, percentage)
