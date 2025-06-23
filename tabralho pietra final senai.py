from InquirerPy import prompt
from datetime import datetime
import re

# Dicionário da tabela Fipe
tabela_fipe = {
    "Gol": 75000, "Polo": 105000, "Virtus": 125000, "T-Cross": 140000, "Nivus": 135000,
    "Onix": 75000, "Cruz": 160000, "Spin": 115000, "S10": 190000,
    "Corolla": 145000, "Yaris": 95000, "Hilux": 230000, "Etios": 85000, "SW4": 285000
}

# Lista de veículos
veiculos_venda = ["Civic 2020", "Onix 2021", "SW4", "Corolla", "Etios", "Yaris", "Hilux", "S10", "Spin", "Cruz", "Nivus"]
veiculos_aluguel = ["Corolla 2019", "HR-V 2022", "Yaris", "SW4", "Spin", "T-Cross"]

# Lista de histórico
historico = []

# Validação do nome com loop
while True:
    nome = input("👤 Qual é o seu nome? \n").strip()
    if re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ ]+", nome):
        break
    else:
        print("❌ Seu nome só pode conter letras e espaços. Tente novamente.")

# Validação do telefone com loop
while True:
    telefone = input("📞 Telefone (só pra formalidade, relaxa!): ").strip()
    if re.fullmatch(r"[0-9()\-\s]+", telefone):
        break
    else:
        print("❌ O telefone deve conter apenas números, espaços, hífens e parênteses. Tente novamente.")

# Validação do saldo com loop
while True:
    try:
        saldo = float(input("💰 Quantos de badalo você tem R$: "))
        break
    except ValueError:
        print("❌ Valor inválido para saldo. Digite um número válido.")

cliente = {"nome": nome, "telefone": telefone, "saldo": saldo}

print(f"\n🚀 Bem-vindo ao Sistema de Veículos do CHICO COINS, {cliente['nome']}! 🚙")

# Menu principal
while True:
    perguntas = [
        {
            "type": "list",
            "name": "opcao",
            "message": f"🛠️ O que deseja fazer hoje, {cliente['nome']}?",
            "choices": ["🛻 Vender veiculo", "🚗 Alugar veiculo", "🚙 Comprar veiculo", "📜 Ver histórico", "❌ Sair"],
        }
    ]
    resposta = prompt(perguntas)["opcao"]

    if resposta == "🛻 Vender veiculo":
        print("\n>>> Venda de Veículo <<< 🛻")
        modelo = input("📄 Informe o modelo do veículo (Ex: Gol, Onix, SW4): ").strip()
        if modelo not in tabela_fipe:
            print("❌ Esse modelo não está na tabela FIPE, meu parceiro.")
            continue
        valor_fipe = tabela_fipe[modelo]
        proposta = valor_fipe * 0.88
        print(f"🤑 O valor avaliado foi R$ {valor_fipe:.2f}. A gente te paga R$ {proposta:.2f}")
        if input("🤔 Aceita a proposta? (s/n): ").lower() == 's':
            cliente["saldo"] += proposta
            veiculos_venda.append(modelo)
            historico.append({
                "tipo": "venda",
                "veiculo": modelo,
                "valor": proposta,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M")
            })
            print(f"✅ Venda realizada! 💰 Novo saldo: R$ {cliente['saldo']:.2f}")
        else:
            print("❌ Tá duro, dorme. Além de pobre, perde meu tempo.")

    elif resposta == "🚗 Alugar veiculo":
        print("\n>>> Aluguel de Veículo <<< 🚗")
        if not veiculos_aluguel:
            print("🚫 Não tem carro pra alugar no momento, foi mal aí pae.")
            continue
        perguntas = [
            {
                "type": "list",
                "name": "veiculo",
                "message": "🚗 Escolha um veículo pra alugar:",
                "choices": veiculos_aluguel,
            }
        ]
        veiculo = prompt(perguntas)["veiculo"]
        try:
            dias = int(input("📆 Quantos dias deseja alugar? "))
        except ValueError:
            print("❌ Número de dias inválido.")
            continue
        custo = dias * 77
        if cliente["saldo"] >= custo:
            cliente["saldo"] -= custo
            veiculos_aluguel.remove(veiculo)
            historico.append({
                "tipo": "aluguel",
                "veiculo": veiculo,
                "valor": custo,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M")
            })
            print(f"✅ Aluguel confirmado 🚗 R$ {custo:.2f} debitados. Saldo atual: R$ {cliente['saldo']:.2f}")
        else:
            print("💸 Saldo insuficiente. Tá duro, dorme. Aluguel cancelado.")

    elif resposta == "🚙 Comprar veiculo":
        print("\n>>> Compra de Veículo <<< 🚙")
        if not veiculos_venda:
            print("🚫 Não tem carro à venda no momento, errei, fui mlk.")
            continue
        perguntas = [
            {
                "type": "list",
                "name": "veiculo",
                "message": "🚙 Escolha um veículo pra comprar:",
                "choices": veiculos_venda,
            }
        ]
        veiculo = prompt(perguntas)["veiculo"]
        if veiculo not in tabela_fipe:
            print("❌ Veículo sem preço definido na FIPE.")
            continue
        valor_fipe = tabela_fipe[veiculo]
        preco_compra = valor_fipe * 1.25
        if cliente["saldo"] >= preco_compra:
            cliente["saldo"] -= preco_compra
            veiculos_venda.remove(veiculo)
            historico.append({
                "tipo": "compra",
                "veiculo": veiculo,
                "valor": preco_compra,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M")
            })
            print(f"✅ Compra confirmada 🚙 R$ {preco_compra:.2f} debitados. Saldo atual: R$ {cliente['saldo']:.2f}")
        else:
            print("💸 Saldo insuficiente. Compra cancelada.")

    elif resposta == "📜 Ver histórico":
        print("\n📜 Histórico de Transações:")
        if not historico:
            print("🔍 Nenhuma transação foi realizada ainda.")
        else:
            for h in historico:
                print(f"- [{h['data']}] {h['tipo'].capitalize()} de {h['veiculo']} por R$ {h['valor']:.2f}")

    elif resposta == "❌ Sair":
        print("👋 Tchau, obrigado! 🚗💨 Volte sempre.")
        break
