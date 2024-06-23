import pyttsx3
import numpy

engine = pyttsx3.init()
def falar(texto, voz='brazil'):
    engine.setProperty('voice', voz)
    engine.say(texto)
    engine.runAndWait()
    
    
prato = 15
pilha = list(range(1, prato + 1))
while True:
    print(f"\nexistem {(len(pilha))} pratos na pilha")
    print(f"pilha atual: {pilha}")
    print('digite 1 para empilhar um novo, 2 para remover e 0 para sair')
    escolha = int(input("operação (1, 2 ou 0)"))
    if escolha == 1:
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"prato {lavado} lavado")
            voice = f"prato {lavado} lavado"
            falar(voice)
        else:
            print("pilha vazia!")
    elif escolha == 2:
        prato += 1 #novo prato
        pilha.append(prato)
        voice1 = f"adicionado"
        falar(voice1)
    elif escolha == 0:
        break
    else:
        print("escolha uma operação correta!")
        voz = "escolha uma operação correta!"
        falar(voz)
        