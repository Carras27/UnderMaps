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
        normaliza los caracteres especiales de UTF-8
    """
    texto = unicodedata.normalize("NFKD", str(texto))
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = re.sub(r"[^\w\s]", " ", texto.lower())
    return re.sub(r"\s+", " ", texto).strip()


def _normalizar_nombre_ccaa(valor: str) -> str:
    limpio = _limpiar(valor)
    limpio = re.sub(r"^\d+\s+", "", limpio)  # quita el código numérico del INE
    print(ALIAS_VALORES_CCAA.get(limpio, valor))
    return ALIAS_VALORES_CCAA.get(limpio, valor)


def leer_datos(ruta_csv: str, sep: str = ";", decimal: str = ",", thousands: str = ".") -> pd.DataFrame:
    """
        Lee un CSV del INE, localiza la columna de CCAA, ignora provincias
        y normaliza nombres.
    """
    df = pd.read_csv(ruta_csv, sep=sep, decimal=decimal, thousands=thousands, encoding="utf-8")

    prov = [c for c in df.columns if _limpiar(c) in ALIAS_COLUMNA_PROVINCIA]
    df = df.drop(columns=prov)

    ccaa = [c for c in df.columns if _limpiar(c) in ALIAS_COLUMNA_CCAA]
    if not ccaa:
        raise ValueError(f"No encuentro columna de CCAA en {ruta_csv}. Columnas: {list(df.columns)}")
    df = df.rename(columns={ccaa[0]: "ccaa"})

    df["ccaa"] = df["ccaa"].map(_normalizar_nombre_ccaa)
    df = df[~df["ccaa"].map(_limpiar).str.startswith("total")]

    return df