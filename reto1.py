name = input("ingrese el nombre de producto ==> ");
code = input("ingrese el còdigo del producto ==> ");
costo = int(input("ingrese el costo del producto ==> "));

utilidad = costo * 1.2;
costoUtilidad = utilidad + costo;
ivaCostoUtilidad = costoUtilidad * 0.15;
precioVenta = ivaCostoUtilidad + costoUtilidad


print("El producto ", name , " con còdigo ", code, " tiene un precio de venta ==>", precioVenta)