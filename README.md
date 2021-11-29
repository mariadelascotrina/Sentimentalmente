# Sentimentalmente
![image](https://user-images.githubusercontent.com/92324979/143914925-424545e1-2732-44d1-bc9b-215de1b214ae.png)

Creando una API de Juego de tronos
Analizando sentimientos de los personajes de la serie Juego de tronos gracias a NLP (procesamiento del lenguaje natural) en Python.

## ¿Cómo funciona?, con diferentes endpoints
### @get
Los endpoints tipo get, permiten consultar información. Hemos creado los siguientes: 
- "/" :
El endpoint inicial te animará a poner otro endpoint para continuar con tu consulta

- "/persons" :
Este endpoint te devuelve el nombre de todos los personajes que forman parte de la serie

- "/episodes" :
Este endpoint te devuelve el nombre de todos los episodios que conforman la serie

- "/frases" :
Este endpoint te devuelve el nombre de todas las frases de la serie

- "/frases/<nombre_del_person>" :
Este endpoint te da las frases de la serie en función del nombre del personaje. En <nombre_del_person>, debes incluir el nombre del personaje. Si tienes dudas de cómo escribir tu personaje favorito, puedes consultalo en el endpoint de /persons


- "/frases/<nombre_del_person>/<nombre_del_episodio>" :
Este endpoint te da las frases de cada personaje en cada capítulo. En <nombre_del_person>, debes incluir el nombre del personaje y en <nombre_del_episodio>, nombre del episodio. Si tienes dudas de cómo escribir tu personaje favorito o el episodio a consultar, puedes consultalo en los endpoints de "/persons" o "/episodes"


### @post
- "/nuevafrase":
Gracias a este endpoint podemos incluir frases nuevas en nuestra base de datos. Los parámetros para incluir la información son:
parametos = {"sentence": "example sentence", "person_id": 14, "episode_episode_id": 3 }
"example sentence" debe ser un string
14 y 3 deben ser números enteros


- "/nuevoperson":
Gracias a este endpoint podemos incluir a un nuevo personaje para que forme parte de nuestra base de datos. Los parámetros para incluir son:
parametos = {"person_name": "example person"}
"example person" debe ser un string

### sentimientos
- "/sentimiento/<person_name>"
Con requests a la API podemos analizar los sentimientos de los mensajes de cada personaje  para saber si se expresa feliz o triste.



