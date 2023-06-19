from flask import Flask, render_template
from functions import *

app = Flask(__name__)


@app.route('/paises/<pais>')
@app.route('/paises')
def rota_pais(pais=None):
    # Filtrar aqui dentro
    media = media_salarial(df, pais)
    media_por_idade = media_salarial_idade(df, pais)
    representatividade = representatividade_genero(df, pais)
    return render_template('pais.html', pais=pais, media=media, media_por_idade=media_por_idade, representatividade=representatividade)


'''@app.route('/')
def home():
    return '<h1>Digite o nome de um país ao final da URL para ver informações a respeito de sua média salarial, média salarial por idade e representatividade de gênero!</h1>'

@app.route('/<pais>')
def info(pais=None):
    return texto(df, pais)'''

# flask --app treino-flask-dev/fabio-quirino/app.py run


    
