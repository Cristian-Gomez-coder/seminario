def calcular_total(v:list):
    """calcula el todas las celdas con * al rededor

    Args:
        v (list): vector con celdas a analizar
    Retorns:
        lista(lista):devuelve un vector de string analizado con la cantidad de * al rededor de cada celda
    """
    def calcular_posicion(v:list, y: int, x:int):
        """calcula la cantidad de * al rededor de x,y

        Args:
            v (list): lista a calcular
            y (int): posicion inicial en alto
            x (int): posicion inicial en ancho

        Returns:
            cant: devuelve la cantidad de * alrededor de la posicion inicial
        """
        cant = 0
        cero=0
        max_y= len(v)
        max_x= len(v[y])
        if (y+1) < max_y and (x+1) < max_x and "*" == v[y+1][x+1]:
            cant+=1
        if (y+1) < max_y  and "*" == v[y+1][x]:
            cant+=1
        if y+1 < max_y and x-1 >= cero and "*" == v[y+1][x-1]:
            cant+=1
        if y-1 >= cero  and "*" == v[y-1][x]:
            cant+=1
        if y-1 >= cero and x+1< max_x and "*" == v[y-1][x+1]:
            cant+=1
        if y-1 >= cero and x-1 >=cero and "*" == v[y-1][x-1]:
            cant+=1
        if x-1 >= cero and "*" == v[y][x-1]:
            cant+=1
        if  x+1 <max_x and "*" == v[y][x+1]:
            cant+=1
        return cant
        
    lista=[]
    for y in range(len(v)):
        cad=""
        for x in range(len(v[y])):
            if v[y][x]!= "*":
                cad = cad + str(calcular_posicion(v, y, x))
            else:
                cad=cad +"*"
        lista.append(cad)
    #print(lista)
    return lista
minas= ['-*-*-','--*--','----*','*----']
print(calcular_total(minas))