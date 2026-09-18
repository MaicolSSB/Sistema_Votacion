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
    
    # --- MEJORA ADICIONAL: Anunciar al ganador ---
    ganador = max(conteo, key=conteo.get)
    resultado += f"\n¡El ganador es {ganador} con {conteo[ganador]} votos!"
    
    return resultado

def reiniciar_votacion():
    if not votos:
        return "No hay votos para reiniciar."
    
    with open("historial_votacion.txt", "a") as archivo:
        archivo.write("--- Nueva Votación ---\n")
        for votante, candidato in votos.items():
            archivo.write(f"{votante} votó por {candidato}\n")
        archivo.write("\n")
    
    votos.clear()
    return "Votación reiniciada y historial guardado en 'historial_votacion.txt'."



# --- BLOQUE DE PRUEBA (solo para verificar que funciona) ---
if __name__ == "__main__":
    print("--- PRUEBA 1: Registrar votos ---")
    print(registrar_voto("Ana", "Candidato A"))
    print(registrar_voto("Luis", "Candidato B"))
    print(registrar_voto("Ana", "Candidato A"))  # Debe dar error (voto duplicado)
    
    print("\n--- PRUEBA 2: Ver resultados ---")
    print(ver_resultados())
    
    print("\n--- PRUEBA 3: Reiniciar votación ---")
    print(reiniciar_votacion())
    
    print("\n--- PRUEBA 4: Ver resultados después de reiniciar ---")
    print(ver_resultados())  # Debe decir que no hay votos
