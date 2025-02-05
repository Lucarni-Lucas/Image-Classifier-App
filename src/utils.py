from PIL import Image
import numpy as np

def preprocess_image(file_path):
    """Ajusta el tamaño de la imagen a 32x32"""
    img = Image.open(file_path).convert('RGB')  
    img_resized = img.resize((32, 32))         
    img_array = np.array(img_resized) / 255.0  
    return np.expand_dims(img_array, axis=0)   