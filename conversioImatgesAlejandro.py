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
    tuplelines = []    return int(math.sqrt(area))

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

    return (dadesvermell, dadesverd, dadesblau)

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
    dadesgris = []
    for line in dades:
        lineagris = []
        for pixel in line:
            lineagris.append(int(pixel[0]*.30 + pixel[1]*.59 + pixel[2]*.11))
        dadesgris.append(lineagris)
    return dadesgris

def valorMàxim(dades: Dades) -> int:
    """
    Calcula el valor màxim de totes les intensitats que apareixen en una imatge en color o escala de grisos.

    Arguments:
        dades: Una llista de llistes de píxels representats per o bé enters representant intensitats de blanc en escala de grisos o bé 3-tuples.
               Cada tupla conté la intensitat dels diferents canals de color de la següent manera: (vermell, verd, blau).

    Retorna:
        Un enter amb el valor màxim que conté un píxel de la imatge per a qualsevol canal.
    """
    maxim = 0
    try:
        for line in dades:
            for pixel in line:
                possiblemaxim = max(pixel)
                if possiblemaxim > maxim:
                    maxim = possiblemaxim
        return maxim
    except:
        for line in dades:
            possiblemaxim = max(line)
            if possiblemaxim > maxim:
                maxim = possiblemaxim
        return maxim
def llindar_valor(imatge: Dades, valor: int) -> Dades:
    """
    Transforma una imatge en escala de grisos a una imatge en blanc i negre.
    Utilitza el 'valor' de valor llindar. Els píxels que quedin per sobre del
    valor llindar es transformaran en blancs i els que quedin per sota o amb el
    mateix valor, es tornaran negres.

    Arguments:
      imatge: Una llista de llista de píxels corresponents a una imatge en
        escala de grisos
      valor: Un enter que representa un valor que defineix el llindar dels
        valors que es convertiran en píxels blancs o negres

    Retorna:
      Una llista de llistes d'enters (0s o 1s) que representen una imatge en
      blanc i negre.

    >>> llindar_valor([[125, 100, 75], [50, 255, 200]], 100)
    [[0, 1, 1], [1, 0, 0]]
    """
    return[[0 if pixel >= valor else 1 for pixel in line] for line in imatge]
# llindar_valor([[125, 100, 75], [50, 255, 200]], 100)
def inverteix_verticalment(imatge: Dades) -> Dades:
    """
    Inverteix una imatge verticalment.

    Arguments:
      imatge: Llista de llistes (matriu) de píxels (ja sigui en escala de
      grisos o en color) que invertirà la funció.

    Retorna:
      Matriu de píxels que conté la imatge original invertida verticalment.

    >>> inverteix_verticalment([[125,100,75],[50, 255, 200]])
    [[50, 255, 200], [125, 100, 75]]

    >>> inverteix_verticalment([[1,11,111,1111], [2,22,222,2222], [3,33,333,3333], [4,44,444,4444]])
    [[4, 44, 444, 4444], [3, 33, 333, 3333], [2, 22, 222, 2222], [1, 11, 111, 1111]]
    """
    return [line for line in reversed(imatge)]


def inverteix_horitzontalment(imatge: Dades) -> Dades:
    """
    Inverteix una imatge horitzontalment.

    Arguments:
      imatge: Llista de llistes (matriu) de píxels (ja sigui en escala de
      grisos o en color) que invertirà la funció.

    Retorna:
      Matriu de píxels que conté la imatge original invertida verticalment.

    >>> inverteix_horitzontalment([[125,100,75],[50, 255, 200]])
    [[75, 100, 125], [200, 255, 50]]

    >>> inverteix_horitzontalment([[1,11,111,1111], [2,22,222,2222], [3,33,333,3333], [4,44,444,4444]])
    [[1111, 111, 11, 1], [2222, 222, 22, 2], [3333, 333, 33, 3], [4444, 444, 44, 4]]
    """

    return [list(reversed(line)) for line in imatge]

def dadespercanal(canals):
    '''
    Aquesta funció serveix per preparar les dades en un
    cert color (vermell, verd o blau) en format ppm.
    Argument:
        Les dades de la fotogafia separades a colors.
    Rertorna:
        Les dades en ppm en el color que ens interesi.
    '''
    dades = []
    color = input('Prem 1 per vermell, prem 2 per verd i prem 3 per blau: ')
    if color == '1':
        vermells = canals[0]
        for line in vermells:
            lineavermells = []
            for pixel in line:
                noupixel = []
                noupixel.append(pixel)
                noupixel.append(0)
                noupixel.append(0)
                pixeltuple = tuple(noupixel)
                lineavermells.append(pixeltuple)

            dades.append(lineavermells)
    
        return dades
    
    if color == '2':
        verds = canals[1]
        for line in verds:
            lineaverds = []
            for pixel in line:
                noupixel = []
                noupixel.append(0)
                noupixel.append(pixel)
                noupixel.append(0)
                pixeltuple = tuple(noupixel)
                lineaverds.append(pixeltuple)

            dades.append(lineaverds)
        return dades
    
    if color == '3':
        blaus = canals[2]
        for line in blaus:
            lineablaus = []
            for pixel in line:
                noupixel = []
                noupixel.append(0)
                noupixel.append(0)
                noupixel.append(pixel)
                pixeltuple = tuple(noupixel)
                lineablaus.append(pixeltuple)

            dades.append(lineablaus)
    
        return dades
    
def dimensions(dades: Dades) -> (int, int):
    """
    Calcula les dimensions d'una imatge a partir de la llista de llistes de píxels.
    Assumeix una imatge ben formada amb totes les files de la mateixa longitud.

    Arguments:
        dades: Una llista de llistes de píxels representats o bé per enters o bé per 3-tuples.

    Retorna:
        Una 2-tupla amb les dimensions de la imatge de la següent manera (amplada, alçada).
    """

    return (len(dades[0]), len(dades))

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
    line = dades[0]
    pixel = line[0]
    try:
        if len(pixel) == 3:
            return ('P3', 'ppm')
    except:
        if valorMàxim(dades) > 1:
            return ('P2', 'pgm')
        else:
            return ('P1', 'pbm')
            
def escriuImatge(dades: Dades, nom: str):
    """
    Escriu les dades d'una imatge en un fitxer. Identifica automàticament el tipus d'imatge i l'extensió que cal fer servir.
    En cas que el valor màxim de la imatge estigui entre 2 i 255 (inclosos) definirà el valor màxim de la imatge com a 255. En cas que sigui major, deixarà el major valor com a valor màxim.

    Arguments:
        dades: Llista de llistes de píxels representats o bé per enters o bé per 3-tuples.
        nom: Cadena de caràcters que representa el nom del fitxer a escriure sense extensió.
    """
    tipus = detectaTipus(dades)
    line1 = tipus[0]
    dimensionsimatge = dimensions(dades)
    maxim = valorMàxim(dades)
    if 1 < maxim < 255 :
        maxim = 255
    with open(nom + '.' + tipus[1], mode = 'w') as imatge:
        imatge.write(line1 + '\n')
        imatge.write(str(dimensionsimatge[0]) + ' ' + str(dimensionsimatge[1]) + '\n')
        imatge.write(str(maxim) + '\n')
        if line1 == 'P3':
            for line in dades:
                for pixel in line:
                    imatge.write(str(pixel[0]) + ' ')
                    imatge.write(str(pixel[1]) + ' ')
                    imatge.write(str(pixel[2]) + ' ')
                imatge.write('\n')


        if line1 != 'P3':
            for line in dades:
                for pixel in line:
                    imatge.write(str(pixel) + ' ')
                imatge.write('\n')
