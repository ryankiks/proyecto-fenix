from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    # Generamos datos aleatorios como en tu script original
    nombre = random.choice(["Kike", "Joaquín", "Messi", "Haaland", "Mbappé"])
    goles = random.randint(0, 50)
    asistencias = random.randint(0, 20)
    velocidad = round(random.uniform(25.0, 38.0), 1)

    # Enviamos los datos a la plantilla HTML
    return render_template('index.html', 
                           nombre=nombre, 
                           goles=goles, 
                           asistencias=asistencias, 
                           velocidad=velocidad)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)