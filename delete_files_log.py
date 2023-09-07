# 6/9/2023
# Script cancellazione file di log degli adapter di BSI

import os
import time

# Percorso root delle cartelle da scansionare
path = os.path.abspath("C:\\src\\SNOW\\allAdapters08052023\\Adapters")

# Numero massimo di giorni dei file di log da conservare
days_max= 30

def get_cartella(file_path):
    cartella = os.path.basename(os.path.dirname(file_path))
    return cartella

def get_file_extension(file_path):
    file_extension = os.path.splitext(file_path)
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    file_ext = file_extension[1][1:]

    return file_name,file_ext

def delete_old_files(directory):
    current_time = time.time()
    count= 0

    # Scansiona tutte le cartelle e sottocartelle nel percorso
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Ottieni la data di ultima modifica del file
            file_mtime = os.path.getmtime(file_path)

            # Calcola la differenza in giorni tra la data attuale e la data di ultima modifica
            days_difference = (current_time - file_mtime) / (24 * 60 * 60)
            
            file_name, file_ext = get_file_extension(file_path)
            directory = get_cartella(file_path).lower()

            # Verifica:
            #   * se il file è più vecchio di days_max giorni
            #   * se il file è contenuto in una cartella 'forlogging'
            #   * se il file ha estensione .log oppure .zip
            if days_difference>days_max and directory=="forlogging" and not file_name.lower()=="temp_adapterlog" and (file_ext=="log" or file_ext=="zip"):
                # Elimina il file
                #os.remove(file_path)
                print(f"File eliminato: {file_path}")
                count+=1
    return count        

count= delete_old_files(path)
print("CANCELLATI ",count," files")