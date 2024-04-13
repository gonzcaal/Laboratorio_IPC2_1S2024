import re

def extraer_fechas(texto):
    # patron dd/mm/yyyy
    patron_fecha= r'\b\d{1,2}/\d{1,2}/\d{4}\b'

    #buscar las coincidencias del patron en el texto
    fechas_encontradas = re.findall(patron_fecha, texto)
    return fechas_encontradas


def validar_nit(nit):
    #patron para nit #######-#
    patron_nit= r'^\d{7}-\d$'
    
    #verificar si el nit coincide con el patron
    if re.match(patron_nit, nit):
        return True
    else:
        return False
    
def procesar_texto (texto):
    fechas = extraer_fechas(texto)
    nits_validos = [palabra for palabra in texto.split() if validar_nit(palabra)]

    return fechas, nits_validos

texto = "7878787-7 coban Alta verapaz 10ma calle 8va avenida 12/04/2024 texto extra NIT: 9202828-4 23/04/2005"

fechas_encontradas, nits_validos = procesar_texto(texto)

print("Fechas encontradas: ", fechas_encontradas)
print("Nits VALIDOS: ", nits_validos)
