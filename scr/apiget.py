
from config2.configuration import *
import pandas as pd
from textblob import TextBlob
import re
import spacy
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#DAME PERSONS
def personajes():
    query = list(engine.execute("SELECT distinct(person_name) FROM api.person;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista

#DAME LOS EPISODIOS
def episodios():
    query = list(engine.execute("SELECT distinct(episode_name) FROM api.episode;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista

#DAME LAS FRASES
def frases():
    query = list(engine.execute("SELECT distinct(sentence) FROM api.sentence;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista

#DAME FRASES EN BASE A NOMBRE DEL PERSON
def sentencias(nombredelperson):
    query = f"""
    SELECT sentence.sentence, person.person_name
    FROM api.sentence
    INNER JOIN api.person
    ON person.person_id=sentence.person_id
    WHERE person_name= '{nombredelperson}';
    """
    data = pd.read_sql_query(query,engine)
    return data.to_json(orient='records')

#DAME FRASES DE CADA PERSONA EN UN EPISODIO PERSON
def sentenciasplus(nombredelperson, nombredelepisodio):
    query = f"""
    SELECT sentence.sentence, person.person_name, episode.episode_name
    FROM api.sentence
    INNER JOIN api.person
    ON person.person_id=sentence.person_id
    INNER JOIN api.episode
    ON sentence.episode_episode_id = episode.episode_id
    WHERE episode_name = '{nombredelepisodio}' AND person_name = '{nombredelperson}' ;
    """
    data = pd.read_sql_query(query,engine)
    return data.to_json(orient='records')


#METE NUEVIS MENSAJES

def nuevomensaje(sentence, person_id, episode_episode_id):

    engine.execute(f"""
    INSERT INTO sentence (sentence,person_id,episode_episode_id)
    VALUES ('{sentence}', {person_id}, {episode_episode_id});
    """)
    
    return f"Se ha introducido correctamente: {sentence} {person_id} {episode_episode_id}"

def nuevoperson( person_name):

    engine.execute(f"""
    INSERT INTO person (person_name)
    VALUES ('{person_name}');
    """)
    
    return f"Se ha introducido correctamente: {person_name} "


def analisisdesentimiento(person_name):
    query =  f"""
    SELECT sentence.sentence
    FROM api.sentence
    INNER JOIN api.person
    ON person.person_id=sentence.person_id
    WHERE person_name= '{person_name}';
    """
    data = pd.read_sql_query(query,engine)
    return data

def tokenizer(frase):
    nlp = spacy.load("en_core_web_sm")
    tokens = nlp(frase)
    filtradas = []
    
    for token in tokens:
        if not token.is_stop:
            lemma = token.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma): # Esto me quita las interrogaciones
                filtradas.append(lemma)
    return " ".join(filtradas)

def sentiment(frase):
    sia = SentimentIntensityAnalyzer()
    polaridad = sia.polarity_scores(frase)
    pol = polaridad["compound"]
    return pol





