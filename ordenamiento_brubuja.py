
import random

def ordenamiento_brubuja(lista):
    n= len(lista)
    for i in range(n):
        for j in range(n-i-1): #  0(n**2)           
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))


    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)
    newLista= ordenamiento_brubuja(lista)
    print(newLista)
    # print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en a lista')