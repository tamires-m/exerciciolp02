def calcular_idade(dias):
    anos = dias // 365
    dias_restantes = dias % 365
    meses = dias_restantes // 30
    dias_finais = dias_restantes % 30

    return anos, meses, dias_finais



idade_em_dias = int(input("Digite sua idade em dias: "))


anos, meses, dias = calcular_idade(idade_em_dias)


print(f"Sua idade é: {anos} anos, {meses} meses e {dias} dias.")