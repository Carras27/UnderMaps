# Nombres posibles de la columna de comunidades (en minúsculas y sin tildes)
ALIAS_COLUMNA_CCAA = {
    "comunidades autonomas",
    "comunidades y ciudades autonomas",
    "comunidad autonoma",
    "ccaa",
    "acom_name",
}

# Nombres posibles de la columna de provincias
ALIAS_COLUMNA_PROVINCIA = {
    "provincias",
    "provincia",
}

# Nombres posibles de la columna de comarcas
ALIAS_COLUMNA_COMARCA = {
    "comarca",
    "comarcas",
}

# Columnas donde hay que elegir un valor. Clave: nombre de la categoría.
# Valor: posibles nombres de la columna 
ALIAS_COLUMNAS_A_ELEGIR = {
    "periodo": {"periodo", "ano", "anio", "year"},
    "sexo": {"sexo", "sexos"},
    # añadir
}

# Nombre normalizado -> nombre canónico (el del GeoJSON)
ALIAS_VALORES_CCAA = {
    "melilla": "Ciudad Autónoma de Melilla",
    "melilla ciudad autonoma de": "Ciudad Autónoma de Melilla",
    "madrid comunidad de": "Comunidad de Madrid",
    "madrid": "Comunidad de Madrid",
    "navarra": "Comunidad Foral de Navarra",
    "navarra comunidad foral de": "Comunidad Foral de Navarra",
    "castilla leon": "Castilla y León",
    "castilla y leon": "Castilla y León",
    "asturias": "Principado de Asturias",
    "asturias principado de": "Principado de Asturias",
    "castilla la mancha": "Castilla-La Mancha",
    "ceuta": "Ciudad Autónoma de Ceuta",
    "catalunya": "Cataluña",
    "cataluna": "Cataluña",
    "andalucia": "Andalucía",
    "ceuta ciudad autonoma de": "Ciudad Autónoma de Ceuta",
    "islas baleares": "Illes Balears",
    "baleares": "Illes Balears",
    "islas canarias": "Canarias",
    "murcia region de": "Región de Murcia",
    "murcia": "Región de Murcia",
    "region de murcia": "Región de Murcia",
    "comunidad valenciana": "Comunitat Valenciana",
    "valencia": "Comunitat Valenciana",
    "aragon": "Aragón",
    "euskadi": "País Vasco",
    "pais vasco": "País Vasco",
    # añadir...
}