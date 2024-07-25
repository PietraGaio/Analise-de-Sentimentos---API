## MLOps: Aplicação Flask

# Importação Bibliotecas
from flask import Flask
from textblob import TextBlob

app = Flask('__name__')

@app.route('/')  # Define a rota para a função home
def home():
    return 'Minha primeira API'

@app.route('/sentimento/<frase>')
def sentimento(frase):
    tb = TextBlob(frase)
    polaridade = tb.sentiment.polarity
    return 'Polaridade: {}'.format(polaridade)

if __name__ == '__main__':
    app.run(debug=True)


