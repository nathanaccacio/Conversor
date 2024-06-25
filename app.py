from flask import Flask, render_template, request
import requests

app = Flask(__name__) # Cria uma instância da classe Flask.

API_KEY = '82fa1d6af5e87652f9cea17d'

@app.route('/', methods=['GET', 'POST']) # Selecione a rota principal da aplicação
def index():
    if request.method == 'POST':
        valor = float(request.form['valor'])
        moeda_origem = 'BRL' 
        moeda_destino = 'USD'  

        resultado = converter_moeda(valor, moeda_origem, moeda_destino) # Chama a função para converter o valor da moeda.
        if resultado is not None:
            return render_template('resultado.html', valor=valor, moeda_origem=moeda_origem,
                                   moeda_destino=moeda_destino, resultado=resultado)
        else:
            return "Erro ao converter moeda. Verifique sua API key ou conexão com a internet."
    
    return render_template('index.html')

# Função que tem como objetivo realizar a conversão de moeda.
def converter_moeda(valor, moeda_origem, moeda_destino):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{moeda_origem}"  # Monta a URL para acessar a API de conversão de moeda.
    
    response = requests.get(url)  # Faz a requisição GET para a API.
    data = response.json()   # Converte a resposta para JSON.

    if response.status_code == 200:
        taxa = data['conversion_rates'][moeda_destino]
        valor_convertido = valor * taxa
        return valor_convertido
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)


