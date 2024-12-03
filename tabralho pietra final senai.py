from InquirerPy import prompt

# dicionario da tabela fipe
tabela_fipe = {
    # Volkswagen
    "Gol": 75000,
    "Polo": 105000,
    "Virtus": 125000,
    "T-Cross": 140000,
    "Nivus": 135000,
    # Chevrolet
    "Onix": 75000,
    "Cruz": 160000,
    "Spin": 115000,
    "S10": 190000,
    # Toyota
    "Corolla": 145000,
    "Yaris": 95000,
    "Hilux": 230000,
    "Etios": 85000,
    "SW4": 285000
}

# lista de venda de veiculo
veiculos_venda = ["Civic 2020", "Onix 2021"]
#lista de aluguel de veiculo
veiculos_aluguel = ["Corolla 2019", "HR-V 2022","HR-V 2022"]

# revceber os dados do cliente
cliente = {
    "nome": input("👤 Qual e o seu nome? "),
    "telefone": input("📞 Telefone (so pra formalidade, relaxa!): "),
    "saldo": float(input("💰 Quantos de badalo voce tem R$: "))
}

print(f"\n🚀 Bem vindo ao Sistema de Veiculos do CHICO COINS: {cliente['nome']}! 🚙")

# menu das opçoes para o usuario
while True:
    perguntas = [
        {
            "type": "list",
            "name": "opcao",
            "message": f"🛠️ O que deseja fazer hoje, {cliente['nome']}?",
            "choices": ["🛻 Vender veiculo", "🚗 Alugar veiculo", "🚙 Comprar veiculo", "❌ Sair"],
        }
    ]
    resposta = prompt(perguntas)["opcao"]

    if resposta == "🛻 Vender veiculo":
        print("\n>>> Venda de Veículo <<< 🛻")
        modelo = input("📄 Informe o modelo do veiculo (Ex: Civico 2020): ")
        if modelo not in tabela_fipe:
            print("❌ Esse modelo nao ta na tabela FIPE, meu parceiro")
            continue
        valor_fipe = tabela_fipe[modelo]
        proposta = valor_fipe * 0.88
        print(f"🤑 O valor avaliado foi R$ {valor_fipe:.2f} A gente te paga R$ {proposta:.2f}")
        if input("🤔 Aceita a proposta? (s/n): ").lower() == 's':
            cliente["saldo"] += proposta
            veiculos_venda.append(modelo)
            print(f"✅ Venda realizada! 💰 Novo saldo: R$ {cliente['saldo']:.2f}")
        else:
            print("Ta duro dorme, alem de pobre perde meu tempo")

    elif resposta == "🚗 Alugar veiculo":
        print("\n>>> Aluguel de Veículo <<< 🚗")
        if not veiculos_aluguel:
            print("🚫 nao tem carro pra alugar no momento, foi mal ae pae")
            continue
        perguntas = [
            {
                "type": "list",
                "name": "veiculo",
                "message": "🚗 Escolha um veiculo pra alugar:",
                "choices": veiculos_aluguel,
            }
        ]
        veiculo = prompt(perguntas)["veiculo"]
        dias = int(input("📆 Quantos dias deseja alugar? "))
        custo = dias * 77
        if cliente["saldo"] >= custo:
            cliente["saldo"] -= custo
            veiculos_aluguel.remove(veiculo)
            print(f"✅ Aluguel confirmado 🚗 R$ {custo:.2f} debitados. Saldo atual: R$ {cliente['saldo']:.2f}")
        else:
            print("💸 Saldo insuficiente","ta duro dorme Aluguel","cancelado.")

    elif resposta == "🚙 Comprar veiculo":
        print("\n>>> Compra de Veículo <<< 🚙")
        if not veiculos_venda:
            print("🚫 nao tem carro a venda no momento, errei fui mlk")
            continue
        perguntas = [
            {
                "type": "list",
                "name": "veiculo",
                "message": "🚙 Escolha um veiculo pra comprar:",
                "choices": veiculos_venda,
            }
        ]
        veiculo = prompt(perguntas)["veiculo"]
        valor_fipe = tabela_fipe[veiculo]
        preco_compra = valor_fipe * 1.25
        if cliente["saldo"] >= preco_compra:
            cliente["saldo"] -= preco_compra
            veiculos_venda.remove(veiculo)
            print(f"✅ Compra confirmada 🚙 R$ {preco_compra:.2f} debitados. Saldo atual: R$ {cliente['saldo']:.2f}")
        else:
            print("💸 Saldo insuficiente Compra cancelada.")

    elif resposta == "❌ Sair":
        print("👋 Tchau, obrigado! 🚗💨 Volte sempre")
        break

