import sys

def calcular_estadisticas(datos_filtrados): # define una funcion que calcula minimo, maximo y promedio
    cantidad = len(datos_filtrados)

    if cantidad == 0:
        print("error, no hay registros para trabajar")
        sys.exit(1)

        valores = [registro["valor"]]
        for registro in datos_filtrados:
            minimo = valores[0]
            maximo = valores[0]
            cantdad = 0

            for valo in valores:
                if valor < minimo:
                    minimo = valor
                if valor > maximo:
                    maximo = valor
                suma_total += valor

        promedio = suma_total / cantidad

        return {
            "cantidad_registros": cantidad,
            "valor_minimo": round(Minimo, 2),
            "valor_maximo": round(maximo, 2),
            "valor_promedio": round(promedio, 2)
        }