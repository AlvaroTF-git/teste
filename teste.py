from time import sleep

def contador(inicio=0, fim=0, passo=0):
    print('-=' * 20)
    print(f'contagem de {inicio} até {fim}, com passo de {passo}: ')
    print('-=' * 20)
    if passo < 0:
        passo *= -1
    while True:
        ##contador decrescente
        if inicio >= fim:
            if passo == 0:
                print("Erro, seu passo não pode ser 0!")
                break
            sleep(0.5)
            print(f"{inicio} |", end=' ', flush=True)
            inicio -= passo
            if inicio < fim:
                break
        ##contador crescente
        elif inicio <= fim:
            if passo == 0:
                print("Erro, seu passo não pode ser 0!")
                break
            sleep(0.5)
            print(f"{inicio} |", end=' ', flush=True) ##flush evita buffer, permitindo utilização correta do (sleep)
            inicio += passo
            if inicio > fim:
                break 
        else:
            break
          
    print('FIM!')
            
    
print('Contador!')
contador(0, 10, 2)
contador(10, 0, 2)
print()
print("Agora é sua vez de personalizar a contagem :") 
contador(int(input("inicio--> ")), int(input("fim--> ")), int(input("passo--> ")))