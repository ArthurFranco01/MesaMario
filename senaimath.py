#GUSTAVO GIGLIO OSS AGORA VAI MESMO

def exponencial(x,y):
    numero=x**y
   
    return numero
   

def fatorial(n):
    if n < 0:
        return "Fatorial não existe para números negativos."
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
       
    return resultado
    

def cosseno(nume):
    resultado=1-(exponencial(w,2)/fatorial(2))+(exponencial(w,4))/fatorial(4)-(exponencial(w,6))/fatorial(6)+(exponencial(w,8))/fatorial(8)-exponencial(w,10)/fatorial(10)
    print(resultado)
    return resultado

    


w = float(input("dig"))
cosseno(w)
exponencial(w,2)
exponencial(w,4)
exponencial(w,6)   
exponencial(w,8)

