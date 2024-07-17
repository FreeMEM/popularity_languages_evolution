# Análisis de popularidad de lenguajes de programación con pandas, matplotlib y python

Pequeño programa escrito en python usando pandas y matplotlib para analizar la evolución de los lenguajes de programación a lo largo de los años usando un dataset descargado de 
https://www.kaggle.com/datasets/muhammadkhalid/most-popular-programming-languages-since-2004?resource=download

que a su vez ha sido extraído de

https://pypl.github.io/PYPL.html

PYPL tal como explica en su página es:

"El índice de popularidad de lenguajes de programación de PYPL se crea analizando la frecuencia con la que se buscan tutoriales de idiomas en Google: cuanto más se busca un tutorial de idiomas, más popular se supone que es el idioma. Es un indicador adelantado. Los datos sin procesar provienen de Google Trends.


Si cree en la sabiduría colectiva, el índice de popularidad de lenguajes de programación de PYPL puede ayudarlo a decidir qué lenguaje estudiar o cuál usar en un nuevo proyecto de software."

## Ejecución del código
Debe tener docker instalado en su sistema. A partir de ahí sólo hay que lanzar el siguiente comando dentro del path donde está el código

```sh
 docker compose up --build
```
Esto instalará las dependencias y creará la imágen docker con todo lo necesario además de ejecutar el código. Tras una espera de unos segundos, generará un video .mp4 con la evolución.

Espero sea ilustrativo

