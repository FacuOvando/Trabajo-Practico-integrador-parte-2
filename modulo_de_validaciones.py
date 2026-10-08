def validar_el_flotante(valor_str):
    try:
        float(valor_str)
        return True
    except ValueError:
        return False

def validar_fecha(fecha_str):

    if not fecha_str.isnumeric():
        return False
    if len(fecha_str) != 8:
        return False
    dia = int(fecha_str[0:2])
    mes = int(fecha_str[2:4])
    anio = int(fecha_str[4:8])
    if mes < 1 or mes > 12 or dia < 1 or dia > 31 or anio >= 2027:
        return False
    return True

def validar_hora(hora_str):
    if not hora_str.isnumeric():
        return False
    return 0 <= int(hora_str) <= 23

def validar_humedad(humedad_str):
    if not validar_el_flotante(humedad_str):
        return False 
    return 0 <= float(humedad_str) <= 100

def validar_presion(presion_str):
    try:
        float(presion_str)
        return True
    except ValueError:
        return False

def validar_dirrecion_viento(dir_viento_str):
    if not validar_el_flotante(dir_viento_str):
        return False
    return 0 <= float(dir_viento_str) <= 360

def validar_veloci_viento(velo_viento_str):
    if not validar_el_flotante(velo_viento_str):
        return False
    return float(velo_viento_str) >= 0

def validar_estacion(nombre_estacion_str):
    return len(nombre_estacion_str.strip()) > 0