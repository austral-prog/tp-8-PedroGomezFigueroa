def get_coordinate(record):

    treasure = record[0]
    cordenada = record[1]
    return cordenada

def convert_coordinate(coordinate):

    nuevacordenada = (coordinate[0],coordinate[1])
    return nuevacordenada

def create_record(azara_record, rui_record):
    
    cordenada = azara_record[1]
    tesoro = azara_record[0]
    nuevacordenada = (cordenada[0],cordenada[1])
    ubicacion = rui_record[0]
    cordenadaa = rui_record[1]
    cuadrante = rui_record[2]

    if nuevacordenada == cordenadaa :
        ubi_final = (tesoro, cordenada, ubicacion, cordenadaa, cuadrante)
        return ubi_final

    else:
        return "not a match"

    return ()
