

````markdown
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
* `http://127.0.0.1:5050/api/factorial/5` → {"numero":5,"factorial":"120","paridad":"impar"}
* `http://127.0.0.1:5050/api/factorial/8` → {"numero":8,"factorial":"40320","paridad":"par"}

---


##  **Análisis (pregunta del parcial)**

Si este microservicio tuviera que comunicarse con otro que guarda el historial de cálculos en una base de datos externa:

* Agregaría una **variable de entorno** `HISTORY_URL` con la dirección del servicio de historial.
* Después de calcular el factorial, enviaría los datos (`número`, `factorial`, `paridad`, `fecha`) con una **petición HTTP POST** usando la librería `requests`.
* Si el servicio de historial falla, este microservicio seguiría respondiendo normalmente.

De esta forma se mantiene el **bajo acoplamiento**, la **independencia** entre servicios y la **escalabilidad**, tal como se busca en las **arquitecturas de microservicios**.

---

 **Autor:** María Alejandra Ocampo
 Arquitectura de Software – Parcial 02


