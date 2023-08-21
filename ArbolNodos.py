class Arbol(object):
    def __init__(self):
        self.der=None
        self.izq=None
        self.cent=None
        self.dato=None

print("Este programa muestra los recorridos de los nodos un árbol de únicamente 3 niveles\n\nUsted indica cual es el camino que gusta ver en pantalla\n\nIndique a continuación se le pregunta como desea su árbol\n")
iniciar=int(input("\n¿Desea iniciar un árbol?\n\n\t0.No\t1.Sí\n"))

controlRama=0 #Indica si hay una o dos ramas en la raíz, 0 indica una sola rama y 1 indica dos ramas
controlSubRama=[0,0] #Indica si hay una o dos subramas en la rama

if(iniciar!=0):
    raiz=Arbol()
    raiz.dato=input("\nIngrese el dato de la raíz: ")
    preg=int(input("\n\n¿Desea una rama izquierda y una derecha?\n\n\t0.Solo una rama\t1.Sí\n"))
    controlRama=preg
    if(preg==1):
        raiz.izq=Arbol()
        raiz.izq.dato=input("\nIngrese el dato de la rama izquierda: ")
        preg=int(input("\n¿Desea una subrama izquierda y una derecha en esta rama?\n\n\t0.Solo una subrama\t\t1.Sí\n"))
        controlSubRama[0]=preg
        if(preg==1):
            raiz.izq.izq=Arbol()
            raiz.izq.izq.dato=input("\n\tIngrese el dato de la subrama izquierda: ")
            raiz.izq.der=Arbol()
            raiz.izq.der.dato=input("\n\tIngrese el dato de la subrama derecha: ")
        elif(preg==0):
            raiz.izq.cent=Arbol()
            raiz.izq.cent.dato=input("\n\tIngrese el dato de la subrama: ")
        
        raiz.der=Arbol()
        raiz.der.dato=input("\nIngrese el dato de la rama derecha: ")
        preg=int(input("\n¿Desea una subrama izquierda y una derecha en esta rama?\n\n\t0.Solo una subrama\t\t1.Sí\n"))
        controlSubRama[1]=preg
        if(preg==1):
            raiz.der.izq=Arbol()
            raiz.der.izq.dato=input("\n\tIngrese el dato de la subrama izquierda: ")
            raiz.der.der=Arbol()
            raiz.der.der.dato=input("\n\tIngrese el dato de la subrama derecha: ")
        elif(preg==0):
            raiz.der.cent=Arbol()
            raiz.der.cent.dato=input("\n\tIngrese el dato de la subrama: ")

    elif(preg==0):
        raiz.cent=Arbol()
        raiz.cent.dato=input("\nIngrese el dato de la rama: ")
        preg=int(input("\n¿Desea una subrama izquierda y una derecha en esta rama?\n\n\t0.Solo una subrama\t\t1.Sí\n"))
        controlSubRama[0]=preg
        if(preg==1):
            raiz.cent.izq=Arbol()
            raiz.cent.izq.dato=input("\n\tIngrese el dato de la subrama izquierda: ")
            raiz.cent.der=Arbol()
            raiz.cent.der.dato=input("\n\tIngrese el dato de la subrama derecha: ")
        elif(preg==0):
            raiz.cent.cent=Arbol()
            raiz.cent.cent.dato=input("\n\tIngrese el dato de la subrama: ")
    
    opc=int(input("\nIngrese la opción de recorrido que quiera que se muestre en pantalla:\n\n\t1.Pre-order\n\t2.In-order\n\t3.Post-order\n\t0.Salir\n\n"))
    while(opc!=0):
        if(opc==1):
            print("\nHa elegido el recorrido Pre-order:")
            if(controlRama==1 & controlSubRama[0]==1 & controlSubRama[1]==1):
                print("\n[",raiz.dato,"][",raiz.izq.dato,"][",raiz.izq.izq.dato,"][",raiz.izq.der.dato,"][",raiz.der.dato,"][",raiz.der.izq.dato,"][",raiz.der.der.dato,"]")

            if(controlRama==1 & controlSubRama[0]==1 & controlSubRama[1]==0):
                print("\n[",raiz.dato,"][",raiz.izq.dato,"][",raiz.izq.izq.dato,"][",raiz.izq.der.dato,"][",raiz.der.dato,"][",raiz.der.cent.dato,"]")

            if(controlRama==1 & controlSubRama[0]==0 & controlSubRama[1]==1):
                print("\n[",raiz.dato,"][",raiz.izq.dato,"][",raiz.izq.cent.dato,"][",raiz.der.dato,"][",raiz.der.izq.dato,"][",raiz.der.der.dato,"]")

            if(controlRama==1 & (controlSubRama[0]==0 & controlSubRama[1]==0)):
                print("\n[",raiz.dato,"][",raiz.izq.dato,"][",raiz.izq.cent.dato,"][",raiz.der.dato,"][",raiz.der.cent.dato,"]")

            if(controlRama==0 & controlSubRama[0]==1 & controlSubRama[1]==0):
                print("\n[",raiz.dato,"][",raiz.cent.dato,"][",raiz.cent.izq.dato,"][",raiz.cent.der.dato,"]")

            if(controlRama==0 & controlSubRama[0]==0 & controlSubRama[1]==0):
                print("\n[",raiz.dato,"][",raiz.cent.dato,"][",raiz.cent.cent.dato,"]")
            opc=int(input("\nOprima 0 para salir u oprima otro número del menú dado anteriormente para mostrar otro recorrido del árbol: "))

        if(opc==2):
            print("\nHa elegido el recorrido In-order")
            if(controlRama==1 & controlSubRama[0]==1 & controlSubRama[1]==1):
                print("\n[",raiz.izq.izq.dato,"][",raiz.izq.dato,"][",raiz.izq.der.dato,"][",raiz.dato,"][",raiz.der.izq.dato,"][",raiz.der.dato,"][",raiz.der.der.dato,"]")

            if(controlRama==1 & controlSubRama[0]==1 & controlSubRama[1]==0):
                print("\n[",raiz.izq.izq.dato,"][",raiz.izq.dato,"][",raiz.izq.der.dato,"][",raiz.dato,"][",raiz.der.cent.dato,"][",raiz.der.dato,"]")

            if(controlRama==1 & controlSubRama[0]==0 & controlSubRama[1]==1):
                print("\n[",raiz.izq.cent.dato,"][",raiz.izq.dato,"][",raiz.dato,"][",raiz.der.izq.dato,"][",raiz.der.dato,"][",raiz.der.der.dato,"]")

            if(controlRama==1 & (controlSubRama[0]==0 & controlSubRama[1]==0)):
                print("\n[",raiz.izq.cent.dato,"][",raiz.izq.dato,"][",raiz.dato,"][",raiz.der.cent.dato,"][",raiz.der.dato,"]")

            if(controlRama==0 & controlSubRama[0]==1 & controlSubRama[1]==0):
                print("\n[",raiz.cent.izq.dato,"][",raiz.cent.dato,"][",raiz.dato,"][",raiz.cent.der.dato,"]")

            if(controlRama==0 & controlSubRama[0]==0 & controlSubRama[1]==0):
                print("\n[",raiz.cent.cent.dato,"][",raiz.cent.dato,"][",raiz.dato,"]")
            opc=int(input("\nOprima 0 para salir u oprima otro número del menú dado anteriormente para mostrar otro recorrido del árbol: "))

        if(opc==3):
            print("\nHa elegido el recorrido Post-order")
            if(controlRama==1 & controlSubRama[0]==1 & controlSubRama[1]==1):
                print("\n[",raiz.izq.izq.dato,"][",raiz.izq.der.dato,"][",raiz.izq.dato,"][",raiz.der.izq.dato,"][",raiz.der.der.dato,"][",raiz.der.dato,"][",raiz.dato,"]")

            if(controlRama==1 & controlSubRama[0]==1 & controlSubRama[1]==0):
                print("\n[",raiz.izq.izq.dato,"][",raiz.izq.der.dato,"][",raiz.izq.dato,"][",raiz.der.cent.dato,"][",raiz.der.dato,"][",raiz.dato,"]")

            if(controlRama==1 & controlSubRama[0]==0 & controlSubRama[1]==1):
                print("\n[",raiz.izq.cent.dato,"][",raiz.izq.dato,"][",raiz.der.izq.dato,"][",raiz.der.der.dato,"][",raiz.der.dato,"][",raiz.dato,"]")

            if(controlRama==1 & (controlSubRama[0]==0 & controlSubRama[1]==0)):
                print("\n[",raiz.izq.cent.dato,"][",raiz.izq.dato,"][",raiz.der.cent.dato,"][",raiz.der.dato,"][",raiz.dato,"]")

            if(controlRama==0 & controlSubRama[0]==1 & controlSubRama[1]==0):
                print("\n[",raiz.cent.izq.dato,"][",raiz.cent.der.dato,"][",raiz.cent.dato,"][",raiz.dato,"]")

            if(controlRama==0 & controlSubRama[0]==0 & controlSubRama[1]==0):
                print("\n[",raiz.cent.cent.dato,"][",raiz.cent.dato,"][",raiz.dato,"]")
            opc=int(input("\nOprima 0 para salir u oprima otro número del menú dado anteriormente para mostrar otro recorrido del árbol: "))
else:
    print("\nFin del programa\n")