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


### @get
- "/nuevafrase", methods=["POST"]) :
Gracias a este endpoint podemos incluir frases nuevas en nuestra base de datos. Los parámetros para incluir la información son:
diccionario = {

def metercosas():
    frase = request.form.get("sentence")
    numper = request.form.get("person_id")
    numep = request.form.get("episode_episode_id")
    # PODRÍAMOS LLAMAR A FUNCIONES CHECK
    print(frase, numep, numper)

    return ag.nuevomensaje(frase, numper, numep)

@app.route("/nuevoperson", methods=["POST"])
def meterperson():
    person_name = request.form.get("person_name")
    # PODRÍAMOS LLAMAR A FUNCIONES CHECK
    print(person_name)

    return ag.nuevoperson(person_name)


@app.route("/sentimiento/<person_name>")
def sent(person_name):
    df = ag.analisisdesentimiento(person_name)
    df["frasestoken"] = df.sentence.apply(ag.tokenizer)
    df["sentimiento"] = df.frasestoken.apply(ag.sentiment)
    return str(df.sentimiento.mean())
 



if __name__ == "__main__":
    app.run(debug=True)


### @post


### Análisis de sentimiento


