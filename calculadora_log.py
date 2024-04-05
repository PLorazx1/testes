ctt=0

print('Bem vindo à calculadora de log, vamos começar!')

while ctt==0:


    b=int(input('qual a base do logaritmo? '))
    n=int(input('qual o logaritmando? '))

    taxa_erro=0.001
    baixo=0
    alto=n
    tentativa=(baixo+alto)/2
    n_tentativas=0

    while abs(b**tentativa-n)>taxa_erro:
        if b**tentativa>n:
            alto=tentativa
        else:
            baixo=tentativa
        tentativa=(baixo+alto)/2
        n_tentativas+=1
    print('o numero de tentativas foi' , n_tentativas)
    print(tentativa , 'é o logaritmo de' , n , 'na base' , b)

    dnv=input('deseja continuar calculando? ')
    if dnv!=('sim'):
        print('obrigado por usar a calculadora!')
        break
