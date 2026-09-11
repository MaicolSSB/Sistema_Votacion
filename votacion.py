# Sistema de Votación - Proyecto Integrador

votos = {} # Diccionario para guardar los votos: {votante: candidato}

# Aquí iremos agregando las funciones en las diferentes ramas

def reiniciar_votacion():
    if not votos:
        return "No hay votos para reiniciar."
    
    # Guardar historial en un archivo
    with open("historial_votacion.txt", "a") as archivo:
        archivo.write("--- Nueva Votación ---\n")
        for votante, candidato in votos.items():
            archivo.write(f"{votante} votó por {candidato}\n")
        archivo.write("\n")
    
    votos.clear()
    return "Votación reiniciada y historial guardado en 'historial_votacion.txt'."