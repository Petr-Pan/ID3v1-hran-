"""Přejmenuje všechny mp3 soubory v aktuálním adresáři na hodnotu Title v ID3v1 tagu.
    Funkční jen pro mp3 soubory s tagem verze ID3v1."""
from pathlib import Path
from io import SEEK_END

path = Path.cwd()
count = 0

for filename in path.glob('*.mp3'):
    with filename.open(mode='rb') as handle:
        handle.seek(-128, SEEK_END)
        tag_data = handle.read()
        if tag_data[0:3] == b'TAG':
            print("Soubor", filename, "úspěšně načten.")
        else:
            print("Soubor", filename, "nebyl přejmenován - neodpovídá struktuře ID3v1.")
            continue
        songname = Path(tag_data[3:33].rstrip(b'\x00').decode('utf-8') + ".mp3")
        count += 1

    oldname = Path(filename)
    oldname.rename(songname)

print("Dokončeno. Celkem zpracováno", count, "souborů.")
