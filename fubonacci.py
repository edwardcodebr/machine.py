def fibonnaci(n):
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


while(True):
    print("digite um número")
    n = int(input())

    if n <= 0:
        print("insira um número inteiro positivo")
    else:
        result = fibonnaci(n)
        print("sequência de fibonacci até {}-ésimo termo.".format(n))
    print(result)