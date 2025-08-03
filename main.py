from flask import Flask, request
import requests
import urllib.parse
import os

app = Flask(__name__)

WHATSAPP_PHONE = '+553182838771'
API_KEY = '4706004'

@app.route('/', methods=['POST'])
def webhook():
    dados = request.get_json()

    for item in dados.get('itens', []):
        descricao = item.get('descricao', '').lower()
        if descricao.startswith('adaptador'):
           mensagem = "📦 Venda confirmada de adaptador!\nPode separar o produto, pedido já está em andamento. ✅"
            texto = urllib.parse.quote(mensagem)
            url = f"https://api.callmebot.com/whatsapp.php?phone={WHATSAPP_PHONE}&text={texto}&apikey={API_KEY}"
            requests.get(url)
            break

    return 'ok', 200

@app.route('/', methods=['GET'])
def status():
    return 'Servidor rodando', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
