import sys
from pathlib import Path

import app
import graficos
import estadisticas

def main():

    if len(sys.argv) != 4:
        print("error, argumentos insuficientes")
        sys.exit(1)

    argumento_consola = sys.argv[1]
    ruta_json = Path(argumento_consola).resolve()

    ruta_json = sys.argv[1]
    estacion = sys.argv[2]
    medicion = sys.argv[3]

    registros = app.cargar_json(str(ruta_json))

    filtrados = app.filtrar_datos(registros, estacion, medicion)

    reporte_estadistico = estadisticas.calcular_estadisticas(filtrados)

    ruta_grafica = graficos.generar_grafico(filtrados, estacion, medicion)

    print("\nproceso completado")
    print(f"cantidad de registros: {reporte_estadistico['cantidad_registros']}")
    print(f"valor minimo: {reporte_estadistico['valor_minimo']}")
    print(f"valor maximo: {reporte_estadistico['valor_maximo']}")

    print(f"valor promedio: {reporte_estadistico['valor_promedio']}")

    print("\nprimeros registros filtrados:")
    for i in filtrados[:3]: # Mostramos los primeros 3 para cumplir la rúbrica
        print(f"Fecha: {i['fecha']}  Hora: {i['hora']}  Valor: {i['valor']}")

    print(f"\n Grafica guardada en: {ruta_grafica}")

main()