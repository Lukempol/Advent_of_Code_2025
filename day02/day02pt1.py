ranges = []

with open('day02.txt') as dados:
    for i in dados.read().split(','):
        a , b = (i.split('-'))
        ranges.append((int(a), int(b)))

def is_invalid(num):
    num_str = str(num)
    size = int(len(num_str))
    if size % 2 != 0:
        return False
    if num_str[:size//2] == num_str[size//2:]:
        return True
    return False

# Parte 1
count = 0
for interval in ranges:
    for num in range(interval[0], interval[1]+1):
        if is_invalid(num):
            count += num

print(f'A resposta da parte 1 é igual a {count}')