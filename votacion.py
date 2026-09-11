# Sistema de Votación - Proyecto Integrador

votos = {} # Diccionario para guardar los votos: {votante: candidato}

def registrar_voto(votante, candidato):
    if votante in votos:
        return f"Error: {votante} ya ha votado anteriormente."
    votos[votante] = candidato
    return f"Voto registrado exitosamente para {candidato}."