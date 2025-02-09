from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        try:
            desde = int(request.form["desde"])
            hasta = int(request.form["hasta"])
            if desde <= hasta:
                resultado = random.randint(desde, hasta)
            else:
                resultado = "Error: El valor 'Desde' debe ser menor o igual a 'Hasta'."
        except ValueError:
            resultado = "Error: Ingrese números válidos."

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
