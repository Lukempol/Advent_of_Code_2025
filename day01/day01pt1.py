movimentações = []

with open('day01.txt') as dados:
    for linha in dados:
        movimentações.append(linha.strip())

def cofre(pos, comado):
    direção, *deslocamento = comado

    if len(deslocamento) > 2:
        deslocamento =  int("".join(deslocamento[-2:]))
    else:
        deslocamento = int("".join(deslocamento))

    if(direção=='L'):
        resultado = pos - deslocamento
        if resultado < 0:
            resultado = 100 + resultado
    elif(direção=='R'):
        resultado = pos + deslocamento
        if resultado > 99:
            resultado = resultado - 100
    else:
        print('Valor inválido')

    if resultado==0:
        n += 1
    return resultado, n

pos = 50
n0 = 0

for mov in movimentações:
    pos, n = cofre(pos, mov)
    n0 += n

print(f'O número de vezes que a posição foi igual a zero foram: {n0} vezes.')
