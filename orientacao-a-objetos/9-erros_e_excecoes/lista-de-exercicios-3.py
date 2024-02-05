## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

def calcular_media(valores):
    tamanho = 0
    soma = 0.0
    media_calculada = 0
    for i in range(len(valores)):
        soma += valores[i]
        tamanho += 1
    media_calculada = soma / tamanho
    return media_calculada

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = False
    elif valor.isdigit():
        valores.append(int(valor))

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))