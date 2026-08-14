import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# 1. Carga de datos
df = pd.read_csv('notebooks/67988.csv')
df2 = df[(df['Sexo'] == 'Total') & (df['Periodo'] == '2025')].copy()

# --- FIX 1: Limpiar puntos de miles y convertir a número AL PRINCIPIO ---
df2['Total'] = pd.to_numeric(
    df2['Total'].astype(str).str.replace('.', '', regex=False), 
    errors='coerce'
).fillna(0)

# 2. Filtrado de provincias / CCAA
es_provincia = df2['Provincias'].fillna('').str[:2].str.isdigit()
df_ccaa = df2[~es_provincia].copy()

# 3. Agrupación por CCAA
df_total = df_ccaa.groupby('CCAA')['Total'].sum().reset_index()

# --- FIX 2: Extraer el número de la CCAA y asegurar 2 dígitos (zfill) ---
# Extrae solo los dígitos numéricos de la cadena por si hay espacios extra
df_total['codigo_ine'] = df_total['CCAA'].astype(str).str.extract(r'(\d+)')[0].str.zfill(2)

# 4. Cargar GeoJSON
mapa = gpd.read_file('notebooks/espana.geojson')

# --- FIX 3: Asegurar que acom_code también sea texto de 2 dígitos ---
mapa['acom_code'] = mapa['acom_code'].astype(str).str.zfill(2)

# 5. Fusionar
mapa_completo = mapa.merge(df_total, left_on="acom_code", right_on="codigo_ine", how="left")

# Rellenar posibles fallos en el merge
mapa_completo['Total'] = mapa_completo['Total'].fillna(0)

# --- FIX 4: Asignación de colores ---
mapa_completo['color'] = mapa_completo['Total'].apply(lambda x: 'red' if x > 1000000 else 'blue')

# ---------------------------------------------------------
# PASO 5: Dibujar el mapa
# ---------------------------------------------------------
fig, ax = plt.subplots(1, 1, figsize=(10, 8))

# Comprobación por consola para verificar las cifras reales procesadas
print("--- DATOS QUE SE VAN A PINTAR ---")
print(df_total[['codigo_ine', 'CCAA', 'Total']])

# Pintamos las CCAA
mapa_completo.plot(color=mapa_completo['color'], edgecolor='black', linewidth=0.5, ax=ax)

# Formato final
ax.axis('off')
plt.title('CCAA con más de 1M de habitantes (Rojo) vs Resto (Azul)')

plt.show()