from flask import Flask, request
import requests

app = Flask(__name__)

# Dados do CallMeBot
WHATSAPP_PHONE = '553182838771'
API_KEY = '4706004'

@app.route('/', methods=['POST'])
def webhook():
    dados = request.get_json()

    # Verifica se tem itens no pedido
    for item in dados.get('itens', []):
        descricao = item.get('descricao', '').lower()
        if descricao.startswith('adaptador'):
            mensagem = f"🔔 Nova venda detectada! Produto: {item['descricao']}\nJá prepara a separação, gostoso 😘"
            url = f"https://api.callmebot.com/whatsapp.php?phone={WHATSAPP_PHONE}&text={mensagem}&apikey={API_KEY}"
            requests.get(url)

    return 'ok'

if __name__ == '__main__':
    app.run()
