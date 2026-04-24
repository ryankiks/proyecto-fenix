
#!/usr/bin/env python3
"""
Script de información del sistema para el Proyecto Fénix.
Muestra la versión del sistema operativo, versión de Python y mensaje de bienvenida.
"""

import platform
import sys

def obtener_version_sistema():
    """Obtiene información del sistema operativo."""
    return platform.system() + " " + platform.release()

def obtener_version_python():
    """Obtiene la versión de Python."""
    return sys.version

def mostrar_bienvenida():
    """Imprime el mensaje de bienvenida al Proyecto Fénix."""
    print("=" * 50)
    print("       ¡Bienvenido al Proyecto Fénix!       ")
    print("=" * 50)
    print()
    print("🐦 El ave mítica renueva de sus cenizas...")
    print("   Este proyecto simboliza renovación y")
    print("   transformación tecnológica.")
    print()
    print("=" * 50)

def main():
    """Función principal que ejecuta todas las operaciones."""
    print("\n--- Información del Sistema ---\n")
    
    # Versión del sistema operativo
    print(f"Sistema Operativo: {obtener_version_sistema()}")
    
    # Versión de Python
    print(f"Versión de Python: {obtener_version_python()}")
    
    print()
    
    # Mensaje de bienvenida
    mostrar_bienvenida()

if __name__ == "__main__":
    main()