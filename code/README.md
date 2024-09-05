API de recomendações - xpto.com.br

Essa API de recomendações de produtos foi desenvolvida com FastAPI e fornece
recomendações de produtos com base no ID do cliente. A API utiliza de uma
base de dados de produtos.

Funcionalidades:
- Recomendação de produtos baseada no ID do cliente.

Algoritmo de recomendação:
- Como o intuito é aumentar os lucros, a recomendação é baseada no faturamento
diário de cada produto (multiplicação entre as colunas product_price e 
sales_per_day). Como o mesmo produto pode ser vendido por lojas diferentes, a
primeira etapa consiste em deduplicar os produtos, mantendo apenas aquele que
contem o maior faturamento diário. Logo após, os produtos são divididos em 5 
categorias de acordo com a faixa de faturamento diário a qual pertence.
Como os clientes são novos e não temos um perfil de compra, a recomendação é
feita com um produto aleatório de cada uma dessas categorias.
Dessa forma, abrange toda a variedade de produtos focando no faturamento.

Requisitos
- Python 3.11+
- FastAPI
- Uvicorn (para executar o servidor)
- Docker (para executar em container)
- pytest (para executar os testes unitários)
- httpx (para testes de requisições HTTP)

Instalação
- Crie um ambiente virtual:
cd code
python3 -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

- Instale as dependencias:
pip install -r requirements.txt

- Execute a aplicação localmente:
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

- Execute via docker:
docker build -t api-recommendation .
docker run -p 8000:8000 api-recommendation

- Rodar os testes unitários
pytest

- Exemplo de uso:

curl http://localhost:8000/v1/recommendations/123

- Exemplo de retorno:

{"user_id":123,"products":{"0":{"product_title":"Home Theater Sony","product_price":17.93,"product_image_url":"https://www.lorempixel.com/449/871","store_name":"Centauro"},"1":{"product_title":"Kindle Paperwhite","product_price":346.73,"product_image_url":"https://www.lorempixel.com/755/108","store_name":"Fnac"},"2":{"product_title":"Smart Lâmpada LED","product_price":529.3,"product_image_url":"https://placekitten.com/564/438","store_name":"Shoptime"},"3":{"product_title":"HD Externo Seagate","product_price":818.51,"product_image_url":"https://placekitten.com/653/655","store_name":"Casas Bahia"},"4":{"product_title":"Console Playstation 5","product_price":980.57,"product_image_url":"https://placeimg.com/205/364/any","store_name":"Carrefour"}}}


...