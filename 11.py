from funcao05 import converter_metro_para_centimetros
from funcao06 import calcular_area_do_circulo
from funcao07 import calcular_area_quadrado


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
            calcular_area_do_circulo()  
        elif opcao == "3":
            calcular_area_quadrado()
        elif opcao == "0":
            print(" Encerradno o programa! ")
            break
        else:
            print(" Opção invalida! - Tente outra vez. ")


menu()
