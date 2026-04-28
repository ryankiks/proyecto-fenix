from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

# --- CONFIGURACIÓN DE DATOS: MARKETPLACE ---
INFORMES_BASE = [
    {
        "id": 1, 
        "tipo": "JUGADOR", 
        "titulo": "SCOUTING: JUDE BELLINGHAM", 
        "descripcion": "Mapa de calor, zonas de influencia y métricas de llegada.", 
        "precio": 15, 
        "color": "#1db954",
        "img": "https://i.ibb.co/bRNCv2Bq/informe-jugador.png",
        "archivo_base": "muestra_jugador"
    },
    {
        "id": 2, 
        "tipo": "COMPARATIVO", 
        "titulo": "DUELO: HAALAND VS MBAPPÉ", 
        "descripcion": "Comparativa de eficiencia en remate y aceleración punta.", 
        "precio": 25, 
        "color": "#3498db",
        "img": "https://i.ibb.co/gLtk9bG5/informe-comparativo.png",
        "archivo_base": "muestra_comparativo"
    },
    {
        "id": 3, 
        "tipo": "PARTIDO", 
        "titulo": "FINAL CHAMPIONS", 
        "descripcion": "Estudio de las transiciones defensivas y el bloque bajo.", 
        "precio": 10, 
        "color": "#9b59b6",
        "img": "https://i.ibb.co/3YjJgnTW/informe-partido.png",
        "archivo_base": "muestra_partido"
    }
]

# --- CONFIGURACIÓN DE DATOS: SCOUTIC CRM ---
JUGADORES_SCOUTIC = [
    {"nombre": "Florian Wirtz", "posicion": "MCO", "equipo": "Bayer Leverkusen", "estado": "En progreso"},
    {"nombre": "Lamine Yamal", "posicion": "ED", "equipo": "FC Barcelona", "estado": "Pendiente"},
    {"nombre": "Viktor Gyökeres", "posicion": "DC", "equipo": "Sporting CP", "estado": "Terminado"}
]

# --- RUTA 1: MARKETPLACE (Página de inicio) ---
@app.route('/')
def home():
    lang = request.args.get('lang', 'es')
    
    textos_interfaz = {
        "titulo_repo": "Scoutic Marketplace",
        "muestra": "Ver Muestra",
        "comprar": "Comprar",
        "btn_crm": "Mi CRM"
    }

    if lang == 'es':
        # Añadimos el nombre del archivo final para español
        for info in INFORMES_BASE:
            info['archivo_final'] = f"{info['archivo_base']}_es.pdf"
        return render_template('index.html', informes=INFORMES_BASE, lang=lang, textos=textos_interfaz)

    try:
        translator = GoogleTranslator(source='auto', target=lang)
        textos_trad = {k: translator.translate(v) for k, v in textos_interfaz.items()}
        
        informes_trad = []
        for info in INFORMES_BASE:
            new_info = info.copy()
            new_info['titulo'] = translator.translate(info['titulo'])
            new_info['descripcion'] = translator.translate(info['descripcion'])
            new_info['archivo_final'] = f"{info['archivo_base']}_{lang}.pdf"
            informes_trad.append(new_info)
            
        return render_template('index.html', informes=informes_trad, lang=lang, textos=textos_trad)
    
    except Exception as e:
        print(f"Error traducción Marketplace: {e}")
        return render_template('index.html', informes=INFORMES_BASE, lang='es', textos=textos_interfaz)

# --- RUTA 2: SCOUTIC CRM (Panel de Gestión) ---
@app.route('/scoutic')
def crm():
    lang = request.args.get('lang', 'es')
    
    textos_scoutic = {
        "titulo_crm": "Scoutic | Gestión de Talento",
        "nuevo_jugador": "Nuevo Informe",
        "subtitulo": "Panel de control de analista"
    }

    if lang == 'es':
        # Renderizamos scoutic.html porque así se llama tu archivo según la imagen
        return render_template('scoutic.html', jugadores=JUGADORES_SCOUTIC, lang=lang, textos=textos_scoutic)

    try:
        translator = GoogleTranslator(source='auto', target=lang)
        textos_trad = {k: translator.translate(v) for k, v in textos_scoutic.items()}
        
        jugadores_trad = []
        for j in JUGADORES_SCOUTIC:
            new_j = j.copy()
            new_j['estado'] = translator.translate(j['estado'])
            jugadores_trad.append(new_j)

        return render_template('scoutic.html', jugadores=jugadores_trad, lang=lang, textos=textos_trad)

    except Exception as e:
        print(f"Error traducción CRM: {e}")
        return render_template('scoutic.html', jugadores=JUGADORES_SCOUTIC, lang='es', textos=textos_scoutic)

# --- BLOQUE DE ARRANQUE ---
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)