def verifica_triangulo(a, b, c):

    if a < b + c and b < a + c and c < a + b:
        return True
    return False

def calcula_area(a, b, c):

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))


if verifica_triangulo(a, b, c):
    area = calcula_area(a, b, c)
    print(f"Os valores formam um triângulo. A área do triângulo é: {area:.2f}")
else:
    print(f"Os valores {a}, {b}, {c} não formam um triângulo.")