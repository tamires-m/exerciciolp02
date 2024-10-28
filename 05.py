def inverter_palavras(frase):

    palavras_invertidas = [palavra[::-1] for palavra in frase.split()]

    nova_frase = ' '.join(palavras_invertidas)
    return nova_frase


frase_original = (input("Digite uma frase: "))
resultado = inverter_palavras(frase_original)
print(resultado)