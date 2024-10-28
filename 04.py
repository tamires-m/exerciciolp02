def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for n in range(1, 101):
    if is_primo(n):
        print(f"{n} é primo")
    else:
        print(f"{n} não é primo")