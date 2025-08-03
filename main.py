from flask import Flask, request
import requests
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET'])
def alerta():
    numero = "+553182838771"
    apikey = "4706004"
    mensagem = "🚨 Alerta de adaptador acessado!"
    texto = urllib.parse.quote(mensagem)
    url = f"https://api.callmebot.com/whatsapp.php?phone={numero}&text={texto}&apikey={apikey}"
    try:
        r = requests.get(url)
        print(f"Enviado: {r.status_code}")
    except Exception as e:
        print(f"Erro ao enviar: {e}")
    return 'Notificação enviada com sucesso 🚀', 200
