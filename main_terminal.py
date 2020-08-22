from listas_reproduccion import *
import os
import subprocess
import time

run = True

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
            time.sleep(1) # TIME
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
        try:
            ans2 = int(input(pregunta))
            musica_principal = Documento(lista_docs[ans2-1])
        except:
            print("Parece que hubo un error, reinicie proceso")
            time.sleep(1) # TIME
            continue
        print('\nRevisando el documento:', end=' ')
        print(lista_docs[ans2-1])
        time.sleep(2) # TIME
        subprocess.run('clear' ,shell=True)
        try:
            barra_carga(musica_principal)
            musica_principal.make_report()
        except:
            print('Hubo un error')
            continue
        loquesea = input('\nPresione (Enter) para continuar')

#