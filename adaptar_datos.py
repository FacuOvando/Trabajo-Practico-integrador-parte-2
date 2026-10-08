import sys
import json
import modulo_de_validaciones
from datetime import datetime
from pathlib import Path

# variables y contador donde guardar los datos

registros_validos = [] 
registros_invalidos = [] 
leidas_totales = 0 

# control de argumentos en la terminal para que solo haya 2 archivos, uno de entrada y otro de salida

if len(sys.argv) != 3:
    print("argumentos insuficientes")
    print("cantidad correcta de argumentos")
    sys.exit(1)

archivo_entrada = Path(sys.argv[1])
archivo_salida = Path(sys.argv[2])

if not archivo_entrada.exists() or not archivo_entrada.is_file():
    print(f"error, el archivo: {archivo_entrada} no existe o no es un archivo")
    sys.exit(1)

if not archivo_salida.exists() or not archivo_salida.is_dir():
    print(f"error, el archivo {archivo_salida} no existe o no es una carpeta")
    sys.exit(2)

print("rutas verificadas")

try:
    with open(archivo_entrada, "r") as archivo:
        lineas = archivo.readlines()
except FileNotFoundError:
    print(f"no se escontro el archivo deseado en la entrada: {archivo_entrada}")
    sys.exit(1)

for linea in lineas[1:]:
    linea_limpia = linea.strip()

    if not linea_limpia:
        continue

    leidas_totales += 1

    zonas = linea_limpia.split()

    if len(zonas) < 8:
        registros_invalidos.append({
            "linea original": linea_limpia,
            "motivo": "cantidad insuficiente de zonas"
        })
        continue

    fecha = zonas[0]
    hora = zonas[1]
    temperatura = zonas[2]
    humedad = zonas[3]
    presion = zonas[4]
    dir_viento = zonas[5]
    veloci_viento = zonas[6]
    estacion = zonas[7]
    estacion = " ".join(zonas[7:])

    error = None

    if not modulo_de_validaciones.validar_fecha(fecha):
        error = "fecha invalida o imposible"
    elif not modulo_de_validaciones.validar_hora(hora):
        error = "hora invalida o imposible"
    elif not modulo_de_validaciones.validar_el_flotante(temperatura):
        error = "temperatura no numerica"
    elif not modulo_de_validaciones.validar_humedad(humedad):
        error = "humedad imposible"
    elif not modulo_de_validaciones.validar_presion(presion):
        error = "presion no numerica"
    elif not modulo_de_validaciones.validar_dirrecion_viento(dir_viento):
        error = "direccion del viento imposible"
    elif not modulo_de_validaciones.validar_veloci_viento(veloci_viento):
        error = "velocidad del viento negativa o imposible"
    elif not modulo_de_validaciones.validar_estacion(estacion):
        error = "nombre de estacion vacio"

    if error: 
        registros_invalidos.append({
            "linea original": linea_limpia,
            "motivo": error
        })

    else:
        registros_validos.append({
            "fecha": fecha,
            "hora": int(hora),
            "temperatura": float(temperatura),
            "humedad": float(humedad),
            "presion": float(presion),
            "direccion del viento": float(dir_viento),
            "velocidad del viento": float(veloci_viento),
            "estacion": estacion.strip()
        })

formato_json = {
    "resumen del proceso": {
        "lineas_leidas_totales": leidas_totales,
        "total validas": len(registros_validos),
        "total invalidas": len(registros_invalidos)
    },
    "registros_validos": registros_validos,
    "registros_invalidos": registros_invalidos
}

ahora = datetime.now()
marca_de_tiempo = ahora.strftime("%d%m%Y-%H%M%S")
nombre_json = f"mediciones-----{marca_de_tiempo}-----.json"



ruta_final_json = archivo_salida / nombre_json

try:
    with open(ruta_final_json, "w") as archivo_json:
        json.dump(formato_json, archivo_json, indent=2)
except FileNotFoundError:
    print("archivo no existente")
    sys.exit(3)

print("proceso terminado")
print(f"total de lineas leidas: {leidas_totales}")
print(f"archivos validos guardados: {len(registros_validos)}")
print(f"archivos invalidos guardados: {len(registros_invalidos)}")

print(f"Archivo json guardado en: {ruta_final_json.resolve()}")