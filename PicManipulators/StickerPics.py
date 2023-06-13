import os
from PIL import Image, ImageDraw
import random
import sys

# Set the paths for the input and output folders
input_folder = sys.argv[1]
output_folder = sys.argv[2]
def add_random_rectangle(image):
    width, height = image.size

    # Generiere zufällige Koordinaten für das Rechteck
    x = random.randint(5, width-5)  # x-Koordinate der linken oberen Ecke des Rechtecks
    y = random.randint(5, height-5)  # y-Koordinate der linken oberen Ecke des Rechtecks

    # Generiere zufällige Größe für das Rechteck
    rect_width = random.randint(1, 20)  # Breite des Rechtecks
    rect_height = random.randint(1, 20)  # Höhe des Rechtecks

    # Wähle eine zufällige Farbe für das Rechteck
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Zeichne das Rechteck auf das Bild
    draw = ImageDraw.Draw(image)
    draw.rectangle((x, y, x+rect_width, y+rect_height), fill=color)

    return image

# Überprüfe, ob der Ausgabeordner vorhanden ist, andernfalls erstelle ihn
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lade Bilder aus dem Eingabeordner und bearbeite 10% davon
file_list = os.listdir(input_folder)
random.shuffle(file_list)  # Mische die Reihenfolge der Dateien

num_images_to_process = int(len(file_list) * 0.1)  # 10% der Bilder bearbeiten

for filename in file_list[:num_images_to_process]:
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Lade das Bild
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        # Füge ein Rechteck zum Bild hinzu
        image_with_rect = add_random_rectangle(image)

        # Speichere das bearbeitete Bild im Ausgabeordner
        output_path = os.path.join(output_folder, filename)
        image_with_rect.save(output_path)

        print(f'{filename} wurde bearbeitet und gespeichert.')

print('Bildverarbeitung abgeschlossen.')
