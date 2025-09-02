def fatorial(n, show=True):
    s = 1
    for c in range(n, 0, -1):
        cont = c * n
        if show==True:
            if c >= 2:
                 print(f"{c} x ", end='')
            if c <2:
                print(f"1 = {s}")
        s *= c
    return s
            


print("=-"*20)
print("Calculando o fatorial de um número: ")
print("=-"*20)
n = int(input("Digite um número para o fatorial: "))
conta = str(input('Deseja mostrar a conta? (sim/não): '))
if conta == "sim":
    conta1 = bool(conta.lower() == "true") ## o comando "bool" define um valor como verdaeiro.
else:
    print("você optou por não mostrar a conta do fatorial.")
    conta1 = False

print(fatorial( n, conta1))
