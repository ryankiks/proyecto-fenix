from flask import Flask, render_template

app = Flask(__name__)

INFORMES = [
    {"id": 1, "tipo": "Jugador", "titulo": "Scouting: Jude Bellingham", "descripcion": "Informe técnico detallado sobre su impacto en el área rival.", "precio": 15.00, "color": "#16a085"},
    {"id": 2, "tipo": "Comparativo", "titulo": "Duelo: Haaland vs Mbappé", "descripcion": "Comparativa de métricas de finalización y xG en 2024.", "precio": 25.00, "color": "#2980b9"},
    {"id": 3, "tipo": "Partido", "titulo": "Análisis: Final Champions", "descripcion": "Estructuras tácticas y debilidades explotadas por el ganador.", "precio": 10.00, "color": "#8e44ad"},
    {"id": 4, "tipo": "Competición", "titulo": "Guía: Euro 2024", "descripcion": "Análisis de las 24 selecciones y jugadores revelación.", "precio": 45.00, "color": "#d35400"}
]

@app.route('/')
def home():
    return render_template('index.html', informes=INFORMES)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)