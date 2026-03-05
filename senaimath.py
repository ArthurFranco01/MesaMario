#thyerrisson
def calcular_euler(precisao=10):
    e_calculado = 1
    fatorial = 1

    for num in range(0,precisao):
        if num > 0:
            fatorial *= num
            e_calculado += 1 / fatorial
    return e_calculado

calculo_euler = calcular_euler(10)

print(f"O valor de e calculado com a precisao de {10} é de {calculo_euler}!")
#Arthur
def pi(n_termos=100000000): #numero default de termos cem milhões
    pi_quarto = 0
    for n in range(n_termos):
        termo = ((-1)**n) / (2*n + 1)
        pi_quarto += termo
    
    return pi_quarto * 4


aproximacao = pi()
print(f"PI aproximado: {aproximacao}")

#Thiago
anguloRecebido = float(input("Digite o ângulo em graus: "))


pi = 3.141592653589793

k = 10

def radiano(angulo):
    rad = angulo * pi / 180
    return rad

radianoConvertido = radiano(anguloRecebido)


def funcao_taylor(rad, k):
    sin = 0

    for pedaco in range(k):
        
        fatorialAtual = 2 * pedaco + 1

        fatorialCalc = 1
        for i in range(1, fatorialAtual + 1):
            fatorialCalc *= i

        formula = (((-1) ** pedaco) * (rad ** (2 * pedaco + 1))) / fatorialCalc
        sin += formula

    return sin
  

resultado = funcao_taylor(radianoConvertido, k)
print(f'O seno do angulo {anguloRecebido} = {resultado:.6f}')

#thaina
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
