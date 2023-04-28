from flask import Flask, request
from api import integrando_google_planilha

with open('linha_planilha.txt', 'w') as arquivo:
    arquivo.write('1')

app = Flask(__name__)

@app.route('/enviar', methods=['POST'])
def enviar():
    dados = request.get_json()
    texto = dados['texto']
    integrando_google_planilha(texto)

    return {'mensagem': 'Dados enviados com sucesso!'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3000')