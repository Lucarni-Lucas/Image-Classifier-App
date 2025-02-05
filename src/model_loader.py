from tensorflow import keras
from src.utils import preprocess_image
import os
import numpy as np
import threading

model = None
class_names = ["Avión", "Automóvil", "Pájaro", "Gato", "Venado", "Perro", "Rana", "Caballo", "Barco", "Camión"]


def try_load_model():
    """Carga el modelo"""
    global model
    try:
        script_dir = os.path.dirname(os.path.realpath(__file__)) 
        model_path = os.path.join(script_dir, "../model/model_cifar10.keras")  
        model = keras.models.load_model(model_path)
        print("Modelo cargado correctamente.")  
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")

# Inicia la carga del modelo en segundo plano
threading.Thread(target=try_load_model, daemon=True).start()

def predict_image(file_path):
    """Realiza la predicción sobre una imagen."""
    global model
    if model is None:
        return "El modelo aún no está cargado.", None
    
    img_array = preprocess_image(file_path)
    predictions = model.predict(img_array)[0]
    predicted_class = class_names[np.argmax(predictions)]
    probability = predictions[np.argmax(predictions)] * 100
    return predicted_class, probability

