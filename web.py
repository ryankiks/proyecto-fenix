from flask import Flask, render_template

app = Flask(__name__)

INFORMES = [
    {
        "id": 1, 
        "tipo": "JUGADOR", 
        "titulo": "SCOUTING: JUDE BELLINGHAM", 
        "descripcion": "Mapa de calor, zonas de influencia y métricas de llegada.", 
        "precio": 15, 
        "color": "#1db954", # Verde Bellingham
        "img": "https://i.ibb.co/bRNCv2Bq/informe-jugador.png", # Aquí pondremos la URL de tu imagen 1
        "archivo": "muestra_jugador.pdf"
    },
    {
        "id": 2, 
        "tipo": "COMPARATIVO", 
        "titulo": "DUELO: HAALAND VS MBAPPÉ", 
        "descripcion": "Comparativa de eficiencia en remate y aceleración punta.", 
        "precio": 25, 
        "color": "#3498db", # Azul Haaland
        "img": "https://i.ibb.co/gLtk9bG5/informe-comparativo.png", # Aquí la URL de tu imagen 2
        "archivo": "#"
    },
    {
        "id": 3, 
        "tipo": "PARTIDO", 
        "titulo": "FINAL CHAMPIONS", 
        "descripcion": "Estudio de las transiciones defensivas y el bloque bajo.", 
        "precio": 10, 
        "color": "#9b59b6", # Morado Champions
        "img": "https://i.ibb.co/3YjJgnTW/informe-partido.png", # Aquí la URL de tu imagen 3
        "archivo": "#"
    },
    {
        "id": 4, 
        "tipo": "COMPETICIÓN", 
        "titulo": "Mundial 2026", 
        "descripcion": "Análisis de todas las selecciones que participarán en el torneo", 
        "precio": 45, 
        "color": "#e67e22", # Naranja Euro
        "img": "https://i.ibb.co/qMBQkT2K/informe-competicion.png", # Aquí la URL de tu imagen 4
        "archivo": "#"
    }
]

@app.route('/')
def home():
    return render_template('index.html', informes=INFORMES)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)