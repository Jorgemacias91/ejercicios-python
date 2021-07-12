
n = int(input())
listas = []
for i in range(n):
    valor = input().split()
    listas.append(valor)

bandera = False

for i in range(len(listas)):
    if(
        int(listas[i][0]) >= 3
        and int(listas[i][1]) >= 4
        and int(listas[i][2]) <= 24
        and int(listas[i][3]) <= 10
    ):
     bandera = True
     print(int(listas[i][4]))
   

if(bandera == False):
    print('NO DISPONIBLE')







