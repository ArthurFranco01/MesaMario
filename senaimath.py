
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