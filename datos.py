import re
import unicodedata

import pandas as pd
from pathlib import Path

from aliases import (
    ALIAS_COLUMNA_CCAA,
    ALIAS_COLUMNA_PROVINCIA,
    ALIAS_VALORES_CCAA,
    ALIAS_COLUMNA_COMARCA,
    ALIAS_COLUMNAS_A_ELEGIR,
)


def _limpiar(texto: str) -> str:
    """
        Pasa todo a minúscula, elimina tildes, puntuación y espacios sobrantes.
        normaliza los caracteres especiales de UTF-8.
    """
    texto = unicodedata.normalize("NFKD", str(texto))
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = re.sub(r"[^\w\s]", " ", texto.lower())
    return re.sub(r"\s+", " ", texto).strip()


def _normalizar_nombre_ccaa(valor: str) -> str:
    """
        Normaliza el nombre de la CCAA y lo busca entre los aliases.
    """
    limpio = _limpiar(valor)
    limpio = re.sub(r"^\d+\s+", "", limpio)  # quita el código numérico del INE
    print(ALIAS_VALORES_CCAA.get(limpio, valor))
    return ALIAS_VALORES_CCAA.get(limpio, valor)

def _quedarse_con_vacias(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """
        Conserva las filas donde la columna indicada esté vacía.
    """
    vacia = df[columna].isna() | (df[columna].astype(str).str.strip() == "")
    return df[vacia].drop(columns=columna)

def _categoria_a_elegir(nombre: str):
    """ Devuelve la categoria (periodo, sexo...), si el nombre coincide 
        con algún alias.
    """
    for categoria, aliases in ALIAS_COLUMNAS_A_ELEGIR.items():
        if nombre in aliases:
            return categoria
    return None

def elegir_valor(df: pd.DataFrame, columna: str, valor=None) -> tuple[pd.DataFrame, str | None]:
    """
        Filtra la tabla por un valor de la columna. Por defecto, no se indica
        y se muestran las opciones posibles.
    """
    valores = df[columna].astype(str).str.strip()
    opciones = sorted(valores.unique())

    unica = len(opciones) == 1
    if unica:  # Si solo hay una opción, se escoge                     
        valor = opciones[0]

    if valor is None:
        print (f"Opciones en '{columna}': '{opciones}'.")
        valor = input("Elige una: ")

    valor = str(valor).strip()
    
    if valor not in opciones:
        raise ValueError(f"'{valor}' no está en '{columna}'. Opciones: {opciones}")


    return df[valores == valor].drop(columns=columna), (None if unica else valor)

def leer_datos(ruta_csv: str, elecciones: dict | None = None, sep: str = ";", decimal: str = ",", thousands: str = ".") -> pd.DataFrame:
    """
        Lee un CSV del INE, localiza la columna de CCAA, ignora provincias
        y normaliza nombres.
    """
    elecciones = elecciones or {}
    titulo = [Path(ruta_csv).stem.replace("_", " ")] # Quita la extensión al nombre del fichero

    # Convierte el archivo leido en una tabla de pandas (DataFrame).
    df = pd.read_csv(ruta_csv, sep=sep, decimal=decimal, thousands=thousands, encoding="utf-8")

    # Renombramos la ultima columna, que contendra los datos a representar
    df = df.rename(columns={df.columns[-1]: "datos"})

    # Recorre todas las columnas, salvo la de datos
    for columna in list(df.columns[:-1]):
        nombre = _limpiar(columna)

        # Borra todas las lineas con provincias y comarcas
        if nombre in ALIAS_COLUMNA_PROVINCIA:
            df = _quedarse_con_vacias(df, columna)
        elif nombre in ALIAS_COLUMNA_COMARCA:
            df = _quedarse_con_vacias(df, columna)
        # Renombra la columna de Comunidades Autonomas
        elif nombre in ALIAS_COLUMNA_CCAA:
            df = df.rename(columns={columna: "ccaa"})
        else: # Cualquier otra columna, si tiene varias opciones, se elige una
            clave = _categoria_a_elegir(nombre) or nombre
            df, elegido = elegir_valor(df, columna, elecciones.get(clave))
            if elegido is not None:
                titulo.append(f"{columna}: {elegido}")
        
    # Da un error si no encuentra la columna de Comunidades Autónomas
    if "ccaa" not in df.columns:
        raise ValueError(f"No encuentro columna de CCAA en {ruta_csv}. Columnas: {list(df.columns)}")

    # Elimina las filas de la columna CCAA que estén vacías o representen un valor total.
    ccaa = df["ccaa"].fillna("").astype(str)
    es_nacional = (ccaa.str.strip() == "") | ccaa.map(_limpiar).str.startswith("total")
    df = df[~es_nacional].copy()

    # Aplica la normalizacion a cada valor de la columna
    df["ccaa"] = df["ccaa"].map(_normalizar_nombre_ccaa)

    return df, " | ".join(titulo)