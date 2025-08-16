def converter_metro_para_centimetros():
    metros = float(input('Metros: '))
    centimetros = metros * 100
    print(f'{metros} m = {centimetros} cm') 

   

print("------------------------------------------------------------------")

def area_circulo():

    raio = float(input('Informe o raio de um círculo: '))
    area = float((raio ** 2) * 3.14)  # (A = π r²) pi=3,1415
    print(f'Com um círculo de raio {raio} temos um círculo de área {area}.')  


print("------------------------------------------------------------------")

def area_quadrado():

    lado = float(input('Informe  de um quadrado: '))        
    dobro = (lado**2) * 2                   
    area = lado**2  
    print(f'O dobro área do quadrado informado é de {dobro}')


def menu():
    while True:
        print("\n -- Menu de opções: ")
        print(" 1 - converter_metro_para_centimetros ")
        print(" 2 . area_circulo ")  
        print(" 3 - area_quadrado ")
        print(" 0 -  sair ")

        opcao = input(" Escolha um aopção: ")
        if opcao == "1":
            converter_metro_para_centimetros()
        elif opcao == "2":
            area_circulo()  
        elif opcao == "3":
            area_quadrado()
        elif opcao == "0":
            print(" Encerradno o programa! ")
            break
        else:
            print(" Opção invalida! - Tente outra vez. ")


menu()




       








