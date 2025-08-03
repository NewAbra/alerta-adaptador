from flask import Flask, request
import requests
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def alerta():
    numero = "+553182838771"
    apikey = "4706004"
    mensagem = "🚨 Alerta de adaptador recebido!"
    texto = urllib.parse.quote(mensagem)
    url = f"https://api.callmebot.com/whatsapp.php?phone={numero}&text={texto}&apikey={apikey}"

    if request.method == 'POST':
        try:
            r = requests.get(url)
            print(f"[POST] Enviado: {r.status_code}")
        except Exception as e:
            print(f"[POST] Erro ao enviar: {e}")
        return 'POST recebido e alerta enviado', 200

    # --- TRATANDO GET COM PARÂMETRO SKU ---
    if request.method == 'GET':
        sku = request.args.get('sku', '').lower()
        if 'adaptador' in sku:
            try:
                r = requests.get(url)
                print(f"[GET] Enviado: {r.status_code}")
            except Exception as e:
                print(f"[GET] Erro ao enviar: {e}")
            return 'GET com SKU detectado e alerta enviado', 200

    return 'Servidor rodando', 200
