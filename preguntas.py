"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    with open('data.csv') as file:
        content = file.readlines()
        content = [int(x.strip().split('\t')[1]) for x in content]
        rta = sum(content)
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return rta


def pregunta_02():
    with open('data.csv') as file:
        content = file.readlines()
        content = [(x.strip().split('\t')[0]) for x in content]
        content = sorted(content)
        letras = list()
        rta = list()
        for i in content:
            if i not in letras:
                letras.append(i)
                rta.append((i, content.count(i)))
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    return rta


def pregunta_03():
    with open('data.csv') as file:
        content = file.readlines()
        content = [(x.strip().split('\t')[0:2]) for x in content]
        letras = sorted((list(set([x[0] for x in content]))))
        rta = list()
        for i in letras:
            acum = 0
            for e in content:
                if e[0] == i:
                    acum += int(e[1])
            rta.append((i, acum))
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return rta


def pregunta_04():
    with open('data.csv') as file:
        content = file.readlines()
        content = [x.strip().split('\t')[2][5:7] for x in content]
        content = sorted(content)
        meses = list()
        rta = list()
        for i in content:
            if i not in meses:
                meses.append(i)
                rta.append((i, content.count(i)))
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return rta


def pregunta_05():
    with open('data.csv') as file:
        content = file.readlines()
        content = [(x.strip().split('\t')[0:2]) for x in content]
        letras = sorted((list(set([x[0] for x in content]))))
        rta = list()
        for i in letras:
            acum = list()
            for e in content:
                if e[0] == i:
                    acum.append(int(e[1]))
            rta.append((i, max(acum), min(acum)))
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return rta


def pregunta_06():
    with open('data.csv') as file:
        content = file.readlines()
        content = [x.strip().split('\t')[-1] for x in content]
        content = ','.join(content).split(',')
        content = [x.split(':') for x in content]
        strings = sorted(list(set([x[0] for x in content])))
        rta = list()
        for i in strings:
            valores = list()
            for e in content:
                if e[0] == i:
                    valores.append(int(e[1]))
            rta.append((i, min(valores), max(valores)))
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return rta


def pregunta_07():
    with open('data.csv') as file:
        content = file.readlines()
        content = [x.strip().split('\t')[0:2] for x in content]
        numeros = sorted(list(set([int(x[1]) for x in content])))
        rta = list()
        for i in numeros:
            letras = list()
            for e in content:
                if int(e[1]) == i:
                    letras.append(e[0])
            rta.append((int(i), letras))
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return rta


def pregunta_08():
    with open('data.csv') as file:
        content = file.readlines()
        content = [x.strip().split('\t')[0:2] for x in content]
        numeros = sorted(list(set([int(x[1]) for x in content])))
        rta = list()
        for i in numeros:
            letras = list()
            for e in content:
                if int(e[1]) == i:
                    letras.append(e[0])
            rta.append((int(i), sorted(list(set(letras)))))

    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return rta


def pregunta_09():
    with open('data.csv') as file:
        content = file.readlines()
        content = [x.strip().split('\t')[-1] for x in content]
        content = ','.join(content).split(',')
        content = [x.split(':')[0] for x in content]
        strings = sorted(list(set(content)))
        dict_strings = dict()
        for i in strings:
            dict_strings[i] = content.count(i)
        rta = dict_strings
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return  rta


def pregunta_10():
    with open('data.csv') as file:
        content = file.readlines()
        content = [x.strip().split('\t') for x in content]
        for i in content:
            i.pop(1)
            i.pop(1)
            i[1] = len(i[1].split(','))
            i[2] = len(i[2].split(','))
        rta = [tuple(x) for x in content]
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return rta


def pregunta_11():
    with open('data.csv') as file:
        content = file.readlines()
        content2 = content.copy()
        content = [x.strip().split('\t')[3] for x in content]
        content = ','.join(content).split(',')
        letras = sorted(list(set(content)))
        content2 = [x.strip().split('\t') for x in content2]
        rta = dict()
        for i in letras:
            acum = 0
            for e in content2:
                if i in e[3]:
                    acum += int(e[1])
            rta[i] = acum
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return rta


def pregunta_12():
    with open('data.csv') as file:
        content = file.readlines()
        content = [x.strip().split('\t') for x in content]
        lista2 = list()
        for i in content:
            for e in range(3):
                i.pop(1)
            i[1] = i[1].split(',')
        valores = [x[1] for x in content]
        for e in valores:
            lista = sum([int(x.split(':').pop(1)) for x in e])
            lista2.append(lista)
        for k in range(len(content)):
            content[k].append(lista2[k])
            content[k].pop(1)
        letras = [x[0] for x in content]
        letras = sorted(list(set(letras)))
        rta = dict()
        for m in letras:
            acum = 0
            for n in content:
                if n[0] == m:
                    acum += n[1]
            rta[m] = acum
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return rta
