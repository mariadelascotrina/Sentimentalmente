from flask import Flask, request
from flask import jsonify
import scr.apiget as ag

app = Flask(__name__)

#http://127.0.0.1:5000/

# EMPESAMO'
@app.route("/")
def inicial()
    return jsonify("Mete algún endpoint para empezar a funcionar")


#DAME LOS PERSONAJES
@app.route("/persons")
def damelaspersons():
    personitas = ag.personajes()
    return jsonify(personitas)

#DAME LOS EPISODIOS
@app.route("/episodes")
def damelosepisodes():
    episodes = ag.episodios()
    return jsonify(episodes)

#DAME LAS FRASES
@app.route("/frases")
def damelasfrases():
    fraseses = ag.frases()
    return jsonify(fraseses)

#DAME LAS FRASES DE CADA PERSONA EN BASE A SU NOMBRE
@app.route("/frases/<nombre_del_person>")
def frases(nombre_del_person):
    frasecitas = ag.sentencias(nombre_del_person)
    return jsonify(frasecitas)

#DAME LAS FRASES DE CADA PERSONA EN UN EPISODIO
@app.route("/frases/<nombre_del_person>/<nombre_del_episodio>")
def frasesmasmolonas(nombre_del_person, nombre_del_episodio):
    frasecitas2 = ag.sentenciasplus(nombre_del_person, nombre_del_episodio)
    return jsonify(frasecitas2)





#METE NUEVAS SENTENCESS
@app.route("/nuevafrase", methods=["POST"])
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