from flask import Flask, render_template
import random

app = Flask(__name__)

# Simulación de Base de Datos de Informes
INFORMES = [
    {"id": 1, "tipo": "Jugador", "titulo": "Análisis Individual: Jude Bellingham", "precio": 15.00, "color": "#16a085"},
    {"id": 2, "tipo": "Comparativo", "titulo": "Haaland vs Mbappé: Duelo de Killers", "precio": 25.00, "color": "#2980b9"},
    {"id": 3, "tipo": "Partido", "titulo": "Final Champions: Análisis Táctico", "precio": 10.00, "color": "#8e44ad"},
    {"id": 4, "tipo": "Competición", "titulo": "Guía Completa Euro 2024", "precio": 45.00, "color": "#d35400"}
]

@app.route('/')
def catalogo():
    return render_template('index.html', informes=INFORMES)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)