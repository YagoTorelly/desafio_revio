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


## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/YagoTorelly/desafio_revio.git


### 2. Navega para a pasta do desafio

'''bash
cd desafio_revio

### 3. Executa o código 

"python main.py"

### 4. Utiliza o Swagger UI para visualização do funcionamento de cada GET

![image](https://github.com/user-attachments/assets/b6cf1185-52c7-40b9-8405-083738ccfc19)





### pip install fastapi uvicorn requests





