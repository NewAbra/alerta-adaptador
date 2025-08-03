from flask import Flask, request
import requests
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET'])
def alerta():
    numero = "+553182838771"
    apikey = "4706004"
    mensagem = "🚨 Alerta de acesso ao site (GET)"
    texto = urllib.parse.quote(mensagem)

    url = f"https://api.callmebot.com/whatsapp.php?phone={numero}&text={texto}&apikey={apikey}"

    try:
        print(f"📤 Enviando requisição para: {url}")
        r = requests.get(url)
        print(f"✅ Status: {r.status_code}")
        print(f"📨 Resposta: {r.text}")
        return '🔔 Notificação enviada com sucesso!', 200
    except Exception as e:
        print(f"❌ Erro ao enviar mensagem: {str(e)}")
        return f"Erro: {str(e)}", 500
