# 🚀 SD_ANALYTICS

---

## 🏗️ Descripción del Proyecto: Calculadora Streamlit/Web

Este proyecto demuestra la incrustación de una aplicación web frontend tradicional (HTML, CSS, JavaScript) dentro de un framework de aplicación de datos de Python (Streamlit). La aplicación funciona como una calculadora simple.

### ⚙️ Funcionamiento y Arquitectura

La aplicación sigue el modelo de desarrollo web tradicional, combinando cuatro tecnologías clave:

### 1. Estructura (HTML) 🏗️

Proporciona el esqueleto de la calculadora:
* **Contenedor principal:** Un `div` para agrupar y centrar los elementos.
* **Entradas de usuario:** Dos campos de texto (`<input type="number">`) para los operandos (**firstNumber** y **secondNumber**).
* **Selector de Operación:** Un menú desplegable (`<select id="operator">`) para elegir la operación (**+, -, *, /**).
* **Interacción:** Un botón (`<button id="calculate">`) que inicia el proceso.
* **Salida:** Un párrafo (`<p id="result">`) para mostrar el resultado o mensajes de error.

### 2. Estilo (CSS) ✨

El CSS se aplica para una presentación visual **limpia** y **responsive** dentro del entorno Streamlit:
* **Diseño:** Centrado, bordes redondeados y una sombra sutil.
* **Consistencia:** Estilo uniforme aplicado a entradas, selector y botón.
* **Énfasis:** El botón "Calculate" se destaca con un color de fondo verde (`#4CAF50`).

### 3. Lógica (JavaScript) 🧠

El motor funcional que maneja la interacción y realiza los cálculos:
* **Captura de DOM:** Localiza los elementos HTML por su `ID`.
* **Función `calculate()`:** Se ejecuta al hacer clic, convierte entradas a números (`parseFloat`), **valida** las entradas (`isNaN`), y usa una sentencia `switch` para aplicar la operación.
* **Manejo de Excepciones:** Incluye lógica para la **división por cero**.
* **Manejador de Eventos:** El método `addEventListener('click', calculate)` enlaza el clic del botón a la ejecución de la función.

### 4. Presentación (Streamlit / Python) 🐍

Streamlit actúa como el *host*, permitiendo la ejecución del código web independiente:
* **Incrustación:** El código HTML, CSS y JavaScript se almacena como una única cadena de texto en una variable de Python (`html_code`).
* **Renderizado:** La función clave es `components.html(html_code, height=450)`, que renderiza el contenido dentro de un **iframe seguro**, haciendo que la calculadora sea completamente interactiva y funcional dentro de la aplicación Streamlit.

---

## 🛠️ Stack de Tecnologías y Herramientas

| Tecnología | Rol en el Proyecto |
| :--- | :--- |
| **Streamlit** | Framework principal de Python para alojar la aplicación web. |
| **HTML5** | Estructura los elementos de la calculadora. |
| **CSS3** | Define el aspecto visual y el diseño. |
| **JavaScript** | Implementa la lógica de cálculo y la interactividad. |
| **Python** | Contiene el script que utiliza Streamlit para incrustar el componente. |

---

## 🧑‍💻 Colaboradores

| Avatar | Nombre | Rol | GitHub & LinkedIn |
| :--- | :--- | :--- | :--- |
| <img width="60" height="60" src="https://github.com/Sergius-DS.png" alt="Sergius-DS" /> | **Sergio Rivera Bustamante** | Data Scientist | [![Github](https://skillicons.dev/icons?i=github)](https://github.com/Sergius-DS) [![Linkedin](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/sergio-rivera-bustamante-6642b836/) |
