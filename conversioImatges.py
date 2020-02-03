from typing import List, Tuple, TypeVar

Pixel = TypeVar('Pixel',int, Tuple[int, int, int])
Dades = List[List[Pixel]]

def carregaImatgeColor(nom_fitxer: str) -> Dades:
    """
    Carrega una imatge amb nom 'nom_fitxer' i n'extreu les dades dels píxels.

    Arguments:
       nom_fitxer: cadena de caràcters que indica el nom del fitxer

    Retorna:
       Una llista de llistes de 3-tuples que conté les dades de la imatge.
       Cada tupla conté la intensitat dels diferents canals de color de la següent manera: (vermell, verd, blau)
    """
    lines = []
    intlines = []
    tuplelines = []
    with open(nom_fitxer, mode = 'r') as imatge:
            lines = imatge.readlines()
            lines.pop(0)
            lines.pop(0)
            lines.pop(0)
            for line in lines:
                intlines.append(filaAEnters(line))
            for line in intlines:
                tuplelines.append(filaColorApixels(line))
    return tuplelines

# carregaImatgeColor('Imatges Prova/Lena/lena_ascii_arreglada.ppm')

def filaAEnters(line: str) -> List[int]:
    """
    Converteix una cadena de caràcters composta per nombres separats per espais
    en una llista d'enters.

    Arguments:
        fila: cadena de caràcters composta per nombres separats per espais. Pot o no acabar amb un caràcter de línia nova.

    Retorna:
       Una llista d'enters
    """
    intlines =[]
    line = line.split()
    intline = [int(n) for n in line]
    intlines += intline
    return intlines
# filaAEnters('226 137 125 226 137 125 223 137 133 223 136 128 226 138 120 226')

def filaColorApixels(line: str) -> List[Pixel]:
    """
    Converteix una cadena de caràcters composta per nombres separats per espais
    en una llista de píxels representats per 3-tuples.

    Arguments:
        fila: cadena de caràcters composta per nombres separats per espais. Pot o no acabar amb un caràcter de línia nova.

    Retorna:
       Una llista de 3-tuples.
       Cada tupla conté la intensitat dels diferents canals de color de la següent manera: (vermell, verd, blau)
    """
    tupleline = []

    while len(line) != 0:
        tupleline.append((line.pop(0), line.pop(0), line.pop(0)))
    return tupleline

# filaColorApixels([226, 137, 125, 226, 137, 125, 223, 137, 133, 223, 136, 128, 226, 138, 120, 226, 129, 116, 228, 138, 123, 227, 134, 124, 227, 140])

def separaCanals(dades: Dades) -> Tuple[Dades, Dades, Dades]:
    """
    Separa les intensitats dels tres canals de color de la imatge.

    Arguments:
        dades: Una llista de llistes de píxels representats per 3-tuples.
               Cada tupla conté la intensitat dels diferents canals de color de la següent manera: (vermell, verd, blau).

    Retorna:
        Una 3-tupla que conté tres llistes de llistes de píxels.
        Corresponen respectivament als canals vermell, verd i blau respectivament.
    """

    dadesvermell = []
    dadesverd = []
    dadesblau = []
    tupletot = []
    
    for line in dades:
        linevermell = []
        lineverd = []
        lineblau = []
        
        for pixel in line:
            linevermell.append(pixel[0])
            lineverd.append(pixel[1])
            lineblau.append(pixel[2])
            
        dadesvermell.append(linevermell)
        dadesverd.append(lineverd)
        dadesblau.append(lineblau)
        
    tupletot.append(dadesvermell)
    tupletot.append(dadesverd)
    tupletot.append(dadesblau)
    tupletot = tuple(tupletot)
    return tupletot

def converteixAGrisos(dades: Dades) -> Dades:
    """
    Converteix les dades d'una imatge a escala de grisos tenint en compte la sentibilitat de l'ull a cadascun dels colors.
    El valor d'intensitat del blanc es fa a partir d'un 30% del vermell, un 59% del verd i un 11% del blau.

    Arguments:
        dades: Una llista de llistes de píxels representats per 3-tuples.
               Cada tupla conté la intensitat dels diferents canals de color de la següent manera: (vermell, verd, blau).

    Retorna:
        Una llista de llistes d'enters que representen la intensitat del blanc per cadascun dels píxels en una imatge amb escala de grisos.
    """
    for line in dades:
        greyline = []
        for pixel in line:
            greypixel = 0
            greypixel = (pixel[0]*.30 + pixel[1]*.59 + pixel[2]*.11)
            greyline.append(greypixel)

def valorMàxim(dades: Dades) -> int:
    """
    Calcula el valor màxim de totes les intensitats que apareixen en una imatge en color o escala de grisos.

    Arguments:
        dades: Una llista de llistes de píxels representats per o bé enters representant intensitats de blanc en escala de grisos o bé 3-tuples.
               Cada tupla conté la intensitat dels diferents canals de color de la següent manera: (vermell, verd, blau).

    Retorna:
        Un enter amb el valor màxim que conté un píxel de la imatge per a qualsevol canal.
    """

def dimensions(dades: Dades) -> (int, int):
    """
    Calcula les dimensions d'una imatge a partir de la llista de llistes de píxels.
    Assumeix una imatge ben formada amb totes les files de la mateixa longitud.

    Arguments:
        dades: Una llista de llistes de píxels representats o bé per enters o bé per 3-tuples.

    Retorna:
        Una 2-tupla amb les dimensions de la imatge de la següent manera (amplada, alçada).
    """

def detectaTipus(dades: Dades) -> (str, str):
    """
    Detecta el tipus d'imatge contingut a les dades.
    Identifica el tipus d'imatge de la següent manera:
       - Si els píxels estan fets de tuples és en color.
       - Si els píxels són enters i el seu valor màxim no supera l'1 són en blanc i negre.
       - Si els píxels són enters i el seu valor màxim supera l'1 són en color.

    Arguments:
        dades: llista de llistes de píxels representats o bé per enters o bé per 3-tuples.

    Retorna:
        Una 2-tupla de cadenes de caràcters amb la informació de la capçalera ('P1', 'P2', 'P3' segons sigui una imatge en Blanc i negre, en escala de grisos o en color) en el primer element i l'extensió ('ppm', 'pbm', 'pgm' respectivament) en el segon.
    """

def escriuImatge(dades: Dades, nom: str):
    """
    Escriu les dades d'una imatge en un fitxer. Identifica automàticament el tipus d'imatge i l'extensió que cal fer servir.
    En cas que el valor màxim de la imatge estigui entre 2 i 255 (inclosos) definirà el valor màxim de la imatge com a 255. En cas que sigui major, deixarà el major valor com a valor màxim.

    Arguments:
        dades: Llista de llistes de píxels representats o bé per enters o bé per 3-tuples.
        nom: Cadena de caràcters que representa el nom del fitxer a escriure sense extensió.
    """
carregaImatgeColor('Imatges Prova/Lena/lena_ascii_arreglada.ppm')