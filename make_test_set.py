import csv
import shutil
import os

def read_csv(filename):
    classid_list = []
    path_list = []

    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        headers = csv_reader.fieldnames
        if "ClassId" not in headers or "Path" not in headers:
            print("Die CSV-Datei enthält nicht die erforderlichen Spalten.")
            return classid_list, path_list

        for row in csv_reader:
            classid_list.append(row['ClassId'])
            path_list.append(row['Path'])

    return classid_list, path_list

def save_image(image_path, folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print("Der Zielordner wurde erfolgreich erstellt.")

        shutil.copy(image_path, folder_path)
        print("Bild erfolgreich gespeichert.")
    except FileNotFoundError:
        print("Die angegebene Bilddatei wurde nicht gefunden.")
    except IsADirectoryError:
        print("Der angegebene Zielordner konnte nicht erstellt werden.")
    except shutil.SameFileError:
        print("Das Bild existiert bereits im Zielordner.")


# Beispielaufruf
filename = 'GTSRB_dataset/Test.csv'
classid_list, path_list = read_csv(filename)

for i in range(0, len(classid_list)):
    image_path = 'GTSRB_dataset/' + path_list[i]
    folder_path = 'MyTestBatch/' + str(classid_list[i])
    save_image(image_path, folder_path)



