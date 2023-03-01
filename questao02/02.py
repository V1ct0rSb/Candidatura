# Lista
lista = [0, 1]

# Entrada
num = int(input("Informe um número: "))

while True:
    # Tamanho da lista
    tamanho = len(lista)

    # Ultimo valor da lista
    ultimoValor = tamanho - 2
    penultValor = tamanho - 1

    # Proximo valor da sequencia e add na lista
    somaFinal = lista[ultimoValor] + lista[penultValor]
    lista.append(somaFinal)

    # Verificar se a entrada estar na sequencia de Fibonacci
    if num < lista[ultimoValor] or num < 0:
        print('=-' * 5)
        print(f"Sequência de Fibonacci: {lista}")
        print(f'O número {num} NÃO ESTÁ na sequência de Fibonacci!!')
        break

    elif num == lista[ultimoValor]:
        print('=-' * 5)
        print(f"Sequência de Fibonacci: {lista}")
        print(f'O número {num} ESTÁ na sequência de Fibonacci!!')
        break
