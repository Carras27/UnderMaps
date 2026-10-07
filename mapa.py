import geopandas as gpd
import matplotlib.pyplot as plt

def cargar_mapa(ruta_geojson: str) -> gpd.GeoDataFrame:
    """ Carga el geojson del mapa y lo devuelve como GeoDataFrame"""
    gdf = gpd.read_file(ruta_geojson)

    # Si no trae sistema de coordenadas, asume WGS84 (lo habitual en GeoJSON)
    if gdf.crs is None:
        gdf = gdf.set_crs(epsg=4326)

    return gdf

def mostrar_mapa(gdf: gpd.GeoDataFrame, titulo: str) -> None:
    fig, ax = plt.subplots(figsize=(6,5)) # Define el tamaño del mapa
    gdf.plot(ax=ax, color="#dde5ee", edgecolor="#555", linewidth=0.5) # Define los colores del mapa y el grosor de las lineas
    ax.set_title(titulo) # Define el titulo
    ax.set_axis_off() # Quita ejes y numeros molestos
    plt.show()

if __name__ == "__main__":
    mapa = cargar_mapa("mapas/...")
    # print(mapa.columns.tolist())  
    # print(mapa[["acom_code", "acom_name", "acom_iso3166_code"]])
    # print(mapa.crs)
    mostrar_mapa(mapa, "España")
