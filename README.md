# Document and Query Representation with TF and TF-IDF

## Description
This project focuses on representing documents and queries using Term Frequency (TF) and Term Frequency-Inverse Document Frequency (TF-IDF) models. The main goal is to prepare matrices that represent the frequency and importance of terms in a collection of documents and queries. This project builds upon the results of previous laboratories and demonstrates advanced text processing techniques to enhance the efficiency of information retrieval within large text datasets.


### Files Included
- **lab5-docs.py**: A Python script for processing document texts to create TF and TF-IDF matrices.
- **lab5-query.py**: A Python script for processing query texts to create TF and TF-IDF matrices.
- **Laboratorio 5 Representación tf y tf-idf.pdf**: Official documentation detailing the objectives, methodology, and results of the project.
- **cueri-TRUNCADO.txt**: A truncated version of query texts.
- **documento-TRUNCADO.txt**: A truncated version of document texts.
- **IDF-docs.txt**: A text file containing the IDF values for documents.
- **IDF-query.txt**: A text file containing the IDF values for queries.
- **matriz-docs.txt**: A text file containing the TF matrix for documents.
- **matriz-query.txt**: A text file containing the TF matrix for queries.
- **matriz-TFIDF-docs.txt**: A text file containing the TF-IDF matrix for documents.
- **matriz-TFIDF-query.txt**: A text file containing the TF-IDF matrix for queries.
- **vocabularioReducidoT.txt**: A text file containing the reduced vocabulary.

### Notable Code Snippets

#### 1. Vectorizing Documents (lab5-docs.py)
This snippet reads document texts and generates a TF matrix based on the reduced vocabulary.

```python
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

# Archivos de entrada
archivo_vocabulario = 'vocabularioReducidoT.txt'
archivo_documentos  = 'documento-TRUNCADO.txt'
archivo_salida      = 'matriz-docs.txt'

# Generar vocabulario
vocabulario = generar_vocabulario(archivo_vocabulario)

# Vectorizar documentos
matriz = vectorizar_documentos(archivo_documentos, vocabulario)

# Escribir matriz en archivo de salida
escribir_matriz(archivo_salida, matriz)
```
#### 2. Calculating IDF (lab5-query.py)

This snippet calculates the IDF values for the terms in the query texts.

```python
def calcular_idf(matriz):
    num_documentos = len(matriz)
    num_palabras = len(matriz[0])
    idf = [0] * num_palabras
    print("\nCALCULANDO IDF...")
    for i in range(num_palabras):
        num_documentos_con_palabra = sum([1 for documento in matriz if documento[i] > 0])
        idf[i] = math.log(num_documentos / num_documentos_con_palabra) + 1
    return idf

# Archivos de entrada
archivo_vocabulario = 'vocabularioReducidoT.txt'
archivo_documentos  = 'cueri-TRUNCADO.txt'
archivo_salida      = 'matriz-query.txt'

# Generar vocabulario
vocabulario = generar_vocabulario(archivo_vocabulario)

# Vectorizar documentos
matriz = vectorizar_documentos(archivo_documentos, vocabulario)

# Calcular IDF
idf = calcular_idf(matriz)

# Escribir IDF en archivo de salida
archivo_idf = 'IDF-query.txt'
escribir_vocabulario_idf(archivo_idf, vocabulario, idf)
```

### Official Documentation Summary

The official documentation provided in "Laboratorio 5 Representación tf y tf-idf.pdf" outlines the following key points:

#### Objectives

-   Represent documents and queries using TF and TF-IDF models.
-   Understand the importance of term frequency and inverse document frequency in information retrieval.
-   Develop Python scripts to compute TF and TF-IDF matrices.

#### Methodology

1.  **Vectorization**: Represent each document and query as a numerical vector based on the term frequencies.
2.  **TF Calculation**: Compute the term frequency (TF) for each term in the documents and queries.
3.  **IDF Calculation**: Compute the inverse document frequency (IDF) for each term.
4.  **TF-IDF Calculation**: Multiply the TF values by the IDF values to obtain the TF-IDF matrix.

#### Results and Discussion

-   The TF matrices for documents and queries show the frequency of terms in each text.
-   The IDF values highlight the importance of terms across the entire corpus.
-   The TF-IDF matrices combine the term frequency and inverse document frequency to emphasize terms that are important in specific documents but not common across the entire corpus.

#### Conclusion

The project successfully demonstrates the creation of TF and TF-IDF matrices for documents and queries, providing a robust method for representing and analyzing text data in information retrieval tasks.

### Installation and Usage

1.  Clone the repository to your local machine.
2.  Ensure you have Python installed.
3.  Run the `lab5-docs.py` script to create the TF and TF-IDF matrices for documents.
4.  Run the `lab5-query.py` script to create the TF and TF-IDF matrices for queries.

```bash
git clone https://github.com/KPlanisphere/tf-idf-representation.git
cd tf-idf-representation
python lab5-docs.py
python lab5-query.py
```

### Dependencies

-   Python
-   NLTK library
-   Colorama library