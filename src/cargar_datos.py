import requests
import pandas as pd
import geopandas as gpd
import json

def cargar_geometrias_provincias():
    """Carga el geojson de provincias de España."""
    url = "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/spain-provinces.geojson"
    return gpd.read_file(url)


def cargar_poblacion_ine(id_tabla=2852):
    """Descarga datos de población por CCAA desde la API del INE."""
    url = f"https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/{id_tabla}?nult=1&tip=AM"
    response = requests.get(url)
    data = response.json()

    registros = []
    for serie in data:
        meta = {m["T3_Variable"]: m for m in serie["MetaData"]}

        ccaa = meta.get("Comunidades y Ciudades Autónomas", {})
        sexo = meta.get("Sexo", {})
        tamano = meta.get("Tamaño de los municipios", {})

        # nos interesa: sexo Total, tamaño Total, y que NO sea el total nacional (código "00")
        if sexo.get("Nombre") != "Total":
            continue
        if tamano.get("Nombre") != "Total habitantes":
            continue
        if ccaa.get("Codigo") == "00":
            continue

        if not serie["Data"]:
            continue

        ultimo = serie["Data"][-1]
        registros.append({
            "ccaa_codigo": ccaa.get("Codigo"),
            "ccaa_nombre": ccaa.get("Nombre"),
            "poblacion": ultimo["Valor"],
            "anyo": ultimo["Anyo"]
        })

    return pd.DataFrame(registros)


if __name__ == "__main__":
    df = cargar_poblacion_ine()
    print(df)