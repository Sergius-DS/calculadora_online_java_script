# <h1 align="center">_SD_ANALYTICS_</h1>
<p align="center">
  <img src="images/SD_analytics.png"  height="400">
<p align="center">

## Descripción Proyectos

🚀 Funcionamiento y Arquitectura
La aplicación combina cuatro tecnologías clave, cada una cumpliendo un rol bien definido, siguiendo el modelo tradicional de desarrollo web:

1. Estructura (HTML) 🏗️
El HTML proporciona el esqueleto y la disposición de la interfaz de la calculadora.

Contenedor principal: Un div que agrupa y centra los elementos.

Entradas de usuario: Dos campos de texto (<input type="number">) para los operandos (firstNumber y secondNumber).

Selector de Operación: Un menú desplegable (<select id="operator">) para elegir la operación aritmética (**, -, *, /).

Interacción: Un botón (<button id="calculate">) que inicia el proceso de cálculo.

Salida: Un párrafo (<p id="result">) reservado para mostrar el resultado final o mensajes al usuario.

2. Estilo (CSS) ✨
El CSS se aplica directamente dentro del HTML para asegurar que la calculadora tenga una presentación visual limpia y responsive, independientemente del entorno de Streamlit.

Diseño: Centrado, bordes redondeados y una sombra sutil para simular una caja física.

Consistencia: Aplica un estilo uniforme a las entradas, el selector y el botón.

Énfasis: Destaca el botón "Calculate" con un color de fondo verde (#4CAF50).

3. Lógica (JavaScript) 🧠
El JavaScript es el motor funcional que realiza los cálculos y maneja la interacción del usuario.

Captura de DOM: El script primero localiza los elementos HTML por su ID.

Función calculate(): Se ejecuta al hacer clic en el botón.

Convierte los valores de entrada a números (parseFloat).

Valida las entradas para evitar errores (isNaN).

Utiliza una sentencia switch para aplicar la operación correcta.

Incluye manejo de excepciones para la división por cero.

Actualiza dinámicamente el contenido del elemento result.

Manejador de Eventos: El método addEventListener('click', calculate) es crucial, ya que enlaza el evento de clic del botón directamente a la ejecución de la función de cálculo.

4. Presentación (Streamlit / Python) 🐍
Streamlit actúa como el host de la aplicación, permitiendo que un código web independiente se ejecute dentro de un marco de aplicación de Python.

Incrustación: El código HTML, CSS y JavaScript se guarda como una única cadena de texto en una variable de Python (html_code).

Renderizado: La función clave es components.html(html_code, height=450). Esta función le indica a Streamlit que renderice el contenido de la cadena dentro de un iframe seguro, haciendo que la calculadora sea completamente interactiva y funcional dentro de la aplicación de Streamlit.

## 🛠️ Stack de tecnologías y herramientas

Tecnología,Rol en el Proyecto
Streamlit,Framework principal de Python para alojar la aplicación web.
HTML5,Estructura los elementos de la calculadora.
CSS3,Define el aspecto visual y el diseño.
JavaScript,Implementa la lógica de cálculo y la interactividad.
Python,Contiene el script que utiliza Streamlit para incrustar el componente.

## Colaboradores

|                         | Nombre   |   Rol                    | GitHub & LinkedIn                                                                                                                                                                                          |
| ----------------------------- | -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img width="60" height="60" src="https://github.com/Sergius-DS.png" alt="Sergius-DS" /> | Sergio Rivera Bustamante | Data Scientist | [![Github](https://skillicons.dev/icons?i=github)](https://github.com/Sergius-DS) [![Linkedin](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/sergio-rivera-bustamante-6642b836/)                         |
|                               |

