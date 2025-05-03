# desafio_revio

Projeto desenvolvido em Python com FastAPI para consultar os municípios do estado de São Paulo onde o nome **Gabriel** está entre os 10 nomes mais frequentes, utilizando dados da API do IBGE.

## 💻 Tecnologias utilizadas

- Python 3.11
- FastAPI
- Uvicorn
- Requests
- JSON

### Endpoints disponíveis

| GET    | `/lista_municipios_SP`     | Retorna todos os municípios de SP com nome, ID e UF.                    |

| GET    | `/municipios_dic`          | Retorna um dicionário `{id: nome}` com todos os municípios.             |

| GET    | `/modelo_url`              | Gera a URL de consulta da API do IBGE por município.                    |

| GET    | `/verificar_gabriel_top10` | Retorna os 10 municípios onde "Gabriel" tem maior frequência no Top 10. |


# Passo a passo para fazer o desafio funcionar


### 1. Clone o repositório

git clone https://github.com/YagoTorelly/desafio_revio.git


### 2. Navega para a pasta do desafio

cd desafio_revio

### 3. Executa o código 

"python main.py"

### 4. Utiliza o Swagger UI para visualização do funcionamento de cada GET
![image](https://github.com/user-attachments/assets/acd9ae41-c3ec-4aec-ad2a-64a2ab310b98)








## Instalar as Bibliotecas que contem nesse projeto 

### pip install fastapi uvicorn requests time 





