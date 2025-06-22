# 💰 Sistema Bancário em Python — V1

Este projeto foi desenvolvido como parte de um desafio proposto por um banco fictício. Ele simula as operações básicas de uma conta bancária utilizando Python puro e a biblioteca padrão.

---

## 📌 Funcionalidades

- ✅ Depósitos com validação
- ✅ Saques com limite de valor e quantidade diária
- ✅ Registro de extrato com data e hora
- ✅ Exibição de extrato formatado
- ✅ Sistema em loop contínuo até o usuário desejar sair

---

## 🧠 Conceitos de Python utilizados no projeto

### ➕ Operadores Aritméticos

Utilizei para cálculos de saldo e controle de limites:

python
saldo += valor          # Soma valor ao saldo (depósito)
saldo -= valor          # Subtrai valor do saldo (saque)
excedeu_saldo = valor > saldo    # Verifica se o saque é maior que o saldo


Também são usados para comparações (>, >=) e contagem de saques (numero_saques += 1).

---

### 🔀 Estruturas Condicionais

Usadas para *tomar decisões* com base em condições:

python
if valor > 0:
    saldo += valor
    registrar_operacao("Depósito", valor)
elif valor <= 0:
    print("Valor inválido.")


Também usadas para:
- Verificar se excedeu o limite de saque
- Validar opção digitada pelo usuário
- Exibir mensagens diferentes no extrato

---

### 🔁 Estruturas de Repetição

A repetição principal é feita com while True, que mantém o sistema rodando até que o usuário escolha sair (q):

python
while True:
    opcao = input(menu).lower().strip()

    if opcao == "q":
        break


Esse loop permite que o usuário realize várias operações seguidas no sistema.

---

### 🧵 Métodos da Classe String

Utilizei diversos métodos internos da classe str:

python
opcao = input(menu).lower().strip()


- .lower() → transforma a entrada em minúscula
- .strip() → remove espaços antes e depois
- .append(...) → adiciona a string do extrato à lista
- .format() (usado indiretamente com f-strings) → para formatar os valores

---

### 💬 Interpolação de Variáveis

Feita com *f-strings*, forma moderna e eficiente de embutir variáveis dentro de strings:

python
print(f"Saldo atual: R$ {saldo:.2f}")
operacao = f"{timestamp} - Saque: R$ {valor:.2f}"


Usei :.2f para exibir valores com *duas casas decimais*, no padrão monetário brasileiro.

---

### 🔍 Fatiamento de Strings

Não utilizei diretamente fatiamento no estilo clássico, como texto[0:5], mas usei a função strftime() da classe datetime para *fatiar e formatar a string da data*:

python
timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


Isso gera uma string da data no formato brasileiro, a partir de um objeto completo datetime.

---

### 📄 Strings de Múltiplas Linhas

Usadas para exibir o menu principal com clareza visual e legibilidade:

python
menu = """
=============== MENU ===============

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


Também são usadas para imprimir o extrato com blocos visuais como:

python
print("\n================ EXTRATO ================")


---

## 🧾 Requisitos Técnicos Atendidos

- [x] Saques limitados a R$ 500 por operação
- [x] Máximo de 3 saques diários
- [x] Validação de entrada (valores negativos, letras, etc.)
- [x] Registro de data/hora das transações com datetime
- [x] Exibição do saldo atualizado ao final do extrato

---

## 🕓 Módulo Extra: datetime

Foi utilizado o módulo datetime para *registrar data e hora de cada operação*:

python
from datetime import datetime


Usado assim:

python
timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


Essa funcionalidade traz *rastreabilidade* para os registros no extrato, como um sistema bancário real faria.

---

## 🤝 Agradecimentos

Sou grato ao conteúdo fornecido pelo curso, que foi essencial para minha participação e execução  deste projeto. 