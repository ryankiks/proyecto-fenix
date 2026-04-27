from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

INFORMES_BASE = [
    {
        "id": 1, 
        "tipo": "JUGADOR", 
        "titulo": "SCOUTING: Jugadores", 
        "descripcion": "Mapa de calor, zonas de influencia y métricas de llegada.", 
        "precio": 15, 
        "color": "#1db954",
        "img": "https://i.ibb.co/bRNCv2Bq/informe-jugador.png",
        "archivo": "muestra_jugador" # Nombre base sin el _es.pdf
    },
    {
        "id": 2, 
        "tipo": "COMPARATIVO", 
        "titulo": "Comparativa de jugadores", 
        "descripcion": "Comparativa de eficiencia en remate y aceleración punta.", 
        "precio": 25, 
        "color": "#3498db",
        "img": "https://i.ibb.co/gLtk9bG5/informe-comparativo.png",
        "archivo": "muestra_comparativo"
    },
    {
        "id": 3, 
        "tipo": "PARTIDO", 
        "titulo": "Pre y post partido", 
        "descripcion": "Estudio de las transiciones defensivas y el bloque bajo.", 
        "precio": 10, 
        "color": "#9b59b6",
        "img": "https://i.ibb.co/3YjJgnTW/informe-partido.png",
        "archivo": "muestra_partido"
    },
    {
        "id": 4, 
        "tipo": "COMPETICIÓN", 
        "titulo": "Competición", 
        "descripcion": "Análisis de todas las selecciones que participarán en el torneo", 
        "precio": 45, 
        "color": "#e67e22",
        "img": "https://i.ibb.co/qMBQkT2K/informe-competicion.png",
        "archivo": "muestra_mundial"
    }
]

@app.route('/')
def home():
    lang = request.args.get('lang', 'es')
    
    textos_interfaz = {
        "comprar": "Comprar",
        "muestra": "Ver Muestra",
        "titulo_repo": "Repositorio de Informes",
        "gracias_titulo": "¡Gracias por descargar la muestra!",
        "gracias_msg": "¿Te ha gustado? Consigue el informe completo."
    }

    if lang == 'es':
        # Añadimos el sufijo _es a los archivos antes de enviar
        for info in INFORMES_BASE:
            info['archivo_final'] = f"{info['archivo']}_es.pdf"
        return render_template('index.html', informes=INFORMES_BASE, lang=lang, textos=textos_interfaz)

    try:
        translator = GoogleTranslator(source='auto', target=lang)
        textos_traducidos = {k: translator.translate(v) for k, v in textos_interfaz.items()}
        
        informes_traducidos = []
        for info in INFORMES_BASE:
            new_info = info.copy()
            new_info['titulo'] = translator.translate(info['titulo'])
            new_info['descripcion'] = translator.translate(info['descripcion'])
            # Creamos el nombre del archivo según el idioma
            new_info['archivo_final'] = f"{info['archivo']}_{lang}.pdf"
            informes_traducidos.append(new_info)
            
        return render_template('index.html', informes=informes_traducidos, lang=lang, textos=textos_traducidos)
    
    except Exception as e:
        print(f"Error de traducción: {e}")
        for info in INFORMES_BASE:
            info['archivo_final'] = f"{info['archivo']}_es.pdf"
        return render_template('index.html', informes=INFORMES_BASE, lang='es', textos=textos_interfaz)

# EL BLOQUE DE ARRANQUE DEBE IR AQUÍ (AL MARGEN IZQUIERDO)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)