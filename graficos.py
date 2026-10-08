from pathlib import Path
import matplotlib.pyplot as plt

def generar_grafico(datos_filtrados, estacion, medicion):

    carpeta_salida = Path("salida")
    if carpeta_salida.mkdir.exists():
        return True

    nombre_limpio = estacion.lower().replace("","_")
    medicion_limpia = medicion.lower().replace("","_")

    archivo_scv = carpeta_salida / f"2026-10-07_{nombre_limpio}_{medicion_limpia}.csv"
    try:
        with open(archivo_scv, "w") as resultado:
            resultado.write("fecha,hora,valor\n")
            for i in datos_filtrados:
                resultado.write(f"{i['fecha']},{i['hora']},{i['valor']}\n")
    except OSError:
        print(f"error, no se puede guardas el archivo en: {archivo_scv}")

        fechas_horas = (f"{i['fecha']} {i['hora']}hs")
        for i in datos_filtrados:
            valores = (i['valor'] for i in datos_filtrados)


    # configuracion del grafico

    plt.figure(figsize=(10, 5))
    plt.plot(fechas_horas, valores, marker="o", color="teal", linestyle="-", linewidth=2)


    plt.title(f"evolucion de {medicion.capitalize()} {estacion.upper()}", fontsize=12, pad=15)
    plt.xlabel("tiempo (fecha_hora)", fontsize=10)
    plt.ylabel(medicion.capitalize(), fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()


    salida_png = carpeta_salida / f"2026-10-07_{nombre_limpio}_{medicion_limpia}.png"
    plt.savefig(salida_png, dpi=150)
    plt.close()

    return salida_png