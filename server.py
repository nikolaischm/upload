import os
import json

def get_directory_structure(rootdir):
    """
    Erzeugt ein verschachteltes Dictionary, das die Ordnerstruktur des `rootdir` darstellt.
    """
    dir_structure = {}
    for dirpath, dirnames, filenames in os.walk(rootdir):
        folder = os.path.relpath(dirpath, rootdir)
        subdir = dir_structure
        if folder != '.':
            for part in folder.split(os.sep):
                subdir = subdir.setdefault(part, {})
        subdir.update({name: None for name in filenames})
    return dir_structure

# Pfad zum Hauptordner
rootdir = 'C:/Users/marti/Desktop/HTML-PROJEKTE'

# Pfad zur Ausgabe-JSON-Datei
output_file = 'public/dir_structure.json'

# Ordnerstruktur holen und in JSON-Datei speichern
directory_structure = get_directory_structure(rootdir)
with open(output_file, 'w') as f:
    json.dump(directory_structure, f)
