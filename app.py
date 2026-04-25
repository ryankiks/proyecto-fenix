import random


def generar_estadisticas():
    """Genera 3 estadísticas aleatorias para un jugador."""
    return {
        "Goles": random.randint(0, 50),
        "Asistencias": random.randint(0, 30),
        "Velocidad": round(random.uniform(20.0, 45.0), 1)
    }


def guardar_jugador(nombre, estadisticas, archivo="jugadores.txt"):
    """Guarda los datos del jugador en el archivo."""
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"Jugador: {nombre}\n")
        for clave, valor in estadisticas.items():
            f.write(f"  {clave}: {valor}\n")
        f.write("\n")


def main():
    nombre = input("Introduce el nombre del jugador de fútbol: ")
    estadisticas = generar_estadisticas()
    guardar_jugador(nombre, estadisticas)
    
    print(f"\n✅ Jugador '{nombre}' guardado en jugadores.txt")
    
    # Accedemos a los goles dentro del diccionario 'estadisticas'
    goles = estadisticas["Goles"] 
    print(f"   Goles: {goles}")

    # Ahora el IF está dentro de main y usa la variable correcta
    if goles > 20:
        print("   ⭐ ¡Es un delantero de élite!")
    else:
        print("   🏃 Es un buen jugador, pero necesita mejorar su puntería.")

    print(f"   Asistencias: {estadisticas['Asistencias']}")
    print(f"   Velocidad: {estadisticas['Velocidad']} km/h")


if __name__ == "__main__":
    main()