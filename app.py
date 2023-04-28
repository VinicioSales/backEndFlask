from flask import Flask
from api import integrando_google_planilha

app = Flask(__name__)

@app.route('/')
def index():
    resposta = integrando_google_planilha()

    return str(resposta)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3000')