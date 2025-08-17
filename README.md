# Extracao De Comentarios Mercado Livre

## Introdução

🤖 Robo feito em python para extração de comentários de produtos no mercado livre usando web scraping 🤖


    ❗ Atenção: O bot ainda esta em desenvolvimento e não esta pronto para uso!! havera atualizações constantemente pois assim como ele, estou em constante desenvolvimento.

## Como usar:
siga as sequintes instruções passo a passo

## 1. Inicie um ambiente virtual
    python -m venv venv

## 2. Instale as dependencias
    pip install -r requirements.txt

## 3. Introduza o arquivo .env
o arquivo .env tera os dados que voçê deseja passar para que a aplicação funcione, ha um arquivo EXEMPLE demonstrando como ele deve ser introduzido.
no arquivo .env-EXEMPLE remova o -EXEMPLE do nome do arquivo, tornando ele um .env

    antes: .env-EXEMPLE

    depois: .env

## 4. Mude as variaveis de ambiente

dentro do arquivo .env renomeado, mude a propriedade "CHANG-ME" para os valores desejados.

    EX: URL_DO_PRODUTO="https://www.mercadolivre.com.br/"

## 5. Inicie o Robo

no diretorio inicial do arquivo rode o comando
    python -m src.main

## Termos de uso

Ao usar o código você aceita os termos disponíveis no arquivo LICENSE.

Além da licença de distribuição, o bot é disponibilizado para uso
sob sua total responsabilidade, o uso do robo para fins ilegais
é extritamente proibido.

Use com responsabilidade. Apenas para maiores de 18 anos.
