# <h1 align="center">_SD_ANALYTICS_</h1>
<p align="center">
  <img src="images/SD_analytics.png"  height="400">
<p align="center">

## Índice

1. [Descripción](#Descripción-Proyectos)
2. [Regresión Lineal con Red Neuronal](#Regresión-Lineal-con-Red-Neuronal)
3. [Predicción Multiclase](#Predicción-Multiclase)
4. [Análisis de Tenis](#Análisis-de-Tenis)
5. [Demo Modelos en Acción](#Demo-Modelos-en-Acción)
6. [Stack de tecnologías y herramientas](#Stack-de-tecnologías-y-herramientas)
7. [Colaboradores](#Colaboradores)

## Descripción Proyectos

## Regresión Lineal con Red Neuronal

Preparación de datos: se establece una relación lineal utilizando un peso de 0,8 y un sesgo de 0,4 para crear un conjunto de datos sintéticos, que luego se divide en conjuntos de entrenamiento (80 %) y de prueba (20 %).

Visualización: se define una función plot_predictions para visualizar los datos de entrenamiento, los datos de prueba y cualquier predicción realizada por el modelo, inicialmente trazando los datos de entrenamiento y prueba sin predicciones.

Definición del modelo: se define un modelo de red neuronal (model_1) utilizando nn.Sequential de PyTorch, que consta de dos capas completamente conectadas con 10 neuronas cada una y una capa de salida con 1 neurona.

Bucle de entrenamiento: el modelo se entrena durante 1000 épocas utilizando la pérdida L1 y el optimizador Adam, imprimiendo la pérdida de entrenamiento y prueba cada 100 épocas para monitorear el progreso del entrenamiento.

Evaluación y visualización: después del entrenamiento, el modelo se evalúa en modo de inferencia para predecir los datos de prueba y los resultados se visualizan utilizando la función plot_predictions, lo que permite la comparación entre las etiquetas de prueba reales y los valores predichos.

## Predicción Multiclase

Objetivo: Clasificar los puntos de datos en una de cuatro clases distintas mediante una red neuronal en PyTorch.

Generación de datos: Conjunto de datos sintéticos creado mediante make_blobs, con 4 clústeres que representan diferentes clases en un espacio de características 2D.
Arquitectura del modelo: Una red neuronal de propagación hacia adelante (BlobModel) con una capa de entrada de 2 características, dos capas ocultas con activación ReLU y una capa de salida para 4 clases.

Proceso de entrenamiento: Utiliza pérdida de entropía cruzada para la clasificación de múltiples clases, el optimizador Adam para actualizaciones de parámetros y entrena durante 100 épocas.

Resultados: Logra una alta precisión en este caso ideal (hasta el 100 % en datos de prueba) y visualiza los límites de decisión, lo que demuestra una distinción de clases efectiva en el conjunto de datos.

## Análisis de Tenis


Procesamiento de video: el script lee un archivo de video de un partido deportivo, detectando los movimientos del jugador y la pelota usando dos modelos CNN separados: un rastreador de jugadores que usa un modelo YOLOv8 y un rastreador de pelotas con un modelo entrenado diferente.

Detección de tiros de pelota: identifica cuadros específicos donde se lanza la pelota, calcula las distancias recorridas por la pelota entre cuadros y convierte estas distancias de píxeles en medidas del mundo real en metros.

Estadísticas de jugadores: el programa recopila y actualiza las estadísticas de dos jugadores, incluyendo la cantidad de tiros realizados, la velocidad total y del último tiro, y la velocidad del jugador contrario cuando se lanza la pelota.

Visualización de datos: visualiza los jugadores detectados, las trayectorias de la pelota, las líneas de la cancha y las estadísticas de los jugadores en los cuadros de video, creando un video de salida anotado que muestra la dinámica del juego.

Generación de salida: finalmente, el script guarda el video procesado, incorporando todas las visualizaciones y los números de cuadro para un mejor análisis y comprensión del desempeño de los jugadores durante el partido.

## Demo Modelos en Acción

| Video sin aplicar Deep Learning                                                                     | 
| ----------------------------------------------------------------------------------------------- |
| <img src="images/tennis_animation_3.gif" alt="Interface Animation"  width="100%" /> |


| Video con Deep Learning Aplicado                                                                     | 
| ----------------------------------------------------------------------------------------------- |
| <img src="images/tennis_animation_4.gif" alt="Interface Animation"  width="100%" /> |

## Stack de tecnologías y herramientas

|  Librería/herramienta    |   Logo                                    | Descripción                                                                                                           |
|----------------------|-----------------------------------------|----------------------------------------------|
| **Pandas**   |      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png" width="100">   | Librería de Python para manipulación y análisis de datos.|
| **PyTorch** | <img src="https://upload.wikimedia.org/wikipedia/commons/1/10/PyTorch_logo_icon.svg" width="100"> | Framework de aprendizaje profundo de código abierto que proporciona un apoyo flexible y potente para el desarrollo de modelos de aprendizaje automático. |
| **Matplotlib**|<img src="https://matplotlib.org/_static/logo_light.svg" width="100">| Librería usada para la generación de gráficos en dos dimensiones.|
|**Seaborn**|<img src="https://seaborn.pydata.org/_images/logo-tall-lightbg.svg" width="100"> | Librería de Python creada sobre matplotlib, usada para crear gráficos estadísticos.|
| **Jupyter**|<img src="https://jupyter.org/assets/homepage/main-logo.svg" width="65">| Software gratuito, estándares abiertos y servicios web para informática interactiva en todos los lenguajes de programación.|
| **Visual Studio Code**|<img src="https://static-00.iconduck.com/assets.00/visual-studio-code-icon-512x506-2fdb6ar6.png" width="70">| Editor de código fuente.|
| **Colaboratory con Python**|<img src="https://colab.research.google.com/img/colab_favicon_256px.png" width="60">| Plataforma de Google basada en Jupyter Notebooks, junto con las librerías de Python para análisis de datos como Pandas y Matplotlib.|
| **Power Point**|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Microsoft_PowerPoint_2013-2019_logo.svg/610px-Microsoft_PowerPoint_2013-2019_logo.svg.png" width="100">| Microsoft PowerPoint (PPT) es un software de ofimática diseñado para realizar presentación de diapositivas.|
| **Python**|<img src="https://seeklogo.com/images/P/python-logo-A32636CAA3-seeklogo.com.png" width="50">| Lenguaje de programación utilizado para análisis de datos y desarrollo de aplicaciones.|
| **GitHub**|<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" width="100">| Plataforma de desarrollo colaborativo para proyectos de software.|
| **Google Drive**|<img src="https://upload.wikimedia.org/wikipedia/commons/1/12/Google_Drive_icon_%282020%29.svg" width="100"> | Servicio de alojamiento y sincronización de archivos.|
| **Streamlit** | <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width="100"> | Streamlit es una herramienta de código abierto diseñada para crear aplicaciones web interactivas y visualizaciones de datos de manera rápida y sencilla utilizando Python.|


## Colaboradores

|                         | Nombre   |   Rol                    | GitHub & LinkedIn                                                                                                                                                                                          |
| ----------------------------- | -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img width="60" height="60" src="https://github.com/Sergius-DS.png" alt="Sergius-DS" /> | Sergio Rivera Bustamante | Data Scientist | [![Github](https://skillicons.dev/icons?i=github)](https://github.com/Sergius-DS) [![Linkedin](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/sergio-rivera-bustamante-6642b836/)                         |
|                               |

