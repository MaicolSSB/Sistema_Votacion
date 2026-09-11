# Sistema de Votación - Proyecto Integrador

votos = {} # Diccionario para guardar los votos: {votante: candidato}

# Aquí iremos agregando las funciones en las diferentes ramas

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