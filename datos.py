import re
import unicodedata

import pandas as pd

from aliases import (
    ALIAS_COLUMNA_CCAA,
    ALIAS_COLUMNA_PROVINCIA,
    ALIAS_VALORES_CCAA,
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


def leer_datos(ruta_csv: str, sep: str = ";", decimal: str = ",", thousands: str = ".") -> pd.DataFrame:
    """
        Lee un CSV del INE, localiza la columna de CCAA, ignora provincias
        y normaliza nombres.
    """

    # Convierte el archivo leido en una tabla de pandas (DataFrame).
    df = pd.read_csv(ruta_csv, sep=sep, decimal=decimal, thousands=thousands, encoding="utf-8")

    # Recorre todas las columnas para buscar la columna de provincias y la borra.
    prov = [col for col in df.columns if _limpiar(col) in ALIAS_COLUMNA_PROVINCIA]
    df = df.drop(columns=prov)

    # Recorre todas las columnas buscando la columna de CCAA, la renombra a 'ccaa'.
    ccaa = [c for c in df.columns if _limpiar(c) in ALIAS_COLUMNA_CCAA]
    if not ccaa:
        raise ValueError(f"No encuentro columna de CCAA en {ruta_csv}. Columnas: {list(df.columns)}")
    df = df.rename(columns={ccaa[0]: "ccaa"})

    # Aplica la normalizacion a cada valor de la columna
    df["ccaa"] = df["ccaa"].map(_normalizar_nombre_ccaa)
    
    # Elimina las filas totales (Total, Total Nacional...)
    df = df[~df["ccaa"].map(_limpiar).str.startswith("total")]

    return df