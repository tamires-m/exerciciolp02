
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))


menor = num1

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3


print(f"O menor número é: {menor}")