# Desafio Neoway - Esteira completa para aplicação Go

Esse repositório consiste em criar uma esteira completa para uma aplicação desenvolvida em Golang. A esteira deve conter os seguintes passos:

- Provisionamento da infraestrutura
- Teste da aplicação
- Build da imagem da aplicação
- Deploy da aplicação

## Provisionamento da infraestrutura

Para infraestrutura foi escolhido a nuvem AWS e a ferramenta de IaC Terraform.

No Terraform foram criados 4 arquivos:
- ec2.tf - Realiza a criação da máquina virtual e do par de chaves SSH.
- provider.tf - Determina o provedor de nuvem e também estabelece o vinculo ao workspace no Terraform Cloud.
- sg_allow_http.tf - Cria o grupo de segurança para liberação de acesso HTTP.
- sg_allow_ssh.tf - Cria o grupo de segurança para liberação de acesso SSH somente para a rede 172.31.0.0/16.

Todo o processo de provisionamento ocorre através da pipeline "Terraform"

## Teste da aplicação

O teste da aplicação é realizado através do próprio Golang pelo comando "go test -coverprofile=coverage.out ./..." e ocorre através da pipeline "Build App"

## Build da imagem da aplicação

O Build da aplicação é feita em Docker e ocorre através da pipeline "Build App"

## Deploy da aplicação

O deploy da aplicação consiste em um script desenvolvido em Python que faz o acesso SSH no servidor provisionado e realiza a instalação do Docker e em seguida, realiza o docker run da imagem da aplicação.
Esse processo é executado na pipeline "App Deploy"