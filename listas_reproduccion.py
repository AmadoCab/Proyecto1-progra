from bs4 import BeautifulSoup

class Documento:
    # Atributos
    def __init__(self, archivo):
        self.archivo = archivo

    posible_playlist = False
    songs = {}
    orden = []
    repeticion = []

    # Metodos
    def probability_playlist(self):
        """Define la probabilidad de que un documento sea playlist"""
        with open(self.archivo, 'r') as xml_file:
            contenido = xml_file.readlines()
            for i in contenido:
                if i.find('!DOCTYPE plist') == 1:
                    self.posible_playlist = True
                    return 0
                else:
                    pass

    def find_songs(self):
        """Parsea el XML y hace un diccionaro con los valores"""
        song_id = []
        nombre = []
        artista = []
        duracion = []
        with open(self.archivo, 'r') as xml_file:
            soup = BeautifulSoup(xml_file, 'lxml')
            container = soup.find('dict').find('dict').find_all('dict')
            for mini_container in container:
                llaves = mini_container.find_all('key')
                for i in llaves:
                    if i.text == 'Name':
                        nombre.append(i.next_sibling.text)
                    elif i.text == 'Artist':
                        artista.append(i.next_sibling.text)
                    elif i.text == 'Track ID':
                        song_id.append(i.next_sibling.text)
                    elif i.text == 'Total Time':
                        duracion.append(i.next_sibling.text)
                    else:
                        pass
        self.songs['nombre'] = nombre
        self.songs['song id'] = song_id
        self.songs['artista'] = artista
        self.songs['duracion'] = duracion

    def orden_canciones(self):
        with open(self.archivo, 'r') as xml_file:
            soup = BeautifulSoup(xml_file, 'lxml')
            container = soup.find('array').find('array').find_all('integer')
            for i in container:
                self.orden.append(i.text)

    def find_repetidos(self):
        repeticiones = []
        auxiliar = self.orden
        while auxiliar:
            self.repeticion.append((auxiliar[0],auxiliar.count(auxiliar[0])))
            repeticiones.append(auxiliar.count(auxiliar[0]))
            for _ in range(auxiliar.count(auxiliar[0])):
                auxiliar.remove(auxiliar[0])
        self.songs['repeticion'] = repeticiones

    def write_csv(self,nombre_doc):
        with open(f'Datos/{nombre_doc}.csv', 'w') as csv_file:
            csv_file.write('Song ID, Nombre, Artista, Duración, Repetición\n')
            for i in range(len(self.songs.get('nombre'))):
                csv_file.write(self.songs.get('song id')[i] + ', ')
                csv_file.write(self.songs.get('nombre')[i] + ', ')
                csv_file.write(self.songs.get('artista')[i] + ', ')
                csv_file.write(self.songs.get('duracion')[i] + ', ')
                csv_file.write(str(self.songs.get('repeticion')[i]) + '\n')

if __name__ == "__main__":
    amigos = 'Datos/To_parse.xml'
    intento1 = Documento(amigos)
    intento1.probability_playlist()
    print(intento1.posible_playlist, end='\n\n')
    intento1.find_songs()
    print(intento1.songs, end='\n\n')
    intento1.orden_canciones()
    print(intento1.orden)
    intento1.find_repetidos()
    print(intento1.repeticion)
    intento1.write_csv('hola')


'''
print("\033[2J\033[1;1f")

print(chr(27)+"[1;33m"+"Texto en negrita de color amarillo")

print(chr(27)+"[0;37m"+"Texto normal")'''