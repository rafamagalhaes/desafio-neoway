terraform {
  cloud {
    organization = "Minha"

    workspaces {
      name = "Desafio_Neoway"
    }
  }
}

provider "aws" {
    region = "us-east-1"
}