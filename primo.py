#definição de número primo

def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while(True):
    print("digite um numero:")
    num = int(input())

    if primo(num):
        print("é primo")
    else:
        print("não é primo")