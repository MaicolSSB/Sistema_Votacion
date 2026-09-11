# Sistema de Votación - Proyecto Integrador

votos = {} # Diccionario para guardar los votos: {votante: candidato}

def registrar_voto(votante, candidato):
    if votante in votos:
        return f"Error: {votante} ya ha votado anteriormente."
    votos[votante] = candidato
    return f"Voto registrado exitosamente para {candidato}."

def ver_resultados():
    if not votos:
        return "No hay votos registrados."
    
    total_votos = len(votos)
    conteo = {}
    for candidato in votos.values():
        conteo[candidato] = conteo.get(candidato, 0) + 1
        
    resultado = "--- RESULTADOS ---\n"
    for candidato, cantidad in conteo.items():
        porcentaje = (cantidad / total_votos) * 100
        resultado += f"{candidato}: {cantidad} votos ({porcentaje:.2f}%)\n"
    return resultado