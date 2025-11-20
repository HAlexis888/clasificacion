# clasificacion
## Opinión
Lo que veo con las diferencias en el max_depth = 2 vs max_depth = None es principalmente que con el que no tiene límite de profundidad, es más preciso; sin embargo, en este ejemplo el árbol que genera es 
más confuso a la hora de su lectura. Mientras que con el de profundidad 2, los resultados son menos precisos (alrededor de un 8% aproximadamente), pero se leen de una manera mucho más sencilla.
Creo que si lo que necesitas es una legibilidad correcta y sencilla, elegir la profundidad de 2 es lo mejor, siempre y cuando no necesites el 100% de la exactitud de los valores. 
Si necesitas máxima precisión, es mejor decidirse por la opción sin límite en la profundidad, aunque se pierda legibilidad.

## Opinión sobre mi base de conocimientos y justificación
No creo que sea aplicable a mi base de conocimientos debido a que en la base de conocimientos de mi proyecto no hay, como tal, parámetros que necesiten ser contabilizados
de manera que se asemeje a lo que requieren estos tipos de árboles de decisión. Por ejemplo, no hay una ID específica para cada elemento y, como tal, no hay una variable objetivo que se asemeje a la dada en esta práctica.

## Cambios que se tendrían que hacer para poder utilizarlos
Principalmente se necesitaría establecer una variable objetivo, que podría ser categórica o continua. La categórica sería la más acertada, ya que la continua es más adecuada si
quisiéramos saber cantidades exactas o azúcares exactos que hay en los alimentos. La variable categórica se podría aplicar para separar los alimentos por categorías como "saludable", 
"recomendable" o "no saludable", para así no hacer algo contable y que solo funcione en base a categorías.
