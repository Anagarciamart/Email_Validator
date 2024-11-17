## Mejoras en la validación de correos electrónicos

Se han realizado varias mejoras en el módulo de validación de correos electrónicos para aumentar su robustez y fiabilidad:

* **Nuevos correos de prueba:** Se han incorporado nuevos correos de prueba a `correos.py` para una validación más exhaustiva.
* **Pruebas unitarias ampliadas:** `test_email_validator.py` ha sido actualizado con nuevas pruebas unitarias para verificar que `EmailValidator` identifique correctamente direcciones válidas y rechace las inválidas. Se genera un informe detallado al finalizar las pruebas.
* **Mejora en la clase `EmailValidator`:**
    * **Expresiones regulares:** Se han utilizado expresiones regulares para mejorar la precisión y eficiencia de la validación.
    * **Registro:** Se ha añadido un sistema de registro en `email_validator.log` para facilitar la depuración y el análisis de los resultados de la validación.
    * **Excepciones:** Se han implementado excepciones personalizadas para manejar errores de manera más específica y proporcionar mensajes de error informativos.
