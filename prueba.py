import pandas as pd

registros = []
for serie in data:
    nombre = serie["Nombre"]
    ultimo = serie["Data"][-1]
    registros.append({
        "serie": nombre,
        "valor": ultimo["Valor"],
        "periodo": ultimo["NombrePeriodo"]
    })

df = pd.DataFrame(registros)
print(df.head(20))