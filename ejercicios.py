def tablaMultiplicacion(numero):
    index=0
    for n in range(0, 10):
        index= index + 1 
        print(f'index {index} x {numero} = {index*numero}')
    
def operaciones(n1, n2):
         print(f'index {index} x {numero} = {index*numero}')
         print(f'index {index} x {numero} = {index*numero}')
         print(f'index {index} x {numero} = {index*numero}')
         print(f'index {index} x {numero} = {index*numero}')

def indetifica_numero(numero):
    if(numero>0):
        print(f'Este numero: {numero} es positivo')
    elif ( numero ==0 ):
        print('Este numero es igual a 0')
    else:
        print(f'Este numero: {numero} es menor a 0')
    
def operacion_entre_numeros(n1, n2):
    suma=0
    pares = 0
    impares = 0
    for n in range(n1, n2+1):
        if(n % 2 == 0):
            pares = n + pares
        else:
            impares = n +impares
        suma = n + suma
    print(f'Suma de los numeros desde {n1} hasta {n2} es igual a:{suma}')
    print(f'la suma de los pares es {pares}')
    print(f'la suma de los impares es {impares}')

def usuario_and_pas(user, password, intentos):

    if(user=='root' and password=='toor'):
        print('¡Bienvenido!')
    elif( intentos > 0 ):
        print(f'Vuelve a intentarlo tiene {intentos} intentos')
        intentos = intentos - 1
        user =  str(input('Ingresa usuario: '))
        password =  str(input('Ingresa password: '))
        usuario_and_pas(user, password, intentos)
    else:       
        print('Acceso fallido')

def delet_impar_list(lista):
    lista_nueva = list(lista)
    print(f'lista { lista}')      
    for l in lista:       
        if( l % 2 != 0 ):
            print(f'elemento removido {l} ')
            lista_nueva.remove(l)


    return lista_nueva.sort()
   
def compara_lista(lista_uno, lista_dos):
    find_elements = []
    for element in lista_uno:
        if element in lista_dos:
            find_elements.append(element)

    if(len(find_elements)>0):
        print(f'Elementos encontrados {find_elements}')
    else:
        print('No se encontro nigun elemento repetido')

def numero_veces_repeti_convetir_diccionario(lista):
    diccionario = {}
    # for element in lista:
    #     diccionario[element] = lista.count(element)
    # return diccionario
    return { element: lista.count(element) for element in lista}

def for_diccionario_convert_lista_sin_valores_duplicados(diccionario):
    lista = []
    for key , value in diccionario.items():
        if value not in lista:
            lista.append(value)

    return lista


if __name__ == '__main__':
    # numero_tabla = int(input('Escribe que tabla quieres? '))
    # numero = int(input('Escribe un numero:  '))
    # n1 = int(input('Escribe el primer numero:  '))
    # n2 = int(input('Escribe el segundo numero:  '))
    # operacion_entre_numeros(n1, n2)
    # user =  str(input('Ingresa usuario: '))
    # password =  str(input('Ingresa password: '))
    # usuario_and_pas(user, password, 2)

    # numero_mayor = 0 
    # for i in range(5):        
    #     numero = int(input('ingrese un numero: ')) 
    #     if ( numero > numero_mayor ):
    #         numero_mayor = numero
            
    # lista_d = delet_impar_list([12, 23, 5, 29, 92, 64])

    #comparacion entre dos listas
    # lista_uno = []
    # lista_dos = []  
    # print('Ingresa los datos de la primera lista')
    # for i in range(5):    
    #     new_numero = int(input('ingrese un numero: ')) 
    #     lista_uno.append(new_numero)

    # print('Ingresa los datos de la segunda lista')
    # for i in range(5):    
    #     new_numero = int(input('ingrese un numero: ')) 
    #     lista_dos.append(new_numero)   
    
    # compara_lista(lista_uno, lista_dos)
  
    #numero de veces que se repite un elemento convertilo en un dicacionario
    # print(f'diccinario {numero_veces_repeti_convetir_diccionario([12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23])}')
    lista = for_diccionario_convert_lista_sin_valores_duplicados({'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5})
    print(f'lista {lista}')

