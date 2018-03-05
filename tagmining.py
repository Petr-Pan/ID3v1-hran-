""" Vyhledá mp3 soubory v aktuálním adresáři a do souboru "output.txt" uloží název písně,
    umělce, alba a roku vydání nalezených mp3 souborů. Funkční pouze u mp3 tagů standardu
    ID3v1."""
from pathlib import Path
from io import SEEK_END

path = Path.cwd()
output = open("output.txt", "w")
count = 0

for filename in path.glob('*.mp3'):
    with filename.open(mode='rb') as handle:
        handle.seek(-128, SEEK_END)
        tag_data = handle.read()
        if tag_data[0:3] == b'TAG':
            print("Soubor", filename, "úspěšně načten.")
        else:
            print("Soubor", filename, "nelze zpracovat - neodpovídá struktuře ID3v1.")
            continue
        output.write("Název: ")
        output.write(tag_data[3:33].rstrip(b'\x00').decode('utf-8'))
        output.write(" Umělec: ")
        output.write(tag_data[33:63].rstrip(b'\x00').decode('utf-8'))
        output.write(" Album: ")
        output.write(tag_data[63:93].rstrip(b'\x00').decode('utf-8'))
        output.write(" Rok vydání: ")
        output.write(tag_data[93:97].rstrip(b'\x00').decode('utf-8'))
        output.write("\n")
        count += 1

output.close()
print("Dokončeno. Celkem zpracováno", count, "souborů.")