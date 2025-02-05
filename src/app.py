import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from src.model_loader import predict_image
import ctypes
import os

def hide_console():
    """Oculta la consola en Windows."""
    if os.name == 'nt':
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def open_file():
    """Abre el explorador de archivos y predice la imagen seleccionada."""
    initialpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    initialdir = os.path.join(initialpath, "../photos")
    file_path = filedialog.askopenfilename(initialdir= initialdir , filetypes=[("Image files", "*.jpg *.png *.jpeg *.nef *.dng *.tif")])
    
    if file_path:
        display_image(file_path)
        result_label.config(text="Procesando imagen...")
        root.update()  
        prediction, probability = predict_image(file_path)
        if probability is None:
            result_label.config(text="El modelo aún no está cargado. Por favor, espere.")
        else:
            result_label.config(text=f"Predicción: {prediction} ({probability:.2f}%)")

def display_image(file_path):
    """Muestra la imagen en la interfaz."""
    img = Image.open(file_path).resize((250, 250))  
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

def initialize():
    """Inicializa la interfaz gráfica."""
    global root, image_label, result_label
    
    hide_console()

    script_dir = os.path.dirname(os.path.realpath(__file__)) 
    icon_path = os.path.join(script_dir, "../assets/icons/image_classifier_icon.ico")  

    root = tk.Tk()
    root.title("Clasificador de Imágenes")
    root.iconbitmap(icon_path)
    root.geometry("500x400")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    btn_select = tk.Button(frame, text="Seleccionar Imagen", command=open_file)
    btn_select.pack()

    image_label = tk.Label(root)
    image_label.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    initialize()