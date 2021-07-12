N ,K = [int (x) for x in list(input().split(' '))]
examenes = [int (x) for x in list(input().split(' '))]

copiaDetectaProfesor = 0
copiaDetectada = 0

diccionario = dict()

for p1t, p2t in enumerate(examenes):
    if(p2t in diccionario and p1t - diccionario.get(p2t) <= K):
        copiaDetectaProfesor += 1
    
    if(p2t in diccionario):
        copiaDetectada += 1
    
    diccionario[p2t] = p1t

print(copiaDetectada, copiaDetectaProfesor)

