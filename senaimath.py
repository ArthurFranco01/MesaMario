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