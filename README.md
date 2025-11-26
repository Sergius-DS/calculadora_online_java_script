
## Descripción Proyectos

Esta es una aplicación web sencilla y funcional cuyo único propósito es realizar operaciones aritméticas básicas (suma, resta, multiplicación y división) utilizando JavaScript para la lógica, y luego ser presentada al usuario a través del framework Streamlit.

## 1. Estructura (HTML)
El código HTML define el esqueleto de la calculadora, que incluye:

Un contenedor principal (<div class="container">) para agrupar todos los elementos.

Dos campos de entrada (<input type="number">) con los IDs firstNumber y secondNumber para que el usuario introduzca los operandos.

Un menú desplegable (<select id="operator">) que permite seleccionar la operación (**, -, *, /).

Un botón (<button id="calculate">) que dispara el cálculo.

Un párrafo (<p id="result">) donde se muestra el resultado o los mensajes de error.

## 2. Estilo (CSS)
El código CSS se encarga de la presentación visual de la calculadora. Sus principales funciones son:

Centrar la calculadora en la página y limitar su ancho (max-width: 400px).

Aplicar un borde y una sombra a la caja principal para un mejor diseño.

Establecer un estilo uniforme (width: 90%, padding, border-radius) para las cajas de entrada y el botón.

Dar un color de fondo (#4CAF50, verde) al botón de "Calculate" para hacerlo destacar.

## 3. Lógica (JavaScript)
El JavaScript es el "cerebro" de la aplicación, controlando cómo funciona la calculadora:

Captura de Elementos: Primero, el script obtiene referencias a todos los elementos clave del HTML (los dos números, el operador, el botón y el párrafo del resultado) usando sus IDs.

Función calculate(): Esta función se ejecuta cuando se hace clic en el botón:

Convierte los valores de texto de los campos de entrada a números flotantes (parseFloat).

Verifica si las entradas son números válidos (isNaN).

Utiliza una sentencia switch para realizar la operación correspondiente según el operador seleccionado.

Maneja un caso especial de división por cero.

Muestra el resultado final o un mensaje de error en el párrafo result.

Manejador de Eventos: La línea calculateButton.addEventListener('click', calculate); asocia la función calculate al evento de clic del botón.

## 4. Presentación (Streamlit)
La parte final del script es de Python y usa Streamlit para servir el código web


## Colaboradores

|                         | Nombre   |   Rol                    | GitHub & LinkedIn                                                                                                                                                                                          |
| ----------------------------- | -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img width="60" height="60" src="https://github.com/Sergius-DS.png" alt="Sergius-DS" /> | Sergio Rivera Bustamante | Data Scientist | [![Github](https://skillicons.dev/icons?i=github)](https://github.com/Sergius-DS) [![Linkedin](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/sergio-rivera-bustamante-6642b836/)                         |
|                               |

