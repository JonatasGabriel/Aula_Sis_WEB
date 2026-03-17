import requests

# Url da API publica da Binance para obter o preco atual de um par SPOT
url = "https://api.binance.com/api/v3/ticker/price" # SPOT Binance

# Funcao que obtem da API publica da Binance o preco atual de um par SPOT
def pega_preco(par):

    # Recebe os dados de precos da API
    response = requests.get(url, timeout=10)
    dados_precos_atuais_raw = response.json()

    # Imprime todos os dados recebidos
    print (f'\nDados recebidos: {dados_precos_atuais_raw}\nTipo dos dados: {type(dados_precos_atuais_raw)}\nPares encontrados: {len(dados_precos_atuais_raw)}\n')

    # Loop que procura o par
    for pares in dados_precos_atuais_raw:
        if pares['symbol'] == par:
            return pares['price']
            
# Teste da funcao pega_preco
if __name__ == "__main__":

    par = "BTCUSDT"
    print (f'O preco atual de {par} em SPOT da Binance e {pega_preco(par)}')

