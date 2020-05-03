
import random

def busqueda_mezcla(lista,dondEsta=''):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista [medio:]
        
        print(izquierda, '*'*5, derecha)
        ##llamada recursiva en cada mitad
        busqueda_mezcla(izquierda,'izquierda')
        busqueda_mezcla(derecha,'derecha')
        #iteradores para recorrer las dos sublistas
        i=0
        j=0
        #iterador para la lista principal
        k=0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k]= izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
                lista[k] = izquierda[i]
                i += 1
                k += 1

        while j < len(derecha):
                lista[k] = derecha [j]
                j += 1
                k += 1
        
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

       
    return lista




if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))


    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)
    newLista= busqueda_mezcla(lista)
    print(newLista)
    # print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en a lista')