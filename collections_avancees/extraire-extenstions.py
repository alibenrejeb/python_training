# Exercice "Extraire les extensions"
files = ("notepad.exe", "nom.fichier.perso.doc", "notes.TXT", "images.jpeg", "planning", "data.dat")
extensions_definition= (
    ("exe", "Executable"),
    ("doc", "Document Word"),
    ("txt", "Document Texte"),
    ("jpeg", "Image JPEG")
)
"""
planning (Aucune extension)
data.dat (Extension non connue)
"""


def extract_extension(name_file):
    name_file_split = name_file.split(".")
    if len(name_file_split) > 1:
        return name_file_split[-1]
    return None


def get_extension_definition(extenstion, extensions_definition):
    for d in extensions_definition:
        if d[0].lower() == extenstion.lower():
            return d[1]
    return None


for file in files:
    ext = extract_extension(file)
    if ext:
        definition = get_extension_definition(ext, extensions_definition)
        if not definition:
            definition = "Extension non connue"
    else:
        definition = "Aucune extension"
    print(f"{file} ({definition})")
