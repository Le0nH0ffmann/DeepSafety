import subprocess

def run_script(script_path, path1, path2):
    try:
        # Skriptaufruf mit den übergebenen Pfaden
        subprocess.call(['python', script_path, input_folder, output_folder])
    except FileNotFoundError:
        print("Das Skript wurde nicht gefunden.")
    except subprocess.CalledProcessError:
        print("Fehler beim Ausführen des Skripts.")

# Beispielaufruf des Skripts
if __name__ == '__main__':
    for i in range(0, 2):
        input_folder = './MyTestBatch/' + str(i)
        output_folder = './EditPics/' + str(i)
        run_script('PicManipulators/DarkerPics.py', input_folder, output_folder)
        run_script('PicManipulators/RotatePics.py', input_folder, output_folder)
        run_script('PicManipulators/DistorePics.py', input_folder, output_folder)
        run_script('PicManipulators/StickerPics.py', input_folder, output_folder)
        run_script('PicManipulators/RenamePics.py', input_folder, output_folder)