# Extracao De Comentarios Do Mercado Livre

## Introdução

🤖 Robo feito em python para extração de comentários de produtos no mercado livre usando web scraping 🤖

Criado e desenvolvido por Thallyson luiz


## Como usar:
siga as sequintes instruções passo a passo

## 1. Inicie um ambiente virtual
    python -m venv venv

## 2. Ative seu ambiente virtual
    windows: venv\Scripts\activate
    linux/mac: source venv/bin/activate
    
## 3. Instale as dependencias
    pip install -r requirements.txt

## 4. Introduza o arquivo .env
o arquivo .env tera os dados que voçê deseja passar para que a aplicação funcione, ha um arquivo EXEMPLE demonstrando como ele deve ser introduzido.
no arquivo .env-EXEMPLE remova o -EXEMPLE do nome do arquivo, tornando ele um .env

    antes: .env-EXEMPLE

    depois: .env

## 5. Mude as variaveis de ambiente

dentro do arquivo .env renomeado, mude a propriedade "CHANG-ME" para os valores desejados.

    EX: URL_DO_PRODUTO="https://www.mercadolivre.com.br/"

## 6. Inicie o Robo

no diretorio inicial do arquivo rode o comando
    python -m src.main

## 7. Obtendo arquivo json

    Apos todas as etapas terem sido concluidas corretamente o robo
    ira salvar os comentarios em um arquivo .json com o nome do produto.
    O arquivo estara localizado no diretorio inicial do projeto
    onde voçẽ podera mover para qualquer diretorio do seu computador!

## Termos de uso

Ao usar o código você aceita os termos disponíveis no arquivo LICENSE.

Além da licença de distribuição, o bot é disponibilizado para uso
sob sua total responsabilidade, o uso do robo para fins ilegais
é extritamente proibido.

Use com responsabilidade. Apenas para maiores de 18 anos.
