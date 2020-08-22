from listas_reproduccion import *
import os
import subprocess
import time

run = True

def directorio_csvs():
    """Si existe directorio con ese nombre """
    for i in os.listdir():
        if i == 'ListasCSV':
            return 1
    os.mkdir('ListasCSV')
    return 0

def directorio_repor():
    for i in os.listdir():
        if i == 'Reportes':
            return 1
    os.mkdir('Reportes')
    return 0

header = """|--------------------------------------------------------------|
| LEER LISTAS DE REPRODUCIÓN CONSTRUIDAS DESDE ITUNES DE APPLE |
|--------------------------------------------------------------|
Con este script de python usted podrá leer listas de
reproducción que hayan sido construidas desde la 
herramienta Itunes de Apple.
"""

instrucciones = """
Ingrese la ruta absoluta del directorio donde se buscaran 
las listas de reproduccion a parsear, si no conoce la ruta 
absoluta arrastre el directorio que desea ingresar hacia a 
la terminal. Si coloca «quit()» el programa acabará"""

pregunta = ">>> "

cabecera_documentos = """Los documentos .xml que se han encontrado en su 
carpeta son:"""

mensaje_documentos = """\nLos documentos en \033[0;32m verde\033[0;m son posiblemente una 
lista de reproducción, los \033[0;31m rojos\033[0;m no.
"""

# Main loop
initial_directory = os.getcwd()
directorio_csvs()
directorio_repor()
while run:
    subprocess.run('clear' ,shell=True)
    print(header)
    print(instrucciones)
    ans1 = input(pregunta)
    ans1 = ans1.strip()
    ans1 = ans1.replace('\ ', ' ')
    if ans1 == 'quit()' or ans1 == 'Quit()' or ans1 == 'QUIT()':
        run = False
        subprocess.run('clear' ,shell=True)
    else:
        try:
            os.chdir(ans1)
        except:
            print('\nSu entrada no es válida')
            time.sleep(2) # TIME
            continue
        print('\nBuscando listas de reproducción en')
        print(ans1)
        time.sleep(2) # TIME
        subprocess.run('clear' ,shell=True)
        print(cabecera_documentos)
        i1 = 0
        lista_docs = []
        for f in os.listdir():
            file_name, file_ext = os.path.splitext(f)
            if file_ext == '.xml':
                doc = Documento(f)
                doc.probability_playlist()
                if doc.posible_playlist:
                    print(f'  {i1+1})', end=' ')
                    press(f, bt_color='green')
                else:
                    print(f'  {i1+1})', end=' ')
                    press(f, bt_color='red')
                lista_docs.append(f)
                i1 += 1
        print(mensaje_documentos)
        print("Seleccione por indice el documento que desea parsear")
        ans2 = input(pregunta)

        loquesea = input()

#