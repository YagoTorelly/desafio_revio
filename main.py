import requests
from fastapi import FastAPI
import uvicorn
import json
import time

app = FastAPI()

class MunicipioService:
    def __init__(self):
        self.url_municipios = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/SP/municipios"
        self.url_base_nomes = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?localidade="

# 1. O primeiro passo seria consultar a API que lista todos os municípios do estado de São Paulo, através do end-poit:
# https://servicodados.ibge.gov.br/api/v1/localidades/estados/SP/municipios

    def lista_municipios_SP(self):
        response = requests.get(self.url_municipios)
        if response.status_code == 200:
            municipios = response.json()
            resultado = []

            for municipio in municipios:
                nome = municipio['nome']
                id_municipio = municipio['id']
                sigla = municipio['microrregiao']['mesorregiao']['UF']['sigla']

                resultado.append({"nome": nome, "id": id_municipio, "uf": sigla})

            return "Deu certo", resultado
        else:
            return "Deu errado", response.status_code

# 2.  deverá coletar o ID de cada município bem como o nome deste município e o estruturar em um dicionário em seu código:

    def municipios_dic(self):
        response = requests.get(self.url_municipios)
        if response.status_code == 200:
            municipios = response.json()
            municipios_dict = {}

            for municipio in municipios:
                id_municipio = municipio['id']
                nome = municipio['nome']
                municipios_dict[id_municipio] = nome

            return "Deu certo", municipios_dict
        else:
            return "Deu errado", response.status_code
        
    
# 3. Com estes dados você deverá agora consultar a API de nomes do IBGE, no entanto para cada município você terá que construir a 
# url de pesquisa seguindo o modelo: https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?localidade={CÓDIGO_MUNICIPIO}

    def modelo_url(self, municipios_dict):
        url_geral = {}
        for id_municipio, nome_municipio in municipios_dict.items():
            url_completa = f"{self.url_base_nomes}{id_municipio}"
            url_geral[nome_municipio] = url_completa
        return url_geral
    
# 4. Agora com essa coleção de dados você deverá processar eles a fim de obter todos os
# municípios onde o nome "GABRIEL" está no top 10

    def verificar_gabriel_top10(self):
        response = requests.get(self.url_municipios, timeout=11)
        resultado_gabriel = {}

        if response.status_code == 200:
            municipios = response.json()

            for municipio in municipios:
                id_municipio = municipio['id']
                nome_municipio = municipio['nome']
                url = f"{self.url_base_nomes}{id_municipio}"

                try:
                    response_nome = requests.get(url, timeout=11)
                    time.sleep(0.3)  

                    if response_nome.status_code == 200:
                        dados = response_nome.json()
                        if dados and 'res' in dados[0]:
                            top_10 = dados[0]['res'][:10]
                            for item in top_10:
                                if item['nome'].upper() == "GABRIEL":
                                    resultado_gabriel[nome_municipio] = item['frequencia']
                                    break
                except requests.exceptions.RequestException:
                    continue  

            # Primeiro ordena em ordem decrescente para pegar os 10 maiores
            top_10_municipios = sorted(resultado_gabriel.items(), key=lambda x: x[1], reverse=True)[:10]
            # Depois inverte a ordem para ter do menor para o maior
            resultado_ordenado = dict(reversed(top_10_municipios))

            with open("resultado_gabriel.json", "w", encoding='utf-8') as f:
                json.dump(resultado_ordenado, f, ensure_ascii=False, indent=4)

            return {"top_10_municipios": resultado_ordenado}

        return {"erro": "Erro na resposta da API de municípios"}


                           
service_municipio = MunicipioService()

#endpoint para listar todos os municipios com o nome, id e sigla

@app.get("/lista_municipios_SP")
def get_lista_municipios_SP():
    dados = service_municipio.lista_municipios_SP()
    return {"municipios": dados} if dados else {"erro": "Erro ao acessar a API do IBGE"}

#endpoint para armazenar em um dicionario 

@app.get("/municipios_dic")
def get_municipios_dic():
    dados = service_municipio.municipios_dic()
    return {"municipios": dados} if dados else {"erro": "Erro ao acessar a API do IBGE"}

#endpoint para criar modelo de url

@app.get("/modelo_url")
def get_modelo_url():
    status, municipios_dict = service_municipio.municipios_dic()
    if status == "Deu certo":
        urls = service_municipio.modelo_url(municipios_dict)
        return {"urls_por_municipio": urls}
    else:
        return {"erro": "Erro ao acessar os municípios"}


#endpoint para verificar quais municipios o GABRIEL é top10 e gerar o json 

@app.get("/verificar_gabriel_top10")
def get_verificacao():
    resultado = service_municipio.verificar_gabriel_top10()
    return {"resultado": resultado}


if __name__ == "__main__":
    uvicorn.run(app, port=8001)









