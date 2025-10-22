

# Microservicio Factorial - Parcial 02

Este microservicio en **Flask (Python)** recibe un número por URL y devuelve un **JSON** con:
- El número recibido  
- Su factorial  
- Una etiqueta `"par"` o `"impar"` según **el número recibido** 

---

##  **Cómo ejecutar**

###  Local
```bash
pip install -r requirements.txt
python app.py
````

Luego abre en el navegador:

* `http://127.0.0.1:5050/` → {"status": "ok"}
* `http://127.0.0.1:5050/api/factorial/5` → {"factorial":"120","numero":5,"paridad":"impar"}
* `http://127.0.0.1:5050/api/factorial/8` → {"factorial":"40320","numero":8,"paridad":"par"}

---


##  **Análisis (pregunta del parcial)**

Si este microservicio tuviera que comunicarse con otro que guarda el historial de cálculos en una base de datos externa:

Si este microservicio tuviera que comunicarse con otro que guarda el historial de los cálculos, lo que haría sería enviarle la información del número, su factorial y la paridad después de hacer el cálculo.
El otro servicio se encargaría de guardar esos datos en su base de datos.

Para eso, solo necesitaría agregar la URL del otro servicio (por ejemplo, en una variable de entorno) y mandar la información con una petición HTTP.
De esta forma, cada servicio sigue haciendo su parte por separado: uno calcula y el otro guarda el historial.
Esto mantiene el bajo acoplamiento y permite que ambos funcionen de forma independiente, que es lo que se busca en una arquitectura de microservicios.

---

 **Autor:** María Alejandra Ocampo
 
 Arquitectura de Software – Parcial 02


