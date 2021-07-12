
productos = {
    1 : ["Manzanas", 8000, 550],
    2 : ["Limones", 2300, 15],
    3 : ["Peras", 2500, 38],
    4 : ["Arandanos", 9300, 55],
    5 : ["Tomates", 2100, 42],
    6 : ["Fresas", 4100, 33],
    7 : ["Helado", 4500, 41],
    8 : ["Galletas", 500, 833],
    9 : ["Chocolates", 3900, 999],
    10 : ["Jamon", 17000, 10]
}

accion = input()
datos = input().split()
datos[0] = int(datos[0])
datos[2] = float(datos[2])
datos[3] = int(datos[3])

def actualizar(productos, datos):
    if datos[0] in productos:
        indice = datos[0]
        datos.pop(0)
        productos[indice] = datos
        return True
    return False

def agregar(productos, datos):
      if datos[0] in productos:
          return False
      indice = datos[0]
      datos.pop(0)
      productos[indice] = datos
      return True

def borrar(productos, datos):
    if datos[0] in productos:
        productos.pop(datos[0])
        return True
    return False

def precioMayor(productos):
    mayor = list(productos.keys())[0]
    for x in productos:
        if productos[x][1] > productos[mayor][1]:
            mayor = x
    return productos[mayor][0]

def precioMenor(productos):
    menor = list(productos.keys())[0]
    for x in productos:
        if productos[x][1] < productos[menor][1]:
            menor = x
    return productos[menor][0]

def promedioPrecio(productos):
    sumatoria = 0
    for x in productos:
        sumatoria += productos[x][1]
        promedio = sumatoria/len(productos)
    return round(promedio, 1)

def valorInventario(productos):
    sumatoria = 0
    for x in productos:
        sumatoria += productos[x][1] * productos[x][2] 
    return round(float(sumatoria), 1)

if accion == 'ACTUALIZAR':
    llamado = actualizar(productos, datos)
if accion == 'AGREGAR':
    llamado = agregar(productos, datos)
if accion == 'BORRAR':
    llamado = borrar(productos, datos)

precioMa = precioMayor(productos)
precioMe = precioMenor(productos)
promP = promedioPrecio(productos)
valorInv = valorInventario(productos)

if(llamado == True):
    print(precioMa, precioMe, promP, valorInv )
else:
    print('ERROR')



