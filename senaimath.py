# Funcao para Log de numero Natural

# Bloco 1: cálculo de y
def calcular_y(x):
    return (x - 1) / (x + 1)

# Bloco 2: calculo de potencia
def potencia(y, n):
    return y ** (2*n + 1)

# Bloco 3: calculo do denominador
def denominador(n):
    return 2*n + 1

# Bloco 4: calculo do termo
def termo_serie(y, n):
    p = potencia(y, n)
    d = denominador(n)
    return p / d

# Bloco 5: calculo da soma dos termos
def somatorio(y, k):
    soma = 0
    for n in range(k + 1):
        soma += termo_serie(y, n)
    return soma

# Log
def ln_aprox(x, k=10):
    y = calcular_y(x)
    soma = somatorio(y, k)
    return 2 * soma

# entrada de dados

x = float(input("Digite o valor de x: "))
k = int(input("Digite o número de termos da série (k): "))

resultado = ln_aprox(x, k)

print(f"ln({x}) ≈ {resultado:.2f}")