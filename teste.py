import requests
import time

def obter_municipios_sp():
    """
    Obtém a lista de municípios do estado de São Paulo usando a API do IBGE.
    Retorna uma lista de dicionários, cada um representando um município.
    """
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/SP/municipios"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        print("Erro ao obter municípios.")
        return []

def verificar_gabriel_top10():
    """
    Para cada município de SP, verifica se o nome GABRIEL está entre os 10 mais frequentes.
    Retorna uma lista de dicionários com o nome do município e a frequência do nome GABRIEL.
    """
    municipios = obter_municipios_sp()
    resultado_gabriel = []

    for municipio in municipios:
        id_municipio = municipio['id']
        nome_municipio = municipio['nome']
        url_nome = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?localidade={id_municipio}"
        try:
            resposta_nome = requests.get(url_nome, timeout=10)
            if resposta_nome.status_code == 200:
                dados = resposta_nome.json()
                if dados and isinstance(dados, list) and len(dados) > 0 and 'res' in dados[0]:
                    top_10 = dados[0]['res'][:10]
                    for item in top_10:
                        if item['nome'].upper() == "GABRIEL":
                            resultado_gabriel.append({
                                "municipio": nome_municipio,
                                "frequencia": item['frequencia']
                            })
                            break
            else:
                print(f"Erro ao buscar nome para município {nome_municipio}: {resposta_nome.status_code}")
        except Exception as erro:
            print(f"Erro ao processar município {nome_municipio}: {erro}")
        time.sleep(0.2)  # Pausa de 200ms entre as requisições

    # Ordena o resultado em ordem decrescente de frequência
    resultado_gabriel.sort(key=lambda x: x['frequencia'], reverse=True)
    return resultado_gabriel

if __name__ == "__main__":
    resultado = verificar_gabriel_top10()
    top_10 = resultado[:10]
    print("Top 10 municípios onde 'GABRIEL' está no top 10 (ordenados por frequência):")
    for posicao, item in enumerate(top_10, start=1):
        print(f"{posicao}º - {item['municipio']}: {item['frequencia']}")

    # Se quiser a lista/dicionário para uso posterior:
    print("\nLista/dicionário do top 10:")
    print(top_10)