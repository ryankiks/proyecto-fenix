import random
from flask import Flask, render_template_string


app = Flask(__name__)


# Nombres de jugadores predefinidos
NOMBRES = ["Messi", "Cristiano", "Mbappé", "Haaland", "Lewandowski", 
           "De Bruyne", "Vinícius", "Bellingham", "Salah", "Halland"]


def generar_jugador_aleatorio():
    """Genera un jugador con nombre y estadísticas aleatorias."""
    nombre = random.choice(NOMBRES)
    return {
        "nombre": nombre,
        "estadisticas": {
            "Goles": random.randint(0, 50),
            "Asistencias": random.randint(0, 30),
            "Velocidad": round(random.uniform(20.0, 45.0), 1)
        }
    }


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estadísticas de Fútbol</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
        h1 { color: #2c3e50; text-align: center; }
        .jugador { background: #ecf0f1; padding: 20px; border-radius: 10px; }
        .nombre { font-size: 24px; font-weight: bold; color: #e74c3c; text-align: center; }
        .stats { margin-top: 20px; }
        .stat { padding: 10px; margin: 5px 0; background: white; border-radius: 5px; }
        .stat-label { font-weight: bold; }
        .btn { display: block; width: 100%; padding: 15px; background: #3498db; color: white; 
               text-align: center; text-decoration: none; border-radius: 5px; margin-top: 20px; }
    </style>
</head>
<body>
    <h1>⚽ Generador de Jugadores</h1>
    <div class="jugador">
        <div class="nombre">{{ jugador.nombre }}</div>
        <div class="stats">
            {% for clave, valor in jugador.estadisticas.items() %}
            <div class="stat">
                <span class="stat-label">{{ clave }}:</span> {{ valor }}
            </div>
            {% endfor %}
        </div>
    </div>
    <a href="/" class="btn">🔄 Generar Otro Jugador</a>
</body>
</html>
"""


@app.route('/')
def index():
    """Ruta principal que genera un jugador aleatorio."""
    jugador = generar_jugador_aleatorio()
    return render_template_string(HTML_TEMPLATE, jugador=jugador)

    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)