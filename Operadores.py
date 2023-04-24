
nombre = input("Ingrese su numbre: ")
apellidos = input("Ingrese sus apellidos: ")

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def Multiplicacion(a,b):
    return a*b
def Division(a,b):
    return a/b

while True:
    print("")
    print("***Menu Principal***")
    print("1) Sumar numeros :")
    print("2) Restar numeros :")
    print("3) Multiplicar numeros :")
    print("4) Dividir numeros :")
    print("5) Tablas de multiplicar:")
    print("6) SALIR")
    opc = int(input("Selecciona una opcion: "));
    
    if opc == 1:
        n1 = int(input("Ingresa el primer numero entero: "));
        n2 = int(input("Ingresa el segundo numero entero: "));
        print("")
        print('La suma de sus numeros es:', suma(n1,n2));
    elif opc == 2:
        n1 = int(input("Ingresa el primer numero entero: "));
        n2 = int(input("Ingresa el segundo numero entero: "));
        print("")
        print('La resta de sus numeros es:', resta(n1,n2));
    elif opc == 3:
        n1 = int(input("Ingresa el primer numero entero: "));
        n2 = int(input("Ingresa el segundo numero entero: "));
        print("")
        print('La multiplicacion de sus numeros es:', Multiplicacion(n1,n2));
    elif opc == 4:
        n1 = int(input("Ingresa el primer numero entero: "));
        n2 = int(input("Ingresa el segundo numero entero: "));
        print('La division de sus numeros es:',Division(n1,n2));
    elif opc == 5:
        n1 = int(input("Ingresa el primer numero entero: "));
        n2 = int(input("Ingresa el segundo numero entero: "));
        print("")
        print('A) Mostrar la tabla de muliplicar del primer numero: ')
        print('B) Mostrar la tabla de muliplicar del segundo numero: ')
        respuesta2 = int(input("Seleccionar opcion 1 o 2: "))
        if respuesta2 == 1 :
            print("")
            print('La tabla de multiplicacion de tu primer numero es:')
            for x in range(1,11):
                n3 = x * n1 ;
                print('1) ', n1,('x'),x,(': '),   n3)
        elif respuesta2 == 2:
            print('La tabla de multiplicacion de tu segundo numero es:')
            for x in range(1,11):
                n3 = x * n2 ;
                print('1) ', n2,('x'),x,(': '),   n3) 
        else:
            print("")
            print("**Opcion invalida**")  
            print("")         

    elif opc ==6:
        print("")
        print(nombre, apellidos)
        print("Gracias por utilizar nuestra app, espero que te haya sido de ayuda")
        print("Hasta pronto!")
        print("")
        exit()            
    else:
        print("")
        print("Opcion Invalida, favor ingresar un valor correcto")            




   
    

   

       
              
           
       







