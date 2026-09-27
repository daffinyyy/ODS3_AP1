# 🗳️ Civitas — Sistema de Votação baseado em Blockchain
<div style="text-align: center;">
<img src="assets\logo.png" alt="Exemplo" width="300" height="300">
</div>

Sistema de votação desenvolvido como uma aplicação de demonstração do uso de **Blockchain local** para registro de votos.

A aplicação permite cadastrar candidatos, registrar votos, consultar resultados e visualizar diretamente os blocos que compõem a Blockchain.

---

## 1. Problema

Sistemas de votação precisam garantir que os registros realizados durante uma eleição não sejam alterados indevidamente após sua confirmação.

> **Como utilizar uma estrutura de Blockchain para registrar votos de forma encadeada, verificável e resistente à alteração, mantendo uma aplicação simples e executável localmente?**

O projeto utiliza um cenário de votação para demonstrar, de forma prática, como uma Blockchain pode registrar operações e preservar o histórico das alterações realizadas.

---

## 2. Solução proposta

Foi desenvolvido um sistema de votação baseado em uma Blockchain local.

A aplicação possui uma interface gráfica desenvolvida com **Streamlit** e uma API desenvolvida com **FastAPI**, que permite ao usuário:

* cadastrar candidatos;
* consultar candidatos cadastrados;
* registrar um voto;
* consultar os resultados;
* visualizar um gráfico dos votos;
* visualizar os blocos da Blockchain;
* baixar a Blockchain em formato JSON.

O voto registrado é transformado em uma operação que gera um novo bloco na Blockchain.

Cada bloco possui informações que permitem relacioná-lo ao bloco anterior, formando uma cadeia de registros.

### Fluxo básico

![fluxo](assets/fluxo.jpg)

---

## 3. Justificativa do uso de Blockchain

A Blockchain foi utilizada porque o problema envolve o **registro e preservação de operações**. Neste projeto, cada voto confirmado é registrado em um novo bloco. Os blocos possuem:

* índice;
* timestamp;
* dados da operação;
* hash do bloco anterior;
* hash associado ao eleitor;
* nonce;
* hash do próprio bloco.

Dessa forma, os blocos ficam encadeados por meio dos hashes.

Uma alteração em um bloco pode fazer com que seu hash deixe de corresponder ao valor esperado, comprometendo a validade da cadeia a partir daquele ponto.

A aplicação também utiliza **Proof of Work**, exigindo que um nonce seja encontrado de acordo com o nível de dificuldade configurado.

Assim, a Blockchain não é utilizada apenas como um banco de dados: ela é utilizada para demonstrar o conceito de **registro encadeado e verificável de operações**.

---

## 4. Arquitetura

A aplicação é composta por três partes principais:

<div style="text-align: center;">
<img src="assets\arquitetura.jpg" alt="Exemplo" width="733" height="400">
</div>

## Tecnologias utilizadas

| Tecnologia     | Função                                          |
| -------------- | ----------------------------------------------- |
| Python         | Linguagem principal                             |
| Streamlit      | Interface da aplicação                          |
| FastAPI        | API/backend                                     |
| Pydantic       | Validação dos dados recebidos                   |
| validate-docbr | Validação do CPF                                |
| Matplotlib     | Geração do gráfico de resultados                |
| Pandas         | Organização dos dados                           |
| ECDSA          | Biblioteca criptográfica utilizada pelo projeto |
| Uvicorn        | Servidor da API                                 |
| JSON           | Persistência local da Blockchain                |

---

## 5. Blockchain local

A Blockchain é executada localmente na máquina utilizada para a demonstração, sem a utilização de um serviço externo de Blockchain.

A cadeia é armazenada no arquivo:

```text
blockchain.json
```

Ao iniciar a aplicação, o sistema verifica se existe uma Blockchain previamente armazenada. Caso não exista, é criado o **bloco gênese** Quando um novo voto é registrado, um novo bloco é criado e adicionado à cadeia.

---

## 6. Contrato inteligente e regras de negócio

Neste projeto, o conceito de **contrato inteligente** é representado pela lógica de negócio responsável por validar as operações de votação antes que elas sejam registradas na Blockchain.

As regras implementadas são:

- **Regra 1 — Deve existir candidato**  
Um voto somente pode ser registrado quando existem candidatos cadastrados.

- **Regra 2 — O CPF deve ser válido**  
O sistema utiliza a biblioteca `validate-docbr` para verificar se o CPF informado possui formato e dígitos verificadores válidos.

- **Regra 3 — Um eleitor não pode votar duas vezes**  
O CPF não é armazenado diretamente na Blockchain. Antes do registro, o CPF é convertido em um hash SHA-256 e esse identificador é utilizado para verificar se aquele eleitor já realizou uma votação.

- **Regra 4 — O voto deve ser registrado na Blockchain**  
Quando todas as validações são aprovadas, a operação é registrada como um novo bloco.

---

## 7. Execução do projeto

### Requisitos

* Python 3.11 ou compatível
* pip

### Instalação

Clone o projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd ODS3_AP1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### Inicie o backend

Em um terminal:

```bash
uvicorn backend:app --host 127.0.0.1 --port 8000
```

### Inicie a interface

Em outro terminal:

```bash
streamlit run main.py
```

---
## 8. Transparência do Uso de Inteligência Artificial  

As imagens da pasta assets e o presente README foram gerados com o auxílio de Inteligência Artificial, mais especificamente os modelos Gemini 3.6 Flash para as imagens e GPT-5.6 Luna para o README. Todo conteúdo gerado foi eventualmente revisado por um humano para garantir integridade e qualidade.
