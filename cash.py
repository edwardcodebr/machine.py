import time
from tqdm import tqdm
import os

while True:
    print("seja bem-vindo ao mercadinho, digite seu preço")
    preco = int(input())
    print("gerando QR CODE de pagamento...")
    for i in tqdm(range(20)):
        time.sleep(1)
    print("QR CODE de pagamento logo abaixo:")
    print(''' 
        ---- ---- --- ---
        --- -- --- ---- -
        -- --- --- ---- -
        - -- - -- - -----
    ''')
    int(input("digite um número para fechar"))
    for i in tqdm(range(20)):
       time.sleep(1)
    os.system("cls")