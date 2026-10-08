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

# Nombre normalizado (CCAA) -> nombre canónico (el del GeoJSON)
ALIAS_VALORES_CCAA = {
    # Melilla
    "melilla": "Ciudad Autónoma de Melilla",
    "melilla ciudad autonoma de": "Ciudad Autónoma de Melilla",
    # Madrid
    "madrid comunidad de": "Comunidad de Madrid",
    "madrid": "Comunidad de Madrid",
    # Navarra
    "navarra": "Comunidad Foral de Navarra",
    "navarra comunidad foral de": "Comunidad Foral de Navarra",
    # Castilla y León
    "castilla leon": "Castilla y León",
    "castilla y leon": "Castilla y León",
    "leon castilla y": "Castilla y León",
    # Asturias
    "asturias": "Principado de Asturias",
    "asturias principado de": "Principado de Asturias",
    "principado de asturias": "Principado de Asturias",
    # Castilla-La Mancha
    "castilla la mancha": "Castilla-La Mancha",
    # Ceuta
    "ceuta": "Ciudad Autónoma de Ceuta",
    "ceuta ciudad autonoma de": "Ciudad Autónoma de Ceuta",
    # Cataluña
    "catalunya": "Cataluña",
    "cataluna": "Cataluña",
    # Andalucia
    "andalucia": "Andalucía",
    # Islas Baleares
    "islas baleares": "Illes Balears",
    "baleares islas": "Illes Balears",
    "baleares": "Illes Balears",
    "balears": "Illes Balears",
    "balears illes": "Illes Balears",
    "illes balears": "Illes Balears",
    # Islas Canarias
    "islas canarias": "Canarias",
    "canarias": "Canarias",
    "canarias islas": "Canarias",
    # Cantabria
    "cantabria": "Cantabria",
    # Galicia
    "galicia": "Galicia",
    # La Rioja
    "la rioja": "La Rioja",
    "rioja la": "La Rioja",
    # Extremadura
    "extremadura": "Extremadura",
    # Murcia
    "murcia region de": "Región de Murcia",
    "murcia": "Región de Murcia",
    "region de murcia": "Región de Murcia",
    # Comunitat Valenciana
    "comunitat valenciana": "Comunitat Valenciana",
    "valenciana comunitat": "Comunitat Valenciana",
    "comunidad valenciana": "Comunitat Valenciana",
    "valencia": "Comunitat Valenciana",
    # Aragón
    "aragon": "Aragón",
    # País Vasco
    "euskadi": "País Vasco",
    "pais vasco": "País Vasco",
    # añadir...
}

# Nombre canónico (Provincias) -> nombre normalizado (el del GeoJson)
ALIAS_VALORES_PROVINCIAS = {
    # Álava
    "alava": "Álava",
    "araba": "Álava",
    "araba alava": "Álava",
    "alava araba": "Álava",
    # Albacete
    "albacete": "Albacete",
    # Alicante
    "alicante": "Alicante",
    "alacant": "Alicante",
    "alicante alacant": "Alicante",
    "alacant alicante": "Alicante",
    # Almería
    "almeria": "Almería",
    # Ávila
    "avila": "Ávila",
    # Badajoz
    "badajoz": "Badajoz",
    # Islas Baleares
    "islas baleares": "Islas Baleares",
    "baleares islas": "Islas Baleares",
    "illes balears": "Islas Baleares",
    "balears illes": "Islas Baleares",
    "balears": "Islas Baleares",
    "baleares": "Islas Baleares",
    # Barcelona
    "barcelona": "Barcelona",
    # Burgos
    "burgos": "Burgos",
    # Cáceres
    "caceres": "Cáceres",
    # Cádiz
    "cadiz": "Cádiz",
    # Cantabria
    "cantabria": "Cantabria",
    # Castellón
    "castellon": "Castellón",
    "castello": "Castellón",
    "castellon castello": "Castellón",
    "castello castellon": "Castellón",
    # Ciudad Real
    "ciudad real": "Ciudad Real",
    "real ciudad": "Ciudad Real",
    # Córdoba
    "cordoba": "Córdoba",
    # La Coruña
    "la coruna": "La Coruña",
    "a coruna": "La Coruña",
    "coruna": "La Coruña",
    "coruna la": "La Coruña",
    "coruna a": "La Coruña",
    # Cuenca
    "cuenca": "Cuenca",
    # Gerona
    "gerona": "Gerona",
    "girona": "Gerona",
    # Granada
    "granada": "Granada",
    # Guadalajara
    "guadalajara": "Guadalajara",
    # Guipúzcoa
    "guipuzcoa": "Guipúzcoa",
    "gipuzkoa": "Guipúzcoa",
    # Huelva
    "huelva": "Huelva",
    # Huesca
    "huesca": "Huesca",
    # Jaén
    "jaen": "Jaén",
    # León
    "leon": "León",
    # Lleida
    "lleida": "Lleida",
    "lerida": "Lleida",
    # La Rioja
    "la rioja": "La Rioja",
    "rioja la": "La Rioja",
    "rioja": "La Rioja",
    # Lugo
    "lugo": "Lugo",
    # Madrid
    "madrid": "Madrid",
    # Málaga
    "malaga": "Málaga",
    # Murcia
    "murcia": "Murcia",
    # Navarra
    "navarra": "Navarra",
    # Orense
    "orense": "Orense",
    "ourense": "Orense",
    # Palencia
    "palencia": "Palencia",
    # Asturias
    "asturias": "Asturias",
    # Las Palmas
    "las palmas": "Las Palmas",
    "palmas las": "Las Palmas",
    "las palmas de gran canaria": "Las Palmas",
    "gran canaria las palmas de": "Las Palmas",
    # Pontevedra
    "pontevedra": "Pontevedra",
    # Salamanca
    "salamanca": "Salamanca",
    # Santa Cruz de Tenerife
    "santa cruz de tenerife": "Santa Cruz de Tenerife",
    "tenerife santa cruz de": "Santa Cruz de Tenerife",
    "tenerife": "Santa Cruz de Tenerife",
    # Segovia
    "segovia": "Segovia",
    # Sevilla
    "sevilla": "Sevilla",
    # Soria
    "soria": "Soria",
    # Tarragona
    "tarragona": "Tarragona",
    # Teruel
    "teruel": "Teruel",
    # Toledo
    "toledo": "Toledo",
    # Valencia
    "valencia": "Valencia",
    "valencia valencia": "Valencia",
    # Valladolid
    "valladolid": "Valladolid",
    # Vizcaya
    "vizcaya": "Vizcaya",
    "bizkaia": "Vizcaya",
    # Zamora
    "zamora": "Zamora",
    # Zaragoza
    "zaragoza": "Zaragoza",
    # Ceuta
    "ceuta": "Ceuta",
    # Melilla
    "melilla": "Melilla",
}