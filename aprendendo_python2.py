def dobro_area_quad():
    print("**********") 
    print("** AREA **")
    print("**********\n")
    lado=float(input("Informe o lado do quadrado: "))
    area= lado**2
    dobro_area=area*2
    print("o dobro da área desse quadrilátero é {:.2f}".format(dobro_area))
def area_circ():
    print("**********")
    print("** AREA **")
    print("**********\n")
    raio=float(input("Informe o raio da circunferência: "))
    area= (raio**2)*3.14
    print("A area da cincunferência é", area)

def media():
    print("***********")
    print("** MEDIA **")
    print("***********\n")
    bim1=input("Informe a primeira nota: ")
    bim2=input("Informe a segunda nota: ")
    bim3=input("Informe a terceira nota: ")
    bim4=input("Informe a quarta nota: ")
    media=(float(bim1)+float(bim2)+float(bim3)+float(bim4))/4   
    print("A média das notas é: ", str(media))
    
def menu(): 
    print("**************************************")
    print("* 1 --> dobro da área de um quadrado *")
    print("* 2 --> área da circunferência       *")
    print("* 3 --> média de notas               *")
    print("**************************************\n")
    num=int(input("Opção desejada: "))
    if num==1:
        dobro_area_quad()
    elif num==2:
        area_circ()
    elif num==3:
        media()
    elif num!=1 and 2 and 3:
        print("Escolha uma opção válida\n")
        menu()
menu()