import time

def PA():
    a1 = int(input('Qual o primeiro termo da progressão?\n'))
    PA = [a1]
    r = int(input('Qual a razão da progressão?\n'))
    n = int(input('Quantos valores tem a progressão?\n'))
    n-=1
    while n != 0:
        PA.append(PA[-1] + r)
        n -= 1
    print(f'Sua progressão é: {PA}')
    time.sleep(5)
    dnv = int(input('digite:\n[1] para encontrar um valor\n[2] para descobrir a soma\n[3] para criar outra progressão\n[4] para sair\n'))
    match dnv:
        case 1:
            An_PA(PA)
        case 2:
            soma_PA(PA)
        case 3:
            start()
        case 4:
            exit('Adioes hermanoo')
def An_PA(PA):
    n = int(input('Qual posição está seu objeto?\n'))
    An = PA[n - 1]
    print(f'O valor que desejas é {An}')
    time.sleep(5)
    dnv = int(input('Desejas algo mais?\n[0] para sair\n[1] para voltar do início\n'))
    match dnv:
        case 0:
            exit('Adioes hermanoo')
        case 1:
            start()
def soma_PA(PA):
    print(f'A soma de sua PA é {sum(PA)}')
    time.sleep(5)
    dnv = int(input('Desejas algo mais?\n[0] para sair\n[1] para voltar do início\n'))
    match dnv:
        case 0:
            exit('Adioes hermanoo')
        case 1:
            start()

def PG():
    a1 = int(input('Qual o primeiro termo da progressão?\n'))
    PG = [a1]
    q = int(input('Qual o quociente da progressão?\n'))
    n = int(input('Quantos valores tem a progressão?\n'))
    n-=1
    while n != 0:
        PG.append(PG[-1] * q)
        n -= 1
    print(f'Sua progressão é: {PG}')
    time.sleep(5)
    dnv = int(input('digite:\n[1] para encontrar um valor\n[2] para descobrir a soma\n[3] para criar outra progressão\n[4] para sair\n'))
    match dnv:
        case 1:
            An_PG(PG)
        case 2:
            soma_PG(PG)
        case 3:
            start()
        case 4:
            exit('Adioes hermanoo')
def An_PG(PG):
    n = int(input('Qual posição está seu objeto?\n'))
    An = PG[n - 1]
    print(f'O valor que desejas é {An}')
    time.sleep(5)
    dnv = int(input('Desejas algo mais?\n[0] para sair\n[1] para voltar do início\n'))
    match dnv:
        case 0:
            exit('Adioes hermanoo')
        case 1:
            start()
def soma_PG(PG):
    print(f'A soma de sua PG é {sum(PG)}')
    time.sleep(5)
    dnv = int(input('Desejas algo mais?\n[0] para sair\n[1] para voltar do início\n'))
    match dnv:
        case 0:
            exit('Adioes hermanoo')
        case 1:
            start()

def start():
    print('Opaa, bora calcular a sua progressão?')
    prog = input('Estamos falando de uma PA ou uma PG?\n')
    if prog == 'PA':
        PA()
    elif prog == 'PG':
        PG()
    else:
        print('Perae... não entendi, bora começar de novo kk')
        start()

start()
