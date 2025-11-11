import csv

def gerar_orcamento(imovel):
    contrato_total = 2000
    contrato_parcela = contrato_total / 5

    if imovel.tipo == "apartamento":
        valor_base = 700
        if imovel.quartos == 2:
            valor_base += 200
        if imovel.garagem:
            valor_base += 300
        if imovel.sem_criancas:
            valor_base *= 0.95
    elif imovel.tipo == "casa":
        valor_base = 900
        if imovel.quartos == 2:
            valor_base += 250
        if imovel.garagem:
            valor_base += 300
    elif imovel.tipo == "estudio":
        valor_base = 1200
        if imovel.vagas_estacionamento >= 2:
            valor_base += 250
            if imovel.vagas_estacionamento > 2:
                valor_base += (imovel.vagas_estacionamento - 2) * 60
    else:
        raise ValueError("Tipo de imóvel inválido")

    aluguel_mensal = valor_base
    total_mensal = aluguel_mensal + contrato_parcela

    print(f"\nResumo do orçamento:")
    print(f"Tipo: {imovel.tipo}")
    print(f"Aluguel mensal: R$ {aluguel_mensal:.2f}")
    print(f"Contrato (5x): R$ {contrato_parcela:.2f}")
    print(f"Total mensal: R$ {total_mensal:.2f}")

    with open("parcelas_orcamento.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Mês", "Valor Mensal"])
        for mes in range(1, 13):
            writer.writerow([f"Mês {mes}", f"{total_mensal:.2f}"])

    print("\nArquivo 'parcelas_orcamento.csv' gerado com sucesso.")
