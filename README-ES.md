# La Red Social
[![en](https://img.shields.io/badge/lang-en-red.svg)](/README.md)

Este repositorio contiene las dos partes de la tarea de la asignatura _Estructura de Datos y Algoritmos_, dentro del currículum de Ingeniería Informática en la Universidad de Valladolid. La intención de la asignatura era aprender cómo estructuras de datos eficientes pueden mejorar notablemente el rendimiento.

El diseño se basa en una _red social_. Se tienen múltiples usuarios, cada uno con sus conexiones (bidireccionales) con otros. El objetivo del programa es identificar _grumos_, grupos de usuarios conectados (ya sea directamente o a través de otro usuario) entre ellos. La siguiente imagen muestra cómo 15 usuarios forman 4 _grumos_:

![Grumos](/readme-files/grumos1.jpg "Grumos")

La red social trata de mantener los usuarios conectados lo más posible con el resto de la plataforma. Dicho de otra forma, se busca que el mayor número de usuarios posibles esté en el mismo _grumo_.
Con esta intención, el programa pregunta por un porcentaje que indica cuántos usuarios queremos que estén en el _grumo_ más grande, y calcula el mínimo número de conexiones necesarias para hacerlo posible.

La imagen siguiente muestra el ejemplo de antes cuando el porcentaje se fija en el 85%. Los 3 _grumos_ más grandes se unen, consiguiendo que el nuevo _grumo_ más grande contenga el 87% de los usuarios.

![Grumos 2](/readme-files/grumos2.jpg "Grumos 2")

En la carpeta [testfiles](testfiles/) hay algunos ficheros que representan las redes sociales.
Después de la ejecución, las conexiones necesarias se imprimen por salida estándar y también en un fichero llamado `extra.txt`. Con el fin de poder testear, este fichero se le puede dar al programa para verificar que funciona correctamente (no se piden más conexiones).

Debemos recordar que lo que queríamos con esta tarea era aprender sobre estructuras de datos, algoritmos y su eficiencia. Por esta razón, se imprime el tiempo que tardan algunas partes del procesado.

Hay dos implementaciones:
1. La primera se realizó usando herramientas típicas de cualquier lenguaje de programación: listas/arrays y métodos asociados (`sort`, `append`, `in`...). Se encuentra en un [archivo único](original_unoptimized.py). Aunque conseguía su propósito la eficiencia era bastante mala. Procesar las redes más grandes era prácticamente imposible.

2. La segunda versión usa lo aprendido en la asignatura para mejorar el programa y reducir el tiempo necesario para procesar la red. La forma de conseguirlo fue usando un [_disjoint-set_](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) para representar la red y sus usuarios. Con esta y otras modificaciones, se lograba procesar hasta las redes más grandes, con 2000000 conexiones. Para ejecutar esta versión se debe usar el archivo [optimized.py](optimized.py). El resto de los ficheros `.py` contienen el código para representar los _grumos_ y los usuarios.

Parte de esta tarea era aprender a programar cada vez mejor, y por ello se usan dos formas de documentar el código.