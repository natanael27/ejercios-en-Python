def listaInvertida(lista):
    ln=[]

    for i in range(len(lista)-1,-1,-1):
        ln.append(lista[i])
    return(ln)