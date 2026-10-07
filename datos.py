import re
import unicodedata

import pandas as pd

from aliases import (
    ALIAS_COLUMNA_CCAA,
    ALIAS_COLUMNA_PROVINCIA,
    ALIAS_VALORES_CCAA,
    ALIAS_COLUMNA_COMARCA,
    ALIAS_COLUMNA_PERIODO,
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

def _elegir_periodo(df: pd.DataFrame, columna: str, periodo=None) -> pd.DataFrame:
    """
        Filtra por un periodo (por defecto, ninguno), si no se indica ninguno,
        da a elegir entre las opciones posibles.
    """
    valores = df[columna].astype(str).str.strip()
    opciones = sorted(valores.unique())

    if periodo is None:
        print (f"Opciones en '{columna}': '{opciones}'.")
        periodo = input("Elige una: ")

    periodo = str(periodo).strip()
    if periodo not in opciones:
        raise ValueError(f"'{periodo}' no está en '{columna}'. Opciones: {opciones}")

    return df[valores == periodo].drop(columns=columna)

def leer_datos(ruta_csv: str, sep: str = ";", decimal: str = ",", thousands: str = ".") -> pd.DataFrame:
    """
        Lee un CSV del INE, localiza la columna de CCAA, ignora provincias
        y normaliza nombres.
    """

    # Convierte el archivo leido en una tabla de pandas (DataFrame).
    df = pd.read_csv(ruta_csv, sep=sep, decimal=decimal, thousands=thousands, encoding="utf-8")

    # Recorre todas las columnas
    for columna in list(df.columns):
        nombre = _limpiar(columna) 

        # Borra todas las lineas con provincias y comarcas
        if nombre in ALIAS_COLUMNA_PROVINCIA:
            df = _quedarse_con_vacias(df, columna)
        elif nombre in ALIAS_COLUMNA_COMARCA:
            df = _quedarse_con_vacias(df, columna)

        # Da a elegir un periodo
        elif nombre in ALIAS_COLUMNA_PERIODO:
            df = _elegir_periodo(df, columna, None)
        # Renombra la columna de Comunidades Autonomas
        elif nombre in ALIAS_COLUMNA_CCAA:
            df = df.rename(columns={columna: "ccaa"})

    
    if "ccaa" not in df.columns:
        raise ValueError(f"No encuentro columna de CCAA en {ruta_csv}. Columnas: {list(df.columns)}")

    # Aplica la normalizacion a cada valor de la columna
    df["ccaa"] = df["ccaa"].map(_normalizar_nombre_ccaa)

    # Elimina las filas totales (Total, Total Nacional...)
    df = df[~df["ccaa"].map(_limpiar).str.startswith("total")]

    return df