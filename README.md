# Sistema de Votación - Proyecto Integrador

Este proyecto es un sistema de votación simple desarrollado en Python, aplicando ramas y versionado con Git.

## Funciones del Sistema

- **`registrar_voto(votante, candidato)`**: Registra el voto de una persona. Valida que un votante no vote dos veces usando un diccionario. *(Desarrollado por: Maicol)*
- **`ver_resultados()`**: Muestra los resultados de la votación con sus respectivos porcentajes y anuncia al ganador. *(Desarrollado por: Maicol)*
- **`reiniciar_votacion()`**: Guarda el historial de la votación en un archivo de texto (`historial_votacion.txt`) y reinicia el conteo. *(Desarrollado por: Maicol)*

## Versionado
- **v0.1-registro**: Función de registro de votos.
- **v0.2-resultados**: Función de visualización de resultados.
- **v0.3-reinicio**: Función de reinicio y guardado de historial.
- **v1.0**: Versión final con la mejora de anuncio del ganador.