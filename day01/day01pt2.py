movimentações = []

with open('day01.txt') as dados:
    for linha in dados:
        movimentações.append(linha.strip())

print(movimentações)

def cofre(pos, comado):
    pos0 = pos == 0
    n =0
    direção, *deslocamento = comado

    if len(deslocamento) > 2:
        n, deslocamento = int("".join(deslocamento[:-2])), int("".join(deslocamento[-2:]))
        #print(n, deslocamento, ": " , comado, flush=True)
    else:
        deslocamento = int("".join(deslocamento))

    if(direção=='L'):
        resultado = pos - deslocamento
        if resultado < 0:
            resultado = 100 + resultado
            if not pos0:
                n += 1
    elif(direção=='R'):
        resultado = pos + deslocamento
        if resultado > 99:
            resultado = resultado - 100
            if resultado != 0: 
                n += 1
    else:
        print('Valor inválido')
    if resultado==0:
        n += 1
    #print(comado, ":", resultado)
    return resultado, n

pos = 50
n0 = 0
print(len(movimentações))
for mov in movimentações:
    #print(pos, mov)
    pos, n = cofre(pos, mov)
    n0 += n
    #print(n0)

    #print(pos)


print(f'O número de vezes que a posição foi igual a zero foram: {n0} vezes.')
