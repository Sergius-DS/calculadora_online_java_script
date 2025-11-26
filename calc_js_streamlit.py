import streamlit as st
import streamlit.components.v1 as components

# Se incrustó el HTML, CSS y JS en un solo string de Python
# Esto se hizo para que se pudiera ejecutar en streamlit
html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Calculator</title>
    <style>
        /* Archivo styles.css */
        .container {{
            padding: 20px;
            max-width: 400px;
            margin: 0 auto;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }}
        input, select, button {{
            width: 90%;
            padding: 10px;
            margin: 5px 0;
            border-radius: 4px;
            border: 1px solid #ddd;
        }}
        button {{
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }}
        #result {{
            margin-top: 15px;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>JS Calculator Demo</h1>
        <input type="number" id="firstNumber" placeholder="First number" />
        <select id="operator">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type="number" id="secondNumber" placeholder="Second number" />
        <button id="calculate">Calculate</button>
        <p id="result">Result will be displayed here</p>
    </div>
    <script>
        /* Archivo script.js */
        const firstNumberInput = document.getElementById('firstNumber');
        const secondNumberInput = document.getElementById('secondNumber');
        const operatorSelectInput = document.getElementById('operator');
        const calculateButton = document.getElementById('calculate');
        const resultParagraph = document.getElementById('result');

        function calculate() {{
          const firstNumber = parseFloat(firstNumberInput.value);
          const secondNumber = parseFloat(secondNumberInput.value);
          const operator = operatorSelectInput.value;
          let result;

          if (isNaN(firstNumber) || isNaN(secondNumber)) {{
            resultParagraph.textContent = 'Please enter a valid number';
            return;
          }}

          switch (operator) {{
            case '+':
              result = firstNumber + secondNumber;
              break;
            case '-':
              result = firstNumber - secondNumber;
              break;
            case '*':
              result = firstNumber * secondNumber;
              break;
            case '/':
              if (secondNumber === 0) {{
                resultParagraph.textContent = 'Division by zero is not allowed';
                return;
              }}
              result = firstNumber / secondNumber;
              break;
            default:
              result = 'Invalid operator';
          }}
          resultParagraph.textContent = 'Result: ' + result;
        }}

        calculateButton.addEventListener('click', calculate);
    </script>
</body>
</html>
"""
st.header('Demostración de JavaScript Incrustado en Streamlit')
components.html(html_code, height=450)
#st.code(html_code, language='html')