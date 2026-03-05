def pi(n_termos=100000000): #numero default de termos cem milhões
    pi_quarto = 0
    for n in range(n_termos):
        termo = ((-1)**n) / (2*n + 1)
        pi_quarto += termo
    
    return pi_quarto * 4


aproximacao = pi()
print(f"PI aproximado: {aproximacao}")