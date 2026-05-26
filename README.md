# Guardería Canina IA

Sistema inteligente desarrollado con Inteligencia Artificial y Machine Learning para analizar el comportamiento de perros dentro de una guardería canina y ayudar en la toma de decisiones relacionadas con convivencia, seguridad y monitoreo de mascotas.

---

# Problema que se buscó solucionar

En muchas guarderías caninas resulta difícil identificar el comportamiento de los perros antes de integrarlos con otras mascotas. Esto puede generar problemas de convivencia, peleas, estrés, accidentes o situaciones de riesgo tanto para los animales como para los cuidadores.

El objetivo principal del proyecto fue desarrollar un sistema inteligente capaz de analizar diferentes características de un perro y predecir automáticamente su comportamiento utilizando Inteligencia Artificial.

La solución permite clasificar mascotas como:

* Tranquilas
* Nerviosas
* Agresivas

Gracias a esto, la guardería puede tomar decisiones más seguras antes de integrar perros en zonas compartidas.

---

# Librerías, frameworks y recursos utilizados

## Backend

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* Joblib

## Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

## Recursos adicionales

* Dataset en formato CSV
* Modelo entrenado con Machine Learning
* GitHub para control de versiones
* Visual Studio Code para desarrollo

---

# Construcción del dataset

El dataset fue construido manualmente utilizando datos simulados relacionados con comportamiento canino.

Las variables utilizadas fueron:

* Energía
* Tamaño
* Edad
* Peso
* Socialización

Cada registro fue clasificado con una etiqueta final correspondiente al comportamiento esperado del perro:

* TRANQUILO
* NERVIOSO
* AGRESIVO

Para generar el dataset se utilizaron diferentes combinaciones de valores buscando representar casos reales que podrían ocurrir dentro de una guardería canina.

---

# Cantidad de entradas utilizadas

El modelo fue entrenado utilizando cientos de registros dentro del dataset en formato CSV.

Cada fila representaba un perro diferente con sus respectivas características físicas y de comportamiento.

---

# Modelos de Machine Learning utilizados

Durante el desarrollo se trabajó principalmente con modelos de clasificación supervisada utilizando Scikit-learn.

El modelo principal implementado fue:

* Random Forest Classifier

También se realizaron pruebas con otros modelos de clasificación para comparar resultados y efectividad.

---

# Razón por la cual se eligió el modelo

El modelo Random Forest fue elegido porque:

* Ofrece buena precisión en clasificación
* Funciona correctamente con datasets medianos
* Reduce problemas de sobreajuste
* Permite trabajar fácilmente con múltiples variables numéricas
* Genera resultados rápidos para aplicaciones web

Además, demostró mejor estabilidad frente a otros modelos evaluados durante las pruebas iniciales.

---

# Nivel de efectividad y métricas obtenidas

El sistema alcanzó niveles altos de precisión durante las pruebas realizadas.

Las métricas principales evaluadas fueron:

* Accuracy
* Precision
* Recall

El modelo obtuvo resultados cercanos al 90% de efectividad en las pruebas internas realizadas con los datos de entrenamiento y validación.

Esto permitió obtener predicciones suficientemente confiables para el funcionamiento del sistema web.

---

# Predicciones generadas por el sistema

El sistema genera predicciones automáticas según los datos ingresados en el formulario.

Las posibles predicciones son:

* Agresivo
* Nervioso
* Tranquilo

Cada predicción se calcula utilizando el modelo entrenado previamente en Python.

---

# Uso de las predicciones dentro de la solución

Las predicciones obtenidas fueron utilizadas para construir reglas inteligentes dentro del sistema.

Por ejemplo:

* Un perro clasificado como agresivo genera alertas de convivencia.
* Un perro nervioso requiere supervisión.
* Un perro tranquilo puede convivir normalmente.

Esto permite que la plataforma no solo muestre una clasificación, sino que también ayude al usuario a tomar decisiones rápidas y seguras.

---

# Implementación web del sistema

La solución fue llevada a una plataforma web utilizando Flask como framework principal.

El backend procesa la información ingresada por el usuario y se comunica con el modelo de Inteligencia Artificial entrenado previamente.

El frontend fue construido con HTML, CSS y JavaScript para crear una interfaz moderna, visual e interactiva.

La página incluye:

* Formulario de análisis
* Historial de predicciones
* Estadísticas automáticas
* Gráficas dinámicas
* Buscador
* Validaciones inteligentes
* Diseño responsive

---

# Explicación del frontend

El frontend fue diseñado para ser visualmente atractivo y fácil de utilizar.

Características principales:

* Fondo animado con huellas transparentes
* Tarjetas informativas
* Galería de imágenes
* Interfaz responsive adaptable a móviles
* Formularios validados automáticamente
* Gráficas estadísticas en tiempo real

También se trabajó en mejorar la experiencia visual utilizando efectos modernos y animaciones suaves.

---

# Explicación del backend

El backend fue desarrollado en Python utilizando Flask.

Sus funciones principales son:

* Recibir datos del formulario
* Procesar información
* Ejecutar predicciones con IA
* Guardar historial
* Enviar respuestas al frontend
* Gestionar rutas web

El modelo entrenado se carga mediante Joblib para realizar predicciones rápidas y eficientes.

---

# Reglas inteligentes generadas por el sistema

Las predicciones del modelo permitieron crear comportamientos automáticos dentro de la plataforma.

Algunas reglas implementadas fueron:

* Mostrar mensajes de convivencia dependiendo del resultado
* Generar estadísticas automáticas
* Actualizar gráficas dinámicamente
* Clasificar automáticamente el historial
* Validar datos incorrectos en formularios
* Limitar valores permitidos según cada variable

Estas reglas ayudan a que el sistema funcione de manera más inteligente e interactiva.

---

# Funcionamiento general del sistema

La página web permite que el usuario ingrese características de un perro mediante un formulario.

Posteriormente:

1. Los datos son enviados al backend.
2. Flask procesa la información.
3. El modelo de IA realiza la predicción.
4. El resultado se devuelve al frontend.
5. El sistema muestra:

   * Resultado del comportamiento
   * Recomendación de convivencia
   * Actualización de estadísticas
   * Historial automático
   * Gráficas dinámicas

El objetivo final es ofrecer una herramienta tecnológica que ayude a mejorar la seguridad y convivencia dentro de una guardería canina utilizando Inteligencia Artificial.

---

# Autor

Proyecto académico desarrollado como solución tecnológica basada en Inteligencia Artificial para gestión y análisis de comportamiento canino.
