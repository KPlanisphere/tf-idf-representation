from colorama import Back, init
import math

# -----------------
# BARRA DE PROGRESO
# -----------------

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))#CALCULA PORCENTAJE
    bar = (Back.LIGHTGREEN_EX+' '+Back.RESET) * int(percent) + '-' * (100 - int(percent))#DEFINE BARRA
    print(f"\r|{bar}| {percent:.2f}%", end="\r")#MUESTRA BARRA + PORCENTAJE

init()

# leer un archivo y devolver su contenido como una lista de líneas
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.readlines()
    return contenido

# escribir una matriz en un archivo de texto
def escribir_matriz(nombre_archivo, matriz):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        contador = 0
        for fila in matriz:
            contador += 1
            progress_bar(contador, 93) #LLAMADA A FUNCIÓN 'progress_bar()'
            archivo.write('\t'.join(map(str, fila)) + '\n')

# generar el vocabulario a partir de un archivo de texto
def generar_vocabulario(archivo_vocabulario):
    vocabulario = {}
    lineas = leer_archivo(archivo_vocabulario)
    contador = 0
    for linea in lineas:
        contador += 1
        palabras = linea.strip().split()
        for palabra in palabras:
            vocabulario[palabra] = len(vocabulario)
    return vocabulario

# -----------------
#    VECTORIZAR
# -----------------

def vectorizar_documentos(archivo_documentos, vocabulario):
    lineas = leer_archivo(archivo_documentos)
    matriz = []
    print("\nVECTORIZANDO DOCUMENTOS...")
    for linea in lineas:
        frecuencias = [0] * len(vocabulario)
        palabras = linea.strip().split()
        for palabra in palabras:
            if palabra in vocabulario:
                indice = vocabulario[palabra]
                frecuencias[indice] += 1
        matriz.append(frecuencias)
    return matriz

# ----------------
#    ARCHIVOS
# ----------------

# Archivos de entrada
archivo_vocabulario = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab5\vocabularioReducidoT.txt'
archivo_documentos  = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab5\cueri-TRUNCADO.txt'
# Archivo de salida
archivo_salida      = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab5\matriz-query.txt'

# Generar vocabulario
vocabulario = generar_vocabulario(archivo_vocabulario)

# Vectorizar documentos
matriz = vectorizar_documentos(archivo_documentos, vocabulario)

# Escribir matriz en archivo de salida
print("\n\nCREANDO MATRIZ TF...")
escribir_matriz(archivo_salida, matriz)

print("\n\nMATRIZ TF GENERADA Y GUARDADA EN:", archivo_salida)
# Imprimir la cantidad de filas y columnas de la matriz
print("\n\tFILAS  DE  LA  MATRIZ TF:", len(matriz))
print("\tCOLUMNAS DE LA MATRIZ TF:", len(matriz[0]))

# -----------------
#   CALCULAR IDF
# -----------------

# Función para calcular el IDF
def calcular_idf(matriz):
    num_documentos = len(matriz)
    num_palabras = len(matriz[0])
    idf = [0] * num_palabras
    print("\nCALCULANDO IDF...")
    for i in range(num_palabras):
        progress_bar(i + 1, num_palabras) #LLAMADA A FUNCIÓN 'progress_bar()'
        # Contar en cuántos documentos aparece la palabra
        num_documentos_con_palabra = sum([1 for documento in matriz if documento[i] > 0])
        # Calcular el IDF
        if num_documentos_con_palabra != 0:
            idf[i] = math.log(num_documentos / num_documentos_con_palabra) + 1
        else:
            idf[i] = 1
    return idf

# Calcular IDF
idf = calcular_idf(matriz)

# Función para escribir el vocabulario junto con sus valores IDF en un archivo de texto
def escribir_vocabulario_idf(nombre_archivo, vocabulario, idf):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        for palabra, valor_idf in zip(vocabulario, idf):
            archivo.write(palabra + '\t' + str(valor_idf) + '\n')

# Generar archivo con vocabulariocls IDF
archivo_idf = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab5\IDF-query.txt'
escribir_vocabulario_idf(archivo_idf, vocabulario, idf)

print("\n\nVALORES IDF GUARDADOS EN:", archivo_idf)

# -----------------
#  CALCULAR TF-IDF
# -----------------

# Función para calcular el TF-IDF
def calcular_tfidf(matriz_tf, idf):
    print("\nCALCULANDO TF - IDF...")
    matriz_tfidf = []
    contador = 0
    for tf_vector in matriz_tf:
        contador += 1
        tfidf_vector = [tf * idf[i] for i, tf in enumerate(tf_vector)]
        matriz_tfidf.append(tfidf_vector)
        progress_bar(contador, 93) #LLAMADA A FUNCIÓN 'progress_bar()'
    return matriz_tfidf

# Calcular TF-IDF
matriz_tfidf = calcular_tfidf(matriz, idf)

# Archivo de salida para la matriz TF-IDF
archivo_salida_tfidf = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab5\matriz-TFIDF-query.txt'

# Escribir matriz TF-IDF en archivo de salida
print("\n\nCREANDO MATRIZ TF-IDF...")
escribir_matriz(archivo_salida_tfidf, matriz_tfidf)

print("\n\nMATRIZ TF-IDF GENERADA Y GUARDADA EN:", archivo_salida_tfidf)