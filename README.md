# Image Classifier App

Este proyecto es una aplicación sencilla que utiliza un modelo previamente entrenado en el dataset **CIFAR-10** para clasificar imágenes en una de las siguientes 10 categorías:

- Avión
- Automóvil
- Pájaro
- Gato
- Venado
- Perro
- Rana
- Caballo
- Barco
- Camión

La aplicación tiene una interfaz gráfica amigable que permite a cualquier persona, incluso sin conocimientos de programación, seleccionar una imagen de su computadora y recibir una predicción junto con la probabilidad asociada.


## Características principales
1. **Interfaz gráfica**: Permite seleccionar imágenes fácilmente y realizar predicciones con un solo clic.
2. **Modelo preentrenado**: Utiliza un modelo previamente entrenado en el dataset CIFAR-10.
3. **Compatibilidad con imágenes de cualquier resolución**: Convierte automáticamente las imágenes cargadas a un formato aceptado por el modelo (32x32 píxeles).
4. **Archivo ejecutable**: No es necesario instalar Python ni dependencias adicionales; simplemente descarga y ejecuta el archivo `.exe`.


## Cómo usar la aplicación
1. Descarga este repositorio.
2. Ejecuta el archivo descargado `image_classifier_app.exe` (puedes hacer doble clic).
3. En la ventana que se abre:
    - Haz clic en el botón "**Seleccionar imagen**" para elegir una foto de tu computadora.
    - Puedes elegir una de las fotos de la carpeta `photos` que se encuentra el directorio raíz.
4. El nombre de la clase predicha y la probabilidad asociada aparecerán en la ventana.


## Requisitos
La aplicación ya incluye todo lo necesario para funcionar, pero si decides ejecutar el código fuente, necesitas:

1. Python 3.8 a 3.11
2. Las siguientes librerías (incluidas en `requirements.txt`):
    - tensorflow
    - numpy
    - Pillow

    Instala las dependencias con:
    ```bash
    pip install -r requirements.txt
    ```
3. Ejecutar con Python `launcher.py` 

## Nota sobre el archivo ejecutable
El archivo `image_classifier_app.exe` no está firmado digitalmente, lo que puede hacer que algunos sistemas operativos lo identifiquen como un posible malware. Esto no significa que el archivo sea peligroso. Si ves una advertencia al intentar ejecutarlo:

1. Haz clic en "**Más información**".
2. Selecciona "**Ejecutar de todas formas**".

Este comportamiento es común en aplicaciones no firmadas. Si tienes dudas, puedes ejecutar el código fuente directamente.

