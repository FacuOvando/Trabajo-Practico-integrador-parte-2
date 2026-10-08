import sys

def filtrar_datos(datos, estacion, medicion):

    datos_filtrados = [] # lista vacia

    vista_mediciones = {
        "temperatura": "temperatura",
        "humedad": "humedad",
        "presion": "presion",
        "viento": "velocidad del viento",
        "velocidad del viento": "velocidad del viento",
        "direccion del viento": "direccion del viento"
    }

    if medicion.lower not in vista_mediciones:
        print(f"error, la medicion: {medicion}, no es valida")
        sys.exit(1)

    clave_de_medicion = vista_mediciones[medicion.lower()]

    for registro in datos: # comparacion exacta sin importar mayusculas o minusculas
        if "estacion" in registro:
            if registro["estacion"].strip().upper() == estacion.strip().upper():
                if clave_de_medicion in registro:
                    datos_filtrados.append({
                        "fecha": registro["fecha"],
                        "hora": registro["hora"],
                        "valor": registro[clave_de_medicion]
                    })
                    
    return datos_filtrados