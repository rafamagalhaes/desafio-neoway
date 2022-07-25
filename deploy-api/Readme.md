# Script para instalação do Docker e deploy da aplicação

## Criação do arquivo de chave privada

O script "Key_pair.sh" foi para criar o arquivo de conexão SSH no servidor provisionado.

## Instalação do Docker e deploy da aplicação

O script "deploy-api.py" foi desenvolvido para executar os seguintes passos:
- Lista as instâncias EC2 na AWS e faz a busca pelo servidor provisionado.
- Armazena o IP público do servidor
- Realiza uma conexão SSH no servidor
- Realiza a instalação do Docker
- Realiza o deploy da aplicação