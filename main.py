from flask import Flask, request
import requests
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def alerta():
    if request.method == 'POST':
        numero = "+553182838771"
        apikey = "4706004"
        mensagem = "🚨 Alerta de adaptador recebido!"
        texto = urllib.parse.quote(mensagem)
        url = f"https://api.callmebot.com/whatsapp.php?phone={numero}&text={texto}&apikey={apikey}"
        try:
            r = requests.get(url)
            print(f"Enviado: {r.status_code}")
        except Exception as e:
            print(f"Erro ao enviar: {e}")
        return 'POST recebido e alerta enviado', 200
    return 'Servidor rodando', 200
