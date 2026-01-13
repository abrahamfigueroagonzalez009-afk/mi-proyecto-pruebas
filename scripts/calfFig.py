#crear un arcibo calcular arias de figuras geometricas.

#las figuras geometricas son cuadrado, trianfulo, pentagono y sirculo el programa le pedira al usuario que figura calcular.

selector = 0

selector=int(input("escoje figura \n1 para cuadrado, \n2 para triangulo , \n3 para sirculo , \n4 para pentagon" ))

match selector:

    case 1:
        print("calculara area de un cuadrado")
        lado =float(input("pon el lo largo de el lado del cuadrado:"))
        area = lado**2
        print ("el area del cuadrado es :", area)

    ##########
    case 2:
        print("calcualr_area_perimetro_trangulo")
        base =float(input("pon la base del triangulo:"))
        altura=float(input("pon la altura del triangulo:"))
        area= base * altura/2
        print ("el area del trangulo  es:", area)
    #############3
    case 3:
        print("calcualr_area_perimetro_sirculo")
        radio =float(input("pon  el radio del sirculo:"))
        area=3.1416*(radio**2)
        print ("el area del sirculo es :", area)
    #########################
    case 4:
        lado = float(input("Ingrese la longitud de un lado del pentágono: "))
        apotema = float(input("Ingrese la longitud de la apotema: "))
        perimetro = 5 * lado
        area = (perimetro * apotema) / 2
        print(f"El área del pentágono es: {area}")
 
