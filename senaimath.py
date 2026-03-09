#Definir os valores iniciais (sem espaços no começo da linha)
x = 2            # O valor de x que você quer calcular
limite = 10      # Quantos termos somar (precisão)
soma = 0
n = 0

#loop principal
while n < limite:
    potencia = x ** n  # Calcula x elevado a n

    #Cálculo do fatorial de maneira "burra"
    fatorial = 1
    j = 1
    while j <= n:
        fatorial = fatorial * j
        j += 1

    termo = potencia / fatorial
    soma = soma + termo
    
    n = n + 1  # Vai para o próximo n

#resultado final
print("Resultado da soma:")
print(soma)