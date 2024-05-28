# Proyecto Individual 1: Sistema de Recomendacion de Juegos - Steam.
En este proyecto, se desarrolló un sistema de recomendación de videojuegos para la plataforma Steam desde cero. Se creó una solución integral que abarca desde la ingeniería de datos hasta el despliegue de una API utilizando la biblioteca FastAPI. El objetivo es proporcionar a los usuarios una herramienta efectiva para descubrir nuevos juegos, basándose en análisis de sentimientos, información de los desarrolladores, interacción de los usuarios y un modelo de aprendizaje automático.
# Proceso del Proyecto.
   - **ETL y Análisis de Sentimiento:** Se llevó a cabo un proceso de extracción, transformación y carga (ETL) para limpiar y formatear los datos de manera adecuada. Además, se utilizó procesamiento de lenguaje natural (NLP) para crear la columna 'opinion', mejorando así el rendimiento de la API y facilitando el entrenamiento de los modelos de machine learning.
     >  El valor 0 para comentarios malos
     >
     >  El valor 1 para comentarios neutros
     >
     >  El valor 2 para comentarios positivos
   - **Análisis Exploratorio de Datos (EDA):** Se realizó un análisis exhaustivo para identificar relaciones entre variables, así como detectar outliers, anomalías y patrones que son útiles para un análisis más profundo.
   - **Implementación de Funciones:** El codigo consta con 6 funciones:
     > `/developer/{desarrollador}`: Esta función filtra un DataFrame para un desarrollador dado, recopila la cantidad de juegos lanzados y los gratuitos por año, y devuelve un diccionario            con 'Cantidad de Items' y 'Contenido Free', cada uno conteniendo diccionarios con los años como claves y las cantidades correspondientes como valores.
     > 
     > `/User_data/{user_id}`: Esta función toma un nombre de usuario, verifica su existencia en un DataFrame de usuarios y juegos, lee un PARQUET en bloques para buscar al usuario, calcula           el gasto total, cantidad de juegos y porcentaje de recomendaciones, y devuelve un diccionario con esta información.
     >
     > `/Game_genre/{gen}`: Esta función toma una cadena de texto que representa una categoría/género de juegos, busca y agrupa en el DataFrame por usuarios y tiempo jugado de aquellos que           han jugado esa categoría/género, y devuelve al usuario con mayor cantidad de horas jugadas en esa categoría/género agrupado de forma descendente por año.
     >
     > `/Best_developer/{anio}`: Esta función toma un entero que representa un año, lee un archivo PARQUET con información sobre desarrolladores y la cantidad de juegos lanzados cada año,            filtra los datos para el año dado y devuelve un diccionario con el 'Top 1', 'Top 2' y 'Top 3' de los desarrolladores que lanzaron más juegos ese año.
     >
     > `/developer_reviews/{dev}`: Esta función toma una cadena de texto que representa el nombre de un desarrollador, lee un archivo Parquet con reseñas de juegos de cada desarrollador,             filtra las reseñas para el desarrollador dado y devuelve un diccionario con la cantidad de reseñas positivas y negativas que ha recibido.
   - **Implementación de Modelos de Recomendación:** Se desarrollaron modelos de recomendación basados en la similitud entre ítems y usuarios. Estos modelos ayudan a sugerir juegos similares, mejorando la experiencia de descubrimiento para los usuarios.
     > `/recommend_games/{user_id}`: Recomendación personalizada de 5 juegos para un usuario basada en sus opiniones previas, o recomendación aleatoria si no hay datos disponibles.
   - **Creación de la API con FastAPI:** Se diseñó y desarrolló una API con FastAPI que permite realizar múltiples consultas a los datos, proporcionando información detallada sobre desarrolladores, usuarios, géneros y juegos.
   - **Despliegue:** La API está desplegada en el servicio Render, lo que permite su acceso y uso desde la web.
#  Autor y Links.
**Lucas Ariel Leguizamon Alegre**
- Link del [Deploy](https://proyecto-individual-1-82o6.onrender.com/docs)
- Link del [Video]()
- [GitHub](https://github.com/1ucas1eguizam0n)
- [LinkedIn](https://www.linkedin.com/in/lucas-leguizam%C3%B3n-4a0437283?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app )
