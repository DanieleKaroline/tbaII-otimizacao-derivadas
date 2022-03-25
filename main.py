#importacao das bibliotecas para utilizar
import math

#funcao menu
def menu():
    
    print("\nDigite a opção desejada: \n 1 - Custo da lata\n 2 - Distancia\n 0 - Sair")

    i = 1
    while i == 1: 
        op = int(input("Digite a opcao: "))

        if op == 1:
            lata()
        if(op == 2):
            distancia()
        if op == 0:
            print("saindo...")
            i = 0
            exit()
    

#funcao lata
def lata():
    #solicita os valores de entrada
    x = float(input("\nDigite o valor de X (laterais): "))
    y = float(input("Digite o valor de Y (base e topo): "))
    v = float(input("Digite o valor de V (volume): "))

    #valor de pi para usar nos calculos
    pi = 3.14
    #calculo do raio. ** -> indica potenciação
    r = ((v*y)/(2*x*pi))**(1/3)
    #calculo da altura
    h = v/(pi*(v*y))/((2*x*pi)**(1/3))**2
    #calculo da base
    base = pi*(r**2)
    #calculo das laterais
    lateral = (2*pi)*r*h
    #calculo da superficie
    area_s = ((2*pi)*(r*h))+((2*pi)*(r**2))

    #custo da base e altura
    c_base = base*x
    c_lateral = lateral*y

    #valor total
    preco = c_base+c_lateral

    #resultados
    print("\n<------------------------------>")
    print(f'\nRaio da base: {r:.2f}\n' )
    print(f'Preco: R${preco:.2f}\n')
    print(f'Altura da lata: {h:.2f}\n')
    print(f'Area da base: {base:.2f}\n')
    print(f'Area da lateral: {lateral:.2f}\n')
    print(f'Area da superficie: {area_s:.2f}\n')

    menu()

def distancia():
    #ilha = 40km
    #cidade = 100km

    #solicita-se os dados de entrada
    x = float(input("Digite a velocidade da barca (x): "))
    y = float(input("Digite a velocidade do carro (y): "))
    xy = (y**2)-(x**2)
    
    #calculo da distancia da estação até a ilha e distancia total
    d = 100-math.sqrt((40**2)*(x**2)/xy)
    dt = d + math.sqrt((40**2)+((100-d)**2))

    
   
    print(f"\nDistancia da estação até a cidade: {d:.2f}km")
    print(f"Distancia da ilha até a cidade (total): {dt:.2f}km")
    
    menu()
 
#main
menu()