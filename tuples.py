def get_coordinate(record):

    treasure = record[0]
    cordenada = record[1]
    return cordenada

def convert_coordinate(coordinate):

    nuevacordenada = (coordinate[0],coordinate[1])
    return nuevacordenada

def create_record(azara_record, rui_record):
    tesoro, coordenadaA=azara_record
    ubicación, coordenadaR, cuadrante=rui_record
    NUM,LETRA=coordenadaA
    conjunto= NUM,LETRA
    if conjunto==coordenadaR:
        return tesoro, coordenadaA, ubicación, coordenadaR, cuadrante
    else:
        return "not a match"
