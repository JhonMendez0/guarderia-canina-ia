from flask import Flask, request, jsonify, send_file
from pathlib import Path
import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent

# =========================
# CARGAR O CREAR DATASET
# =========================

try:

    # Intentar cargar CSV existente
    df = pd.read_csv(BASE_DIR / "perros.csv")

    print("CSV cargado correctamente")

except:

    print("Creando dataset nuevo...")

    n = 100

    energia = np.random.randint(1, 11, n)
    tamano = np.random.randint(1, 4, n)
    edad = np.random.randint(1, 10, n)
    peso = np.random.randint(5, 40, n)
    socializacion = np.random.randint(1, 11, n)

    df = pd.DataFrame({

        "energia": energia,
        "tamano": tamano,
        "edad": edad,
        "peso": peso,
        "socializacion": socializacion

    })

    # =========================
    # CLASIFICAR COMPORTAMIENTO
    # =========================

    def clasificar(fila):

        if fila["socializacion"] <= 3 and fila["energia"] >= 7:
            return 0

        elif fila["socializacion"] <= 5:
            return 1

        else:
            return 2

    df["comportamiento"] = df.apply(
        clasificar,
        axis=1
    )

    # Guardar CSV
    df.to_csv(BASE_DIR / "perros.csv", index=False)

# =========================
# VARIABLES DEL MODELO
# =========================

X = df[[
    "energia",
    "tamano",
    "edad",
    "peso",
    "socializacion"
]].values

y = df["comportamiento"].values

# =========================
# ENTRENAMIENTO
# =========================

modelo = LogisticRegression(max_iter=1000)

modelo.fit(X, y)

print("Modelo entrenado correctamente")

# =========================
# RUTA PRINCIPAL
# =========================

@app.route("/")
def home():

    return send_file(BASE_DIR / "home.html")

@app.route("/analisis")
def analisis():
    return send_file(BASE_DIR / "index.html")

# =========================
# HISTORIAL
# =========================

@app.route("/historial")
def historial():

    datos = []

    for _, fila in df.iterrows():

        if fila["comportamiento"] == 0:
            resultado = "Agresivo"

        elif fila["comportamiento"] == 1:
            resultado = "Nervioso"

        else:
            resultado = "Tranquilo"

        datos.append({

            "energia": int(fila["energia"]),
            "socializacion": int(fila["socializacion"]),
            "resultado": resultado

        })

    return jsonify(datos)

# =========================
# PREDICCIÓN
# =========================

@app.route("/predecir", methods=["POST"])
def predecir():

    global df

    data = request.json

    nuevo_perro = np.array([[
        data["energia"],
        data["tamano"],
        data["edad"],
        data["peso"],
        data["socializacion"]
    ]])

    # Predicción
    pred = modelo.predict(nuevo_perro)

    # Probabilidades
    prob = modelo.predict_proba(nuevo_perro)

    # Interpretación
    if pred[0] == 0:

        mensaje = "AGRESIVO"

    elif pred[0] == 1:

        mensaje = "NERVIOSO"

    else:

        mensaje = "TRANQUILO"

    # =========================
    # GUARDAR NUEVO PERRO
    # =========================

    nuevo_registro = {

        "energia": data["energia"],
        "tamano": data["tamano"],
        "edad": data["edad"],
        "peso": data["peso"],
        "socializacion": data["socializacion"],
        "comportamiento": int(pred[0])

    }

    # Agregar al dataframe
    df = pd.concat([
        df,
        pd.DataFrame([nuevo_registro])
    ], ignore_index=True)

    # Guardar CSV actualizado
    df.to_csv(BASE_DIR / "perros.csv", index=False)

    print("Nuevo perro agregado")

    return jsonify({

        "resultado": mensaje,
        "confianza": float(max(prob[0]))

    })

# =========================
# EJECUTAR APP
# =========================

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=False)